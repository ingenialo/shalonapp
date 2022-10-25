import requests
import datetime
from pprint import pprint
from apps.products.models import Product
from apps.payments.models import Payment, Transaction
from apps.company.models import Company
from apps.clients.models import Clients
from apps.bookings.models import Booking

def save_error(payment,newError):

    erroresOld = ""
    if(payment.errores):
        erroresOld = payment.errores
    payment.errores =f'{erroresOld} | {newError}'
    payment.save()

def validate_if_client_exists_in_siigo(document_number):

    company = Company.objects.first()
    url = f'{company.siigo_host}/customers?identification={document_number}'
    headers = {
        'Accept': 'application/json',
        'Authorization': company.siigo_access_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        #print(response_json["results"])
        if(response_json["results"]):
            return True
    return False

def create_client_in_siigo(payment):
    
    # crear el cliente
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
        # identification_number
        "identification": document_number,
        "name": [
            # first_name
            client.first_name,
            # last_name
            client.last_name,
        ],
        "commercial_name": "Siigo",
        "address": {
                    # address
                    "address": client.address,
                    "city": {
                        "country_code": "Co",
                        "state_code": "19",
                        "city_code": "19001"
                    }
                },
        "phones": [
                    {
                        # phone
                        "number": client.phone.replace(" ","")[-10:],
                    }
                ],
        "contacts": [
                    {
                        # first_name
                        "first_name": client.first_name,
                        # last_name
                        "last_name": client.last_name,
                        # email
                        "email": client.email
                    }
                ]
    }
    pprint(payload)
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        client.siigo = True
        client.consumidor_final = False
        client.save()
        return True
    elif(response.status_code == 400):
        response_json = response.json()
        errors = response_json["Errors"]
        errorestring = ""
        for error in errors:
            if(error["Params"]):
                paramsstr = ""
                for param in error["Params"]:
                    paramsstr = f'{paramsstr}, {param}'
            errorestring += f'codigo:{error["Code"]} mensaje:{error["Message"]}'
            errorestring += f' parametros:({paramsstr})' if paramsstr else errorestring
        save_error(payment, errorestring)
    else:
        pprint(response.json())

    return True

def facturar_electronicamente(payment, document_number):
    print('facturando')
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
    
    print('fecha actual')
    print(date)

    items = []

    for booking in bookings:
        items.append({
                        # nombre del producto
                        "code": booking.service.replace(' ', ''),
                        # cantidad a llevar del producto
                        "quantity": 1,
                        # precio a pagar
                        "price": booking.price,
                        "discount": booking.discount if booking.discount else 0,
            })
    for product in products:
        items.append({
                        # nombre del producto
                        "code": product.product.replace(' ', ''),
                        # cantidad a llevar del producto
                        "quantity": product.quantity,
                        # precio a pagar
                        "price": product.price,
                        "discount": product.discount if booking.discount else 0,
            })

    print("itemmmmmmssssss")
    print(items)

    payments = []
    for transaction in transactions:
        forma_de_pago = None
        if(transaction.payment_method=="Efectivo"):
            forma_de_pago=3142
        elif(transaction.payment_method=="Tarjeta de Débito"):
            forma_de_pago=3144
        elif(transaction.payment_method=="Tarjeta Crédito"):
             forma_de_pago=3145
        elif(transaction.payment_method=="Transferencia"):
            forma_de_pago=7383
        else:
            print('no se encontro forma de pago')
        payments.append({
                        # este id es de la forma de pago
                        "id": forma_de_pago,
                        # este value es el total apagar
                        "value":  transaction.amount
        })
    print("forma de pagooooooooooooo")
    print(payments)
    
    center = ""
    location_name = payment.location_name
    location_name = location_name.replace(" ","").upper()
    if(location_name=="TEQUENDAMA"):
        center=183
    elif(location_name=="SHALONSEDEAVENTURAPLAZA"):
        center=185
    elif(location_name=="SHALONSEDECASASHALON"):
        center=66
    else:
        save_error(payment, "error en ubicacion")
    
    factura = {
                "document": {
                    "id": 13643
                },
                # fecha de creacion factura esta va sujeta al campo del nombre y tipo de factura
                "date": date,
                "customer": {
                    # identification el numero de cedula del cliente
                    "identification": document_number,
                    "branch_office": 0
                },
                #   cost_center es el id del local donde se realizo la compra
                "cost_center": center,
                #  seller es el codigo de cajero o persona autorizada
                "seller": 352,
                "observations": "sin observaciones",
                "items": items,
                "payments": payments,
            }
    print("-------line 200--------")
    pprint(factura)

   
    response = requests.post(url, json=factura, headers=headers)
    print("-----line 205----------")
    print(response.status_code)
    if response.status_code == 201:
        response_json = response.json()
        print("ooookkkkkkk")
        pprint(response_json)
        payment.comprobante_siigo = response_json["name"]
        payment.facturado=True
        payment.save()
    elif(response.status_code == 400):
        response_json = response.json()
        errors = response_json["Errors"]
        errorestring = ""
        for error in errors:
            if(error["Params"]):
                paramsstr = ""
                for param in error["Params"]:
                    paramsstr = f'{paramsstr}, {param}'
            errorestring += f'codigo:{error["Code"]} mensaje:{error["Message"]}'
            errorestring += f' parametros:({paramsstr})' if paramsstr else errorestring
        save_error(payment, errorestring)
        print(errorestring)

    else:
        pprint(response.json())


def facturar_elctronica_by_payment_id(id_payment):
    payment = Payment.objects.get(pk=id_payment)
    payment.errores = ""
    payment.save()
    if(payment.facturado):
        save_error(payment,"ya facturado")
        return True
    if(not payment.facturable_electronica):
        save_error(payment,"no facturable electronicamente")
        return True

    print(f'facturando ....... {id_payment}')
    document_number = ""

    
    if(payment.client.consumidor_final):
        facturar_electronicamente(payment, "222222222222")
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
            exists = validate_if_client_exists_in_siigo(document_number)

            if(exists):
                print("el cliente existe")
                # to do: update the client
            else:
                print("el cliente no existe")
                create_client_in_siigo(payment)

            facturar_electronicamente(payment, document_number)
        else:
            print("Cedula invalida")
            save_error(payment,"cedula invalida")

    
    
    
    
    # to do
    # - traer cliente de siigo
    #   - si no existe crearlo
    #   - si existe no hacer nada
    # - facturar 
    return True