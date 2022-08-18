from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from pprint import pprint
from clients.models import Clients
from payments.models import Payment


# Create your views here.
def list_payments(request):
    # respuesta = ""
    
    # url = "https://api.github.com/users/jorgeeliecerpalacios"
    url = "https://agendapro.com/api/public/v1/payments"

    
    headers = {
    "Accept": "application/json",
    "Authorization": "Basic MWk4c3RicDY6dGd5ZWRqd3FtZjM0ejNwdGttNjM0bTJid2llM28zanBjZWhtbWI0Zg=="
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        
        paymentjson=response.json()["payments"][0]
        
        if (paymentjson):
            
            # cliente 
            clientejson = paymentjson["client"]
            clientedb = Clients.objects.filter(id_agenda=clientejson["id"]).first()
            if(not clientedb):
                clientdb = Clients(**clientejson)
                clientdb.save()
            print(clientdb)
            
            # payment
            paymentdb = Payment.objects.filter(id_agenda=clientejson["id"]).first()
            if(not paymentdb):
                paymentdb = Clients(**paymentjson)
                paymentdb.save()
    # for row in response:
    #     print(row)
        # clients = Clients(row)
        # print(clients)
        # clients.save()
        # print(clients.first_name)
    
    
    # client = Client(
    #     first_name = {response[8]},
    #     # last_name =  {response[1]},
    #     # email =  {response[1]},
    #     # identification_number =  {response[1]},
    #     # phone =  {response[1]},
    #     # second_phone =  {response[1]},
    #     # age =  {response[1]},
    #     # birth_day =  {response[1]},
    #     # birth_month =  {response[1]},
    #     # birth_year =  {response[1]},
    #     # record_number =  {response[1]},
    #     # address =  {response[1]},
    #     # district =  {response[1]},
    #     # city =  {response[1]},
    #     )
    # client.save()
    
    # print(response)
    # else:
    #     print('Error')

    
    
    # # Diccionario
   
   
    
    

    
    
    return HttpResponse('hola mundo')

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
        "pija":"megusta",
       
    }
    paymentpija = Payment (**pago)
    
    # paymentpija.save()
    
    pagodos=Payment.objects.filter(id=1)
    pagodos=pagodos[0]
    print(pagodos)
    # if(pagodos):
    #     print(pagodos)
    #     pagodos.delete()
    
    return HttpResponse('mkon')