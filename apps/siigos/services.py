import requests
from pprint import pprint
from apps.products.models import Product
from apps.payments.models import Payment, Transaction
from apps.company.models import Company
from apps.clients.models import Clients
from apps.bookings.models import Booking

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

def create_client_in_siigo(id_client):
    # crear el cliente
    client = Clients.objects.get(pk=id_client)
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
    print("response creando un cliente")
    #response = requests.post(url, json=payload, headers=headers)
    #pprint(response.json())

    return True

def facturar_electronicamente(payment):
    print('facturando')

    
    document_number = payment.client.identification_number.replace('.', '')

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
    # payment = Payment.objects.filter(Payment=payment)
    

    items = []

    for booking in bookings:
        items.append({
                        # nombre del producto
                        "code": booking.service,
                        # cantidad a llevar del producto
                        "quantity": 1,
                        # precio a pagar
                        "price": booking.price,
                        "discount": booking.discount if booking.discount else 0,
            })
    for product in products:
        items.append({
                        # nombre del producto
                        "code": product.product,
                        # cantidad a llevar del producto
                        "quantity": product.quantity,
                        # precio a pagar
                        "price": product.price,
                        "discount": product.discount if booking.discount else 0,
            })

    print("itemmmmmmssssss")
    print(items)

    for transaction in transactions:
        items.append({
                        "number": transaction.ticker_number,
                        "amount": transaction.amount,
                        "installments": transaction.installments,
                        "payment_method": transaction.payment_method,
                        "payment_method_type": transaction.payment_method_type,
                        "bank": transaction.bank, 
      })
    print("Transsssssssssssssssssssssssssssacion")
    print(transaction)

    # for payment in Payment:
    #     items.append({
    #                     "document": {
    #                         "id": 13643
    #                     },
    #                     # fecha de creacion factura esta va sujeta al campo del nombre y tipo de factura
    #                     "date": payment.payment_date,
    #                     "customer": {
    #                         # identification el numero de cedula del cliente
    #                         "identification": document_number,
    #                         "branch_office": 0
    #                     },
    #                     #   cost_center es el id del local donde se realizo la compra
    #                     "cost_center": 185,
    #                     #  seller es el codigo de cajero o persona autorizada
    #                     "seller": 352,
    #                     "observations": "sin observaciones",
    #                     "items": items,
    #                     "payments": [
    #                         {
    #                             # este id es de la forma de pago
    #                             "id": 3142,
    #                             # este value es el total apagar
    #                             "value": Product.price
    #                         }
    #                     ],
    #                 }
    #     )
    # print("Paymennnnnnnnsssss")
    # print(payment)
    

   
    # response = requests.post(url, json=factura, headers=headers)
    # pprint(response)


def facturar_elctronica_by_payment_id(id_payment):
    payment = Payment.objects.get(pk=id_payment)
    print(f'facturando ....... {id_payment}')
    document_number = payment.client.identification_number
    document_number = document_number.replace('.', '')
    try:
        document_number = int(document_number)
    except Exception as e:
        print(e)
        document_number = None
    if(document_number):
        print(f'cliente numero documento {document_number}')
        exists = validate_if_client_exists_in_siigo(document_number)
        if(exists):
            print("el cliente existe")
        else:
            print("el cliente no existe")
            create_client_in_siigo(payment.client.id)
        print("chupar pijas")
        facturar_electronicamente(payment)

    else:
        print("no lo hace")
        erroresOld = ""
        if(payment.errores):
            erroresOld = payment.errores

        payment.errores =f'{erroresOld} | cedula invalida'
        payment.save()
    
    
    
    # to do
    # - traer cliente de siigo
    #   - si no existe crearlo
    #   - si existe no hacer nada
    # - facturar 
    return True