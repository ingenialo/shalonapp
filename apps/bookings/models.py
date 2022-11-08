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
    
# nota: no se debe crear un modelo mockbooking por que ya se guardan los mock booking dentro de la tabla booking ver apps/payments/services.py linea 106
# class MockBooking (CustomBaseModel):
#     class Meta:
#         verbose_name = _('reserva_simulada')
#         verbose_name_plural = _('reservas_simuladas')
#     Payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, verbose_name=_('pago'))
#     price = models.IntegerField(blank=True,null=True, verbose_name=_('precio'))
#     discount = models.IntegerField(blank=True,null=True, verbose_name=_('descuento'))
#     service = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('servicio'))
#     provider = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('proveedor'))
#     Receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, null=True, verbose_name=_('recibo'))