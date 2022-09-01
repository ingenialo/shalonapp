# django imports
from django.shortcuts import render
from django.http import HttpResponse

# third party imports
from django.http import JsonResponse
import requests
import json
from pprint import pprint


# import models
from apps.bookings.models import Booking
from apps.clients.models import Clients
from apps.company.models import Company
from apps.payments.models import Payment
from apps.products.models import Product
from apps.receipts.models import Receipt
from apps.payments.models import Transaction
from config.utils.models import update_model


def conv(value):
    if value:
        return value
    else:
        return None

# Create your views here.


def list_payments(request):
    company = Company.objects.first()
    print(company)
    url = f"{company.agenda_pro_host}/payments/"
    headers = {
        "Accept": "application/json",
        "Authorization": company.agenda_pro_token
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()

    f = open("./apps/payments/salida1.json", "w")
    f.write(json.dumps(response_json))
    f.close()

    if response.status_code == 200:

        for paymentjson in response_json["payments"]:
            if(paymentjson):
                print("------------------------------------------------------------")
                pprint(paymentjson['id'])
                clientejson = paymentjson["client"]

                cliente = {
                    'agenda_id': conv(clientejson['id']),
                    'first_name': conv(clientejson['first_name']),
                    'last_name': conv(clientejson['last_name']),
                    'email': conv(clientejson['email']),
                    'identification_number': conv(clientejson['identification_number']),
                    'phone': conv(clientejson['phone']),
                    'second_phone': conv(clientejson['second_phone']),
                    'age': conv(clientejson['age']),
                    'birth_day': conv(clientejson['birth_day']),
                    'birth_month': conv(clientejson['birth_month']),
                    'birth_year': conv(clientejson['birth_year']),
                    'record_number': conv(clientejson['record_number']),
                    'address': conv(clientejson['address']),
                    'district': conv(clientejson['district']),
                    'city': conv(clientejson['city']),
                }
                clientedb, created = Clients.objects.update_or_create(
                    agenda_id=clientejson["id"], defaults=cliente)

                pago = {
                    'agenda_id': conv(paymentjson['id']),
                    'payment_date': conv(paymentjson['payment_date']),
                    'agenda_location_id': conv(paymentjson['location_id']),
                    'location_name': conv(paymentjson['location_name']),
                    'amount': conv(paymentjson['amount']),
                    'paid_amount': conv(paymentjson['paid_amount']),
                    'change_amount': conv(paymentjson['change_amount']),
                    'employee_code_id': conv(paymentjson['employee_code_id']),
                    'employee_code_name': conv(paymentjson['employee_code_name']),
                    'client': clientedb,

                }
                paymentdb, created = Payment.objects.update_or_create(
                    agenda_id=paymentjson["id"], defaults=pago)

                for receiptjson in paymentjson["receipts"]:
                    pprint(receiptjson)
                    recibo = {
                        'Payment': paymentdb,
                        'agenda_id': conv(receiptjson['id']),
                        'amount': conv(receiptjson['amount']),
                        'date': conv(receiptjson['date']),
                        'number': conv(receiptjson['number']),
                        'receipt_type': conv(receiptjson['receipt_type']),
                    }
                    receiptdb, created = Receipt.objects.update_or_create(
                        agenda_id=receiptjson["id"], defaults=recibo)

                    for bookingsjson in paymentjson["bookings"]:
                        pprint(bookingsjson)
                        booking = {
                            'Payment': paymentdb,
                            'Receipt': receiptdb,
                            'web_origin': conv(bookingsjson['web_origin']),
                            'provider_lock': conv(bookingsjson['provider_lock']),
                            'is_session': conv(bookingsjson['is_session']),
                            'is_session_booked': conv(bookingsjson['is_session_booked']),
                            'notes': conv(bookingsjson['notes']),
                            'price': conv(bookingsjson['price']),
                            'discount': conv(bookingsjson['discount']),
                            'service': conv(bookingsjson['service']),
                            'provider': conv(bookingsjson['provider']),
                            'status': conv(bookingsjson['status']),
                            'agenda_receipt_id': conv(bookingsjson['receipt_id']),
                            'start': conv(bookingsjson['start']),
                            'end': conv(bookingsjson['end']),
                        }
                        bookingdb, created = Booking.objects.update_or_create(
                            agenda_receipt_id=bookingsjson["receipt_id"], service=bookingsjson["service"], defaults=booking)

                    for mockbookingsjson in paymentjson["mock_bookings"]:
                        pprint(mockbookingsjson)
                        mockbooking = {
                            'Payment': paymentdb,
                            'Receipt': receiptdb,
                            'price': conv(mockbookingsjson['price']),
                            'discount': conv(mockbookingsjson['discount']),
                            'service': conv(mockbookingsjson['service']),
                            'provider': conv(mockbookingsjson['provider']),
                            'agenda_receipt_id': conv(mockbookingsjson['receipt_id']),
                        }
                        mockbookingdb, created = Booking.objects.update_or_create(
                            agenda_receipt_id=mockbookingsjson["receipt_id"], service=mockbookingsjson["service"], defaults=mockbooking)

                    for productjson in paymentjson["products"]:
                        pprint(productjson)
                        producto = {
                            'Payment': paymentdb,
                            'Receipt': receiptdb,
                            'price': conv(productjson['price']),
                            'discount': conv(productjson['discount']),
                            'quantity': conv(productjson['quantity']),
                            'product': conv(productjson['product']),
                            'product_brand': conv(productjson['product_brand']),
                            'product_display': conv(productjson['product_display']),
                            'product_category': conv(productjson['product_category']),
                            'product_price': conv(productjson['product_price']),
                            'agenda_receipt_id': conv(productjson['receipt_id']),
                            'seller_details': conv(productjson['seller_details']),

                        }
                        productdb, created = Product.objects.update_or_create(
                            agenda_receipt_id=productjson["receipt_id"], product=productjson["product"], defaults=producto)

                    for downpaymentjson in paymentjson["down_payment"]:
                        for paymenttransactionsjson in downpaymentjson["payment_transactions"]:
                            transacion = {
                                'Payment': paymentdb,
                                'number': conv(paymenttransactionsjson['number']),
                                'amount': conv(paymenttransactionsjson['amount']),
                                'installments': conv(paymenttransactionsjson['installments']),
                                'payment_method': conv(paymenttransactionsjson['payment_method']),
                                'payment_method_type': conv(paymenttransactionsjson['payment_method_type']),
                                'bank': conv(paymenttransactionsjson['bank']),
                            }
                            pprint(transacion)
                            transationdb, created = Transaction.objects.update_or_create(
                                number=conv(paymenttransactionsjson["number"]),
                                amount=conv(paymenttransactionsjson["amount"]),
                                installments=conv(
                                    paymenttransactionsjson["installments"]),
                                payment_method=conv(
                                    paymenttransactionsjson["payment_method"]),
                                payment_method_type=conv(
                                    paymenttransactionsjson["payment_method_type"]),
                                bank=conv(paymenttransactionsjson["bank"]),
                                defaults=transacion
                            )

    return HttpResponse('<h1> Get data from agenda pro successfully <span>&#128512;</span> </h1>')


def generate_token():
    company = Company.objects.first()
    username = company.siigo_username
    access_key = company.siigo_access_key

    url = "https://api.siigo.com/auth"
    payload = {'username': username, 'access_key': access_key}
    headers = {'Accept': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)
    pprint(response)
    if response.status_code == 200:
        response_json = response.json()
        access_token = response_json['access_token']
        print(access_token)
        company.siigo_access_token = access_token
        company.save() 
        return access_token
    return None



def testsiigo(request):
    company = Company.objects.first()

    # access_token = generate_token()
    # print(access_token)
    # print('---------------------------------------------------------------------')

    url = "https://api.siigo.com/v1/customers"
    headers = {
        'Accept': 'application/json',
        'Authorization': company.siigo_access_token
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        response_json = response.json()

        f = open("./apps/payments/salida2.json", "w")
        f.write(json.dumps(response_json))
        f.close()
        return HttpResponse('<h1> testsiigo successfully <span>&#128512;</span> </h1>')
    elif response.status_code==401:
        access_token = generate_token()
        return HttpResponse(f'<h1> se regenero el token <span>&#128512;</span> </h1> <p>{access_token}</p>')
    else:
        return HttpResponse('<h1> no paso </span> </h1>')


def test_siigo_create_client(request):

    access_token = generate_token()
    list_payments()

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': access_token
    }

    url = "https://api.siigo.com/v1/customers"

    payload = {
        "type": "Customer",
                "person_type": "Person",
                "id_type": "13",
                # identification_number
                "identification": "123234567",
                "name": [
                    # first_name
                    "prueba7",
                    # last_name
                    "prueba7",
                ],
        "commercial_name": "Siigo",
        "address": {
                    # address
                    "address": "carrera7 #7-7",
                    "city": {
                        "country_code": "Co",
                        "state_code": "19",
                        "city_code": "19001"
                    }
                },
        "phones": [
                    {
                        # phone
                        "number": "3108473323",
                    }
                ],
        "contacts": [
                    {
                        # first_name
                        "first_name": "prueba7",
                        # last_name
                        "last_name": "prueba7",
                        # email
                        "email": "prueba7@prueba7.com"
                    }
                ]
    }
    response = requests.post(url, json=payload, headers=headers)
    pprint(response)
    return HttpResponse('<h1> test_siigo_create_client <span>&#128512;</span> </h1>')


def test_siigo_create_factura(request):

    access_token = generate_token()
    test_siigo_create_client()

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': access_token
    }

    url = "https://api.siigo.com/v1/invoices"

    factura = {
        "document": {
            "id": 13643
        },
        # fecha de creacion factura esta va sujeta al campo del nombre y tipo de factura
        "date": "2015-12-15",
        "customer": {
            # identification el numero de cedula del cliente
            "identification": "123234567",
            "branch_office": 0
        },
        #   cost_center es el id del local donde se realizo la compra
        "cost_center": 185,
        #  seller es el codigo de cajero o persona autorizada
        "seller": 352,
        "observations": "Observaciones",
        "items": [
            {
                        # nombre del producto
                        "code": "CREMACICATRIZACIONMICRO",
                        # cantidad a llevar del producto
                        "quantity": 1,
                        # precio a pagar
                        "price": 22000,
                        "discount": 0.0,

            }
        ],
        "payments": [
            {
                # este id es de la forma de pago
                "id": 3142,
                # este value es el total apagar
                "value": 22000
            }
        ],
    }
    response = requests.post(url, json=factura, headers=headers)
    pprint(response)
    return HttpResponse('<h1> test_siigo_create_client <span>&#128512;</span> </h1>')
