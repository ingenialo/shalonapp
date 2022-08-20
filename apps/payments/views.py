from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from pprint import pprint
from apps.clients.models import Clients
from apps.payments.models import Payment
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
            print("-----------------------------")
            clientejson=paymentjson["client"]
            clientedb = {}
            clientedb = Clients.objects.filter(agenda_id=clientejson["id"]).first()
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
            if(not clientedb):
                print("no existe el cliente")
                clientedb = Clients(**cliente)
            else:
                print("existe el cliente")
                clientedb = update_model(clientedb, save_update=False, **cliente)
            print(clientedb)
            clientedb.save()
            
    return HttpResponse('<h1> Get data from agenda pro successfully <span>&#128512;</span> </h1>')


 # paymentdb = Payment.objects.filter(agenda_id=clientejson["id"]).first()
        
        # if(not paymentdb):
        #     print("no hay cliente")
        #     print(clientejson['first_name'])
        #     pago = {
        #             'agenda_id' : clientejson['id'],
        #             'payment_date' : conv(clientejson['payment_date']),
        #             'location_id' : conv(clientejson['location_id']),
        #             'location_name' : clientejson['location_name'],
        #             'amount' : conv(clientejson['amount']),
        #             'paid_amount' : conv(clientejson['paid_amount']),
        #             'change_amount' : conv(clientejson['change_amount']),
        #             'employee_code_id' : conv(clientejson['employee_code_id']),
        #             'employee_name' : clientejson['employee_name'],
        #             'client' : clientedb,
                    
        #         }
                
        #     paymentdb = Payments(**pago)
        #     paymentdb.save()
        #     print(paymentdb)
 


def test(request):
    cliente = Clients.objects.get(id=1)
    todoslosclientes = Clients.objects.all()
    print(todoslosclientes)
    pago = {
        'agenda_id' : '123344',
        'payment_date' : '12345678',
        'location_id' : '98765',
        'location_name' : 'jpl',
        'amount' : None,
        'paid_amount' : None,
        'change_amount' : None,
        'employee_code_id' : None,
        'employee_name' : '',
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
    