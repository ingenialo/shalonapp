from django.db import models
from config.utils.models import CustomBaseModel
from django.utils.translation import gettext_lazy as _

class Company(CustomBaseModel):
    class Meta:
        verbose_name = _('empresa')
        verbose_name_plural = _('empresas')

    nombre = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    nit = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono_a = models.CharField(max_length=50, blank=True, null=True)
    telefono_b = models.CharField(max_length=50, blank=True, null=True)
    telefono_c = models.CharField(max_length=50, blank=True, null=True)
    sitioweb = models.URLField(blank=True, null=True)
    mail = models.EmailField(blank=True, null=True)
    slogan = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=100, unique=True, default='principal',editable=False)
    agenda_pro_token = models.CharField(max_length=200)
    siigo_username = models.CharField(max_length=100)
    siigo_access_key = models.CharField(max_length=200)
    siigo_access_token = models.CharField(max_length=2000)
    agenda_pro_host=models.CharField(max_length=100, null=True)
    siigo_host=models.CharField(max_length=100, null=True)

