from django.db import models

from apps.payments.models import Payment
from config.utils.models import CustomBaseModel
class Booking(CustomBaseModel):
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    web_origin = models.CharField(max_length=200, blank=True,null=True)
    provider_lock = models.CharField(max_length=200, blank=True,null=True)
    is_session_booked = models.BooleanField(blank=True, null=True)
    notes = models.CharField(max_length=200, help_text='Bienvenido(a) a Shalon Lash Brow , Por favor llegar 5 min antes.', blank=True,null=True)  #"Bienvenido(a) a Shalon Lash Brow , Por favor llegar 5 min antes."
    price = models.IntegerField(blank=True,null=True)
    discount = models.IntegerField(blank=True,null=True)
    service = models.CharField(max_length=200, blank=True,null=True)
    provider = models.CharField(max_length=200, blank=True,null=True)
    status = models.CharField(max_length=200, blank=True,null=True)
    receipt_id = models.IntegerField(blank=True,null=True)
    start = models.IntegerField(blank=True,null=True)
    end = models.IntegerField(blank=True,null=True)
    
