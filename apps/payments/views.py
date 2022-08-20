from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from pprint import pprint
from apps.clients.models import Clients
from apps.payments.models import Payment
# from apps.clients.serializer import ClientSerializer

def conv(value):
    if value:
        print("retorno el valor")
        return value
    else:
        print("seria none")
        return None

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
        for paymentjson in response.json()["payments"]:
            clientejson=paymentjson["client"]
            clientedb = Clients.objects.filter(identification_number=clientejson["identification_number"]).first()
            if(not clientedb):
                print("no hay cliente")
                print(clientejson['first_name'])
                cliente = {
                            'agenda_id' : clientejson['id'],
                            'first_name' : clientejson['first_name'],
                            'last_name' : clientejson['last_name'] ,
                            'email' : clientejson['email'] ,
                            'identification_number' : clientejson['identification_number']  ,
                            'phone' : clientejson['phone'] ,
                            'second_phone' : conv(clientejson['second_phone']),
                            'age' : conv(clientejson['age']),
                            'birth_day' : conv(clientejson['birth_day']),
                            'birth_month' : conv(clientejson['birth_month']),
                            'birth_year' : conv(clientejson['birth_year']),
                            'record_number' : conv(clientejson['record_number']),
                            'address' : clientejson['address'],
                            'district' : clientejson['district'],
                            'city' : clientejson['city'],
                        }
                print(cliente)
                clientdb = Clients(**cliente)
                clientdb.save()
                print(clientdb)
            
        
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
        #             'client' : clientdb,
                    
        #         }
                
        #     paymentdb = Payments(**pago)
        #     paymentdb.save()
        #     print(paymentdb)
    
    
    # cliente = Clients.objects.get(pk=1)
    # # todoslosclientes = Clients.objects.all()
    # print(todoslosclientes)
     
     
     
     
     
     
     
     

    # if response.status_code == 200:
        
    #     paymentjson=response.json()["payments"][0]["client"]
        
    #     if (paymentjson):
            
    #         # cliente 
          
                    
    #         clientejson = paymentjson["client"]
    #         clientedb = Clients.objects.filter(agenda_id=clientejson["id"]).first()
    #         if(not clientedb):
    #             clientdb = Clients(
                    
    #                 client = {
    #                     'agenda_id' : '',
    #                     'first_name' : '',
    #                     'last_name' : '' ,
    #                     'email' : '' ,
    #                     'identification_number' : '' ,
    #                     'phone' : '',
    #                     'second_phone' : None,
    #                     'age' : None,
    #                     'birth_day' : None,
    #                     'birth_month' : None,
    #                     'birth_year' : None,
    #                     'record_number' : '',
    #                     'address' : '',
    #                     'district' : '',
    #                     'city' : '',
    #                 }
                    
    #             )
    #             clientdb.save()
    #             print(clientdb)
            
    #         # payment
    #         paymentdb = Payment.objects.filter(agenda_id=clientejson["id"]).first()
    #         if(not paymentdb):
    #             paymentdb = Payment(
               
    #                 pago = {
    #                     'agenda_id' : '',
    #                     'payment_date' : '',
    #                     'location_id' : '',
    #                     'location_name' : '',
    #                     'amount' : None,
    #                     'paid_amount' : None,
    #                     'change_amount' : None,
    #                     'employee_code_id' : None,
    #                     'employee_name' : '',
    #                     'client' : clientdb,
                    
    #             }
    #             )
                
    #             paymentdb.save()
    #             print(paymentdb)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
    
    
    #     else:
    # print('Error')

    
    
    # # Diccionario
   
   
    
    

    
    
    return HttpResponse('hola mundo')































def test(request):
#     cliente = Clients.objects.get(id=1)
#     todoslosclientes = Clients.objects.all()
#     print(todoslosclientes)
#     pago = {
#         'agenda_id' : '123344',
#         'payment_date' : '12345678',
#         'location_id' : '98765',
#         'location_name' : 'jpl',
#         'amount' : None,
#         'paid_amount' : None,
#         'change_amount' : None,
#         'employee_code_id' : None,
#         'employee_name' : '',
#         'client' : cliente,
#         "pija":"megusta",
       
#     }
#     paymentpija = Payment (**pago)
    
#     paymentpija.save()
    
#     pagodos=Payment.objects.filter(id=1)
#     pagodos=pagodos[0]
#     print(pagodos)
#     # if(pagodos):
#     #     print(pagodos)
#     #     pagodos.delete()
    
    return HttpResponse('mkon')