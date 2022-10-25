import requests
import datetime
from pprint import pprint
from apps.products.models import Product
from apps.siigos.models import DocumentType
from apps.payments.models import Payment, Transaction
from apps.company.models import Company
from apps.clients.models import Clients
from apps.bookings.models import Booking
import time

def save_error(payment,newError):

    erroresOld = ""
    if(payment.errores):
        erroresOld = payment.errores
    payment.errores =f'{erroresOld} | {newError}'
    payment.save()

def validate_if_client_exists_in_siigo(document_number):
    """
        This function return True if giving the document number exists in siigo, and false if not
    """
    company = Company.objects.first()
    url = f'{company.siigo_host}/customers?identification={document_number}'
    headers = {
        'Accept': 'application/json',
        'Authorization': company.siigo_access_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        if(response_json["results"]):
            return True
    return False

def create_client_in_siigo(payment):
    """
        This function Creates a Client in siigo, according to the client model
    """
    print("creando cliente...")
    client = Clients.objects.get(pk=payment.client.id)
    document_number = client.identification_number.replace('.', '')

    company = Company.objects.first()
    url = f'{company.siigo_host}/customers'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': company.siigo_access_token
    }
    payload = {
        "type": "Customer",
        "person_type": "Person",
        "id_type": "13",
        "identification": document_number, #identification_number
        "name": [
            client.first_name, # first_name
            client.last_name, # last_name
        ],
        "commercial_name": "Siigo",
        "address": {
            "address": client.address,# address
            "city": {
                "country_code": "Co",
                "state_code": "19",
                "city_code": "19001"
            }
        },
        "phones": [
            {
                "number": client.phone.replace(" ","")[-10:], # phone number, the last 10 characters
            }
        ],
        "contacts": [
            {
                "first_name": client.first_name, #first_name
                "last_name": client.last_name, #last_name
                "email": client.email # email
            }
        ]
    }
    print(">>>>>>")
    pprint(payload)
    response = requests.post(url, json=payload, headers=headers)
    
    print("<<<<<<")
    status_code = response.status_code
    print(f'status code: {status_code}')
    response_json = response.json()
    pprint(response_json)

    if status_code == 201:
        client.siigo = True
        client.consumidor_final = False
        client.save()
        return True
    elif(status_code == 400):
        errors = response_json["Errors"]
        errorestring = "creando_cliente "
        for error in errors:
            if(error["Params"]):
                paramsstr = ""
                for param in error["Params"]:
                    paramsstr = f'{paramsstr}, {param}'
            errorestring += f'codigo:{error["Code"]} mensaje:{error["Message"]}'
            errorestring += f' parametros:({paramsstr})' if paramsstr else errorestring
        save_error(payment, errorestring)

    return False

def facturar_electronicamente(payment, document_number):
    print('facturando...')
    company = Company.objects.first()
    url = f'{company.siigo_host}/invoices'

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': company.siigo_access_token
    }

    bookings = Booking.objects.filter(Payment=payment)
    products = Product.objects.filter(Payment=payment)
    transactions = Transaction.objects.filter(Payment=payment)
    fecha_actual = datetime.datetime.now ()
    date = datetime.datetime.strftime(fecha_actual, '%Y-%m-%d')

    items = []
    for booking in bookings:
        discount = float(booking.discount) if booking.discount else 0
        percentaje_with_discount = 100-discount
        price = booking.price*100/percentaje_with_discount
        items.append(
            {
                "code": booking.service.replace(' ', ''),# nombre del servicio
                "quantity": 1,
                "price": price,
                "discount": booking.discount if booking.discount else 0,
            }
        )
    for product in products:
        items.append(
            {
                "code": product.product.replace(' ', ''), # nombre del producto
                "quantity": product.quantity,
                "price": product.product_price,
                "discount": product.discount if product.discount else 0,
            }
        )
    
    for item in items:
        if not item["code"]:
            save_error(payment,f'item: sin nombre')
            return False
        if not item["price"]:
            save_error(payment,f'item: {item["code"]} sin precio')
            return False
        if not item["quantity"]:
            save_error(payment,f'item: {item["code"]} sin cantidad')
            return False

    payments = []
    descuento = 0
    for transaction in transactions:
        forma_de_pago = None
        document_type = DocumentType.objects.filter(name=transaction.payment_method).first()
        if(document_type):
            forma_de_pago=document_type.siigo_id
        else:
            save_error(payment,f'no se encontro metodo de pago: {transaction.payment_method}')
            return False
        
        payments.append(
            {
                "id": forma_de_pago, # este id es de la forma de pago
                "value": transaction.amount # este value es el total apagar
            }
        )
    
    center = ""
    location_name = payment.location_name
    location_name = location_name.replace(" ","").upper()
    if(location_name=="TEQUENDAMA"):
        center=183
    elif(location_name=="SHALONSEDEAVENTURAPLAZA"):
        center=185
    elif(location_name=="SHALONSEDECASASHALON"):
        center=66
    elif(location_name=="SEDEADMINISTRATIVA"):
        center=58
    else:
        save_error(payment, "error en ubicacion")
    
    factura = None
    factura = {
        "document": {
            "id": 13643
        },
        "date": date, # fecha de creacion factura esta va sujeta al campo del nombre y tipo de factura
        "customer": {
            "identification": document_number, # identification el numero de cedula del cliente
            "branch_office": 0
        },
        "cost_center": center, #   cost_center es el id del local donde se realizo la compra
        "seller": 352, # seller es el codigo de cajero o persona autorizada
        "observations": "sin observaciones",
        "items": items,
        "payments": payments,
    }

    print(">>>>>>")
    pprint(factura)
    response = requests.post(url, json=factura, headers=headers)
    
    print("<<<<<<")
    status_code = response.status_code
    print(f'status code: {status_code}')
    response_json = response.json()
    pprint(response_json)

    if status_code == 201:
        payment.comprobante_siigo = response_json["name"]
        payment.facturado=True
        payment.save()
        return True
    elif(status_code == 400):
        errors = response_json["Errors"]
        errorestring = "creando_factura "
        for error in errors:
            if(error["Params"]):
                paramsstr = ""
                for param in error["Params"]:
                    paramsstr = f'{paramsstr}, {param}'
            errorestring += f'codigo:{error["Code"]} mensaje:{error["Message"]}'
            errorestring += f' parametros:({paramsstr})' if paramsstr else errorestring

            if("The code doesn't exist" in error["Message"]):
                errorestring = f'Hay un item de venta que no existe en siigo'
            
            if("invalid_total_payments" in error["Code"]):
                errorestring = f'La suma de los items no cuadra con los pagos'
        save_error(payment, errorestring)
        return False

def facturar_elctronica_by_payment_id(id_payment):
    print("-------------------------------------------")
    print(f'facturando pago id: {id_payment} .......')
    document_number = ""

    payment = Payment.objects.get(pk=id_payment)
    payment.errores = ""
    payment.save()
    if(payment.facturado):
        save_error(payment,"ya facturado")
        return False
    if(not payment.facturable_electronica):
        save_error(payment,"no facturable electronicamente")
        return False

    if(payment.client.consumidor_final):
        time.sleep(3)
        return facturar_electronicamente(payment, "222222222222")
    else:
        if payment.client.identification_number:
            document_number = payment.client.identification_number
            document_number = document_number.replace('.', '')
        try:
            document_number = int(document_number)
        except Exception as e:
            print(e)
            document_number = None
        if(document_number):
            document_number = str(document_number)
            exists = validate_if_client_exists_in_siigo(document_number)
            if(not exists):
                exists = create_client_in_siigo(payment)
            if(exists):
                return facturar_electronicamente(payment, document_number)
        else:
            print("Cedula invalida")
            save_error(payment,"cedula invalida")
            return False


def get_payment_methods_in_siigo():
    """
        This function return and save the payment method
    """
    company = Company.objects.first()
    url = f'{company.siigo_host}/payment-types?document_type=FV'
    headers = {
        'Accept': 'application/json',
        'Authorization': company.siigo_access_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        print(response_json)
    return False