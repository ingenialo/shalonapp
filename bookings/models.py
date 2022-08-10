from django.db import models

from payments.models import Payment



class Booking(models.Model):
    
    # payment = models.ForeignKey('clients.Clients', on_delete=models.CASCADE)
    
    
    web_origin = models.CharField(max_length=200, blank=True, null=True)
    provider_lock = models.CharField(max_length=200, blank=True , null=True)
    is_session_booked = models.BooleanField(blank=True, null=True)
    notes = models.CharField(max_length=200, help_text='Bienvenido(a) a Shalon Lash Brow , Por favor llegar 5 min antes.')  #"Bienvenido(a) a Shalon Lash Brow , Por favor llegar 5 min antes."
    price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    service = models.CharField(max_length=200)
    provider = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    receipt_id = models.IntegerField(null=True)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now=True)
    
