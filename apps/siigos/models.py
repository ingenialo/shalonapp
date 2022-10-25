from django.db import models
from config.utils.models import CustomBaseModel

from django.utils.translation import gettext_lazy as _

class DocumentType(CustomBaseModel):
    class Meta:
        verbose_name = _('metodo_de_pago_siigo')
        verbose_name_plural = _('metodo_de_pagos_siigo')
    siigo_id= models.IntegerField(blank=True,null=True, unique=True)
    name= models.CharField(max_length=100, blank=True,null=True)
    type= models.CharField(max_length=100, blank=True,null=True)
    active= models.BooleanField(null=True)
    due_date= models.DateTimeField(blank=True,null=True)
    