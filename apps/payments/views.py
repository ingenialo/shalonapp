# django imports
from django.shortcuts import render
from django.http import HttpResponse

# third party imports
from django.http import JsonResponse
import datetime
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
    existData = True
    page = 0
    date = datetime.datetime.now()
    fecha = date.strftime('%y-%m-%d')
    print(fecha)
    while(existData):
        page += 1
        url = f"{company.agenda_pro_host}/payments/?page={page}&from={fecha}&to={fecha}"
        headers = {
            "Accept": "application/json",
            "Authorization": company.agenda_pro_token
        }
        response = requests.get(url, headers=headers)
        response_json = response.json()


        if response.status_code == 200:
            if response_json["payments"]:

                for paymentjson in response_json["payments"]:
                    if(paymentjson):
                        print("------------------------------------------------------------")
                        pprint(paymentjson['id'])
                        clientejson = paymentjson["client"]
                        urlclient =f"{company.agenda_pro_host}/clients/{clientejson['id']}"
                        responseclient = requests.get(urlclient, headers=headers)
                        clientejson = responseclient.json()
                        tipo_docto=[x for x in clientejson['custom_attributes'] if x["custom_attribute_id"] == 12442]
                        print(tipo_docto[0]["value"])

                        cliente = {
                            'agenda_id': conv(clientejson['id']),
                            'first_name': conv(clientejson['first_name']),
                            'last_name': conv(clientejson['last_name']),
                            'email': conv(clientejson['email']),
                            'document_type': conv(tipo_docto[0]["value"]),
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
                                        'ticker_number': conv(paymenttransactionsjson['number']),
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
            else:
                existData=False
    return HttpResponse('<h1> Get data from agenda pro successfully <span>&#128512;</span> </h1>')

