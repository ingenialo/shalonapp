from django.db import models
from config.utils.models import CustomBaseModel

from django.utils.translation import gettext_lazy as _

class Clients(CustomBaseModel):
    class Meta:
        verbose_name = _('cliente')
        verbose_name_plural = _('clientes')
    agenda_id = models.IntegerField(blank=True,null=True, unique=True,)
    first_name = models.CharField(max_length=200,blank=True,null=True, verbose_name=_('nombres'))
    last_name = models.CharField(max_length=200,blank=True,null=True, verbose_name=_('apellidos'))
    email = models.EmailField(blank=True,null=True, verbose_name=_('correo'))
    document_type = models.CharField(max_length=100, blank=True,null=True, verbose_name=_('tipo_docto')) 
    identification_number = models.CharField(max_length=200, unique=True, blank=True,null=True, verbose_name=_('documento')) 
    phone = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('telefono'))
    second_phone = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('telefono_dos'))
    age = models.IntegerField(blank=True,null=True, verbose_name=_('edad'))
    birth_day = models.IntegerField(blank=True,null=True, verbose_name=_('dia_nacimiento'))
    birth_month = models.IntegerField(blank=True,null=True, verbose_name=_('mes_nacimiento'))
    birth_year = models.IntegerField(blank=True,null=True, verbose_name=_('ano_nacimiento'))
    record_number = models.IntegerField(blank=True,null=True, verbose_name=_('numero_registro'))
    address = models.CharField(max_length=200 ,blank=True,null=True, verbose_name=_('direccion'))
    district = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('distrito'))
    city = models.CharField(max_length=200 ,blank=True,null=True, verbose_name=_('ciudad'))
    siigo = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Create your models here.
