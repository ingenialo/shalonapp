from datetime import datetime
from xmlrpc.client import _datetime
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
import requests
import json
from pprint import pprint



from apps.company.models import Company
from .models import DocumentType
from apps.payments.models import Payment
from apps.siigos.services import facturar_elctronica_by_payment_id

def generate_token():
    company = Company.objects.first()
    username = company.siigo_username
    access_key = company.siigo_access_key

    url = "https://api.siigo.com/auth"
    payload = {'username': username, 'access_key': access_key}
    headers = {'Accept': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)
    #pprint(response)
    if response.status_code == 200:
        response_json = response.json()
        access_token = response_json['access_token']
        #print(access_token)
        company.siigo_access_token = access_token
        company.save() 
        return access_token
    return None


def get_document_type(request):
    access_token = generate_token()
    company = Company.objects.first()
    url = f'{company.siigo_host}/payment-types?document_type=FV'
    headers = {
        'Accept': 'application/json',
        'Authorization': company.siigo_access_token
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()
        documents_types = response_json
        # pprint(documents_types)
        ids_db_ok = []
        for document_type in documents_types:
            
            documento ={
                "siigo_id": document_type['id'],
                "name": document_type['name'],
                "type": document_type['type'],
                "active": document_type['active'],
                "due_date": None,
            }
            pprint(documento)
            documentodb, created = DocumentType.objects.update_or_create(
                siigo_id=document_type['id'], 
                defaults=documento
            )
            ids_db_ok.append(documentodb.id)
        documentodbs_bad =DocumentType.objects.exclude(pk__in=ids_db_ok)
        documentodbs_bad.delete()
        #return JsonResponse(response_json, safe=False)
        return HttpResponseRedirect("/admin/siigos/documenttype/")
    else:
        return JsonResponse(response_json)


def get_customers(request):
    company = Company.objects.first()
    url = f'{company.siigo_host}/customers'
    headers = {
        'Accept': 'application/json',
        'Authorization': company.siigo_access_token
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()
    if response.status_code == 200:
        f = open("./apps/payments/salida2.json", "w")
        f.write(json.dumps(response_json))
        f.close()
        return JsonResponse(response_json)
    elif response.status_code==401:
        access_token = generate_token()
        return HttpResponse(f'<h1> se regenero el token <span>&#128512;</span> </h1> <p>{access_token}</p>')
    else:
        return JsonResponse(response_json)



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

def test_siigo_facturar(request):
    payments = Payment.objects.filter(facturado=False)
    for payment in payments:
        client = payment.client
        print(client)
    breakpoint()
    return HttpResponse('<h1> test_siigo_facturar <span>&#128512;</span> </h1>')

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




def facturar_electronica_payment(request, id_payment):
    generate_token()
    facturar_elctronica_by_payment_id(id_payment)
    return HttpResponse(f'<h1> facturado pago {id_payment} <span>&#128512;</span> </h1>')



