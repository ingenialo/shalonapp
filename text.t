import request 


# if __name__=='__main__':
#     url:'https://app.agendapro.com/company_settings/integration'

#     session = request.session()
#     session.auth = ('1i8stbp6', 'tgyedjwqmf34z3ptkm634m2bwie3o3jpcehmmb4f')

#     response = session.get(url)
#     if response.ok:
#         print(response.content)





{
    'active': True,
    'address': {'address': 'CLL 1 B 55 25',
                'city': {'city_code': '76001',
                        'city_name': 'Cali',
                        'country_code': 'Co',
                        'country_name': 'Colombia',
                        'state_code': '76',
                        'state_name': 'Valle del Cauca'},
                'postal_code': ''},
    'branch_office': 0,
    'check_digit': '',
    'contacts': [{'email': 'manuelayanguass14@gmail.com',
                'first_name': 'MANUELA',
                'last_name': 'YANGUAS RUIZ',
                'phone': {'number': '3502026662'}}],
    'fiscal_responsibilities': [{'code': 'R-99-PN', 'name': 'No aplica - Otros'}],
    'id': '97e9e726-276f-47da-9d04-2054ef4f1be1',
    'id_type': {'code': '13', 'name': 'Cédula de ciudadanía'},
    'identification': '1112044130',
    'metadata': {'created': '2022-08-25T14:36:21.617',
                'last_updated': '2022-08-25T14:37:04.517'},
    'name': ['MANUELA', 'YANGUAS RUIZ'],
    'person_type': 'Person',
    'phones': [{'number': '3502026662'}],
    'type': 'Customer',
    'vat_responsible': False
    }


























"payments": [
    {
      "id": 12441625,
      "payment_date": "2022-07-27T12:42:00.000Z",
      "location_id": 3292,
      "location_name": "SHALON SEDE AVENTURA PLAZA",
      "amount": 25000,
      "paid_amount": 25000,
      "change_amount": 0,
      "employee_code_id": null,
      "employee_code_name": "",
      "client": 
      {
        "id": 2751378,
        "first_name": "CATALINA",
        "last_name": "ARAMBULO",
        "email": "cataaramburo@hotmail.com",
        "identification_number": "29.178.442",
        "phone": "+57 312 2059142",
        "second_phone": "",
        "age": null,
        "birth_day": 7,
        "birth_month": 12,
        "birth_year": null,
        "record_number": "",
        "address": "VIA  CALI JAMUNDI ELCASTILLO CONJUNTO ROBLES CASA 164",
        "district": "",
        "city": ""
      },
      "bookings": 
      [
        {
          "web_origin": false,
          "provider_lock": false,
          "is_session": false,
          "is_session_booked": false,
          "notes": "Bienvenido(a) a Shalon Lash Brow , Por favor llegar 5 min antes.",
          "price": 25000,
          "discount": 0,
          "service": "RETOQUE CEJAS 14 a 20 DIAS",
          "provider": " ELIANA G.",
          "status": "Asiste",
          "receipt_id": 12804286,
          "start": "2022-07-27T12:30:00.000Z",
          "end": "2022-07-27T13:00:00.000Z"
        }
      ],
      "products": 
      [
      ],
      "mock_bookings": 
      [
      ],
      "memberships": 
      [
      ],
      "giftcards": 
      [
      ],
      "down_payment": 
      [
        {
            "payment_transactions":
            [
                 {
              "number": "",
              "amount": 25000,
              "installments": 0,
              "payment_method": "Efectivo",
              "payment_method_type": "",
              "bank": ""
                 }
            ]
        }
      ],
      "receipts": 
      [
        {
          "id": 12804286,
          "amount": 25000,
          "date": "2022-07-27",
          "number": "60540",
          "receipt_type": "Factura"
        }
      ]
    },  ]

"receipts": [{
      "id": 13321249,
      "amount": 25000.0,
      "date": "2022-08-20",
      "number": "26261",
      "receipt_type": "Factura"
    }]


    "mock_bookings": [{
      "price": 10000.0,
      "discount": 33.33333333333334,
      "service": "DEPILACION MICRO",
      "provider": "T. YERALDIN CORTES",
      "receipt_id": 13320431
    }]