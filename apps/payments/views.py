# django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect

import datetime

from .services import getPaymentsFromAgendaPro



# Create your views here.


def list_payments(request):
    fecha = request.POST.get("date")
    if(fecha == ""):
        date = datetime.datetime.now()
        fecha = date.strftime('%y-%m-%d')
    
    try:
        getPaymentsFromAgendaPro(fecha)
        if request.method == "GET":
            return HttpResponse('<h1> Get data from agenda pro successfully <span>&#128512;</span> </h1>')

        if request.method == "POST":
            messages.success(request, 'los datos de Agenda Pro se trajeron satisfactoriamente :) ')
            return HttpResponseRedirect("/admin/payments/payment/")
    except:
        if request.method == "GET":
            return HttpResponse('<h1> Get data from agenda pro failed <span>😔</span> </h1>')

        if request.method == "POST":
            messages.error(request, 'No se pudo traer los datos de Agenda Pro :( ')
            return HttpResponseRedirect("/admin/payments/payment/")
    
    

