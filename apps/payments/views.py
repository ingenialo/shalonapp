# django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect

import datetime

from .services import getPaymentsFromAgendaPro, getPaymentFromAgendaPro



# Create your views here.


def getPaymentsByDate(request):
    if request.method == "POST":
        fecha = request.POST.get("date")
    else:
        fecha=""
    #print(fecha)
    if(fecha == ""):
        date = datetime.datetime.now()
        fecha = date.strftime('%y-%m-%d')
    
    try:
        getPaymentsFromAgendaPro(fecha)
        if request.method == "GET":
            return HttpResponse(f'<h1> Get data from {fecha} in agenda pro successfully <span>&#128512;</span> </h1>')

        if request.method == "POST":
            messages.success(request, f'los datos de {fecha} en Agenda Pro se trajeron satisfactoriamente :) ')
            return HttpResponseRedirect("/admin/payments/payment/")
    except Exception as e:
        print(e)
        if request.method == "GET":
            return HttpResponse(f'<h1> Get data from {fecha} in agenda pro failed <span>😔</span> </h1>')

        if request.method == "POST":
            messages.error(request, f'No se pudo traer los datos de {fecha} en Agenda Pro :( ')
            return HttpResponseRedirect("/admin/payments/payment/")
    
    
def get_payment(request, id_agenda_pro):

    try:
        getPaymentFromAgendaPro(id_agenda_pro)
        return HttpResponse('<h1> Get data from agenda pro successfully <span>&#128512;</span> </h1>')

    except Exception as e:
        return HttpResponse('<h1> Get data from agenda pro failed <span>😔</span> </h1>')
