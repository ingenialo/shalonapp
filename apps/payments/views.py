from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from pprint import pprint
from apps.clients.models import Clients
from apps.payments.models import Payment
from apps.payments.models import Transaction
from config.utils.models import update_model

def conv(value):
    if value:
        return value
    else:
        return None

# Create your views here.
def list_payments(request):
    url = "https://agendapro.com/api/public/v1/payments"
    headers = {
    "Accept": "application/json",
    "Authorization": "Basic MWk4c3RicDY6dGd5ZWRqd3FtZjM0ejNwdGttNjM0bTJid2llM28zanBjZWhtbWI0Zg=="
    }
    response = requests.get(url, headers=headers) 
    response_json =response.json()
    
    f = open("./apps/payments/salida.json", "w")
    f.write(json.dumps(response_json))
    f.close()
    
    if response.status_code == 200:
        
        for paymentjson in response_json["payments"]:
            if(paymentjson):
                clientejson=paymentjson["client"]
                
                cliente = {
                    'agenda_id' : conv(clientejson['id']),
                    'first_name' : conv(clientejson['first_name']),
                    'last_name' : conv(clientejson['last_name']),
                    'email' : conv(clientejson['email']),
                    'identification_number' : conv(clientejson['identification_number']),
                    'phone' : conv(clientejson['phone']),
                    'second_phone' : conv(clientejson['second_phone']),
                    'age' : conv(clientejson['age']),
                    'birth_day' : conv(clientejson['birth_day']),
                    'birth_month' : conv(clientejson['birth_month']),
                    'birth_year' : conv(clientejson['birth_year']),
                    'record_number' : conv(clientejson['record_number']),
                    'address' : conv(clientejson['address']),
                    'district' : conv(clientejson['district']),
                    'city' : conv(clientejson['city']),
                }
                clientedb, created = Clients.objects.update_or_create(agenda_id=clientejson["id"],defaults=cliente)
                
                pago = {
                    'agenda_id' : conv(paymentjson['id']),
                    'payment_date' : conv(paymentjson['payment_date']),
                    'agenda_location_id' : conv(paymentjson['location_id']),
                    'location_name' : conv(paymentjson['location_name']),
                    'amount' : conv(paymentjson['amount']),
                    'paid_amount' : conv(paymentjson['paid_amount']),
                    'change_amount' : conv(paymentjson['change_amount']),
                    'employee_code_id' : conv(paymentjson['employee_code_id']),
                    'employee_code_name' : conv(paymentjson['employee_code_name']),
                    'client' : clientedb,
                    
                }
                paymentdb, created = Payment.objects.update_or_create(agenda_id=paymentjson["id"],defaults=pago)

            # for paymentjson in response_json["payments"]:
            # productojson=paymentjson["products"]
            # if products in productojson:
            #     pprint('no existe')
            # else: 
            #     pprint(productojson)
                
                # producto = {
                #     'price' : conv(productodb['price']),
                #     'discount' : conv(productodb['discount']),
                #     'quantity' : conv(productodb['quantity']),
                #     'product' : conv(productodb['product']),
                #     'product_brand' : conv(productodb['product_brand']),
                #     'product_display' : conv(productodb['product_display']),
                #     'product_category' : conv(productodb['product_category']),
                #     'product_price' : conv(productodb['product_price']), 
                #     'agenda_id' : conv(productodb['id']), 
                #     'seller_details' : conv(productodb['seller_details']),
                    
                # }
                # productodb, created = Product.objects.update_or_create(agenda_id=productojson["id"],defaults=producto)

            # productodb, created = Product.objects.update_or_create(agenda_id=clientejson["id"],defaults=cliente)
            
            # for downpaymentjson in paymentjson["down_payment"]:
            #     for paymenttransactionsjson in downpaymentjson["payment_transactions"]:
            #         transacion = {
            #             'Payment' : paymentdb,
            #             'number' : conv(paymenttransactionsjson['number']),
            #             'amount' : conv(paymenttransactionsjson['amount']),
            #             'installments' : conv(paymenttransactionsjson['installments']),
            #             'payment_method' : conv(paymenttransactionsjson['payment_method']),
            #             'payment_method_type' : conv(paymenttransactionsjson['payment_method_type']),
            #             'bank' : conv(paymenttransactionsjson['bank']),
                        
            #         }
            #         transationdb, created = Transaction.objects.update_or_create(agenda_id=paymentjson["id"],defaults=transacion)
                    
                    
    return HttpResponse('<h1> Get data from agenda pro successfully <span>&#128512;</span> </h1>')


       
 


def test(request):
    cliente = Clients.objects.get(id=1)
    todoslosclientes = Clients.objects.all()
    print(todoslosclientes)
    pago = {
        'agenda_id' : '123344',
        'payment_date' : '12345678',
        'location_id' : '98765',
        'location_name' : '12345',
        'amount' : None,
        'paid_amount' : None,
        'change_amount' : None,
        'employee_code_id' : None,
        'employee_name' : None,
        'client' : cliente,
       
    }
    paymentsaved = Payment (**pago)
    
    paymentsaved.save()
    
    pagodos=Payment.objects.filter(id=1)
    pagodos=pagodos[0]
    print(pagodos)
    if(pagodos):
        print(pagodos)
        pagodos.delete()
    return HttpResponse('testing.....')
    