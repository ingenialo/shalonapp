from django.db import models

from apps.payments.models import Payment
from apps.receipts.models import Receipt
from config.utils.models import CustomBaseModel

from django.utils.translation import gettext_lazy as _
class Booking(CustomBaseModel):
    class Meta:
        verbose_name = _('reserva')
        verbose_name_plural = _('reservas')
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, verbose_name=_('pago'))
    Receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, null=True, verbose_name=_('recibo'))
    web_origin = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('web'))
    provider_lock = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('proveedor'))
    is_session = models.BooleanField(blank=True, null=True, verbose_name=_('es session'))
    is_session_booked = models.BooleanField(blank=True, null=True, verbose_name=_('es sesion reservada'))
    notes = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('notas'))
    price = models.IntegerField(blank=True,null=True, verbose_name=_('precio'))
    discount = models.IntegerField(blank=True,null=True, verbose_name=_('descuento'))
    service = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('servicio'))
    provider = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('proveedor'))
    status = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('estado'))
    agenda_receipt_id = models.IntegerField(blank=True,null=True, verbose_name=_('agenda'))
    start = models.DateTimeField(blank=True,null=True, verbose_name=_('inicio'))
    end = models.DateTimeField(blank=True,null=True, verbose_name=_('fin'))
    
# class MockBooking (CustomBaseModel):
     
#       price = models.IntegerField(blank=True,null=True)
#       discount = models.IntegerField(blank=True,null=True)
#       service = models.CharField(max_length=200, blank=True,null=True)
#       provider = models.CharField(max_length=200, blank=True,null=True)
#       agenda_id = models.IntegerField(blank=True,null=True, unique=True)
    
