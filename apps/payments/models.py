from django.db import models
from django.utils.translation import gettext_lazy as _

from config.utils.models import CustomBaseModel

class Payment(CustomBaseModel):
    class Meta:
        verbose_name = _('pago')
        verbose_name_plural = _('pagos')

    # id = models.AutoField(auto_created=True)
    agenda_id = models.IntegerField(blank=True,null=True, unique=True)
    payment_date = models.DateTimeField(blank=True,null=True, verbose_name=_('fecha_pago'))
    agenda_location_id = models.IntegerField(blank=True,null=True,)
    location_name = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('ubicacion'))
    amount = models.IntegerField(blank=True,null=True, verbose_name=_('cantidad'))
    paid_amount = models.IntegerField(blank=True,null=True, verbose_name=_('cantidad pagada'))
    change_amount = models.IntegerField(blank=True,null=True, verbose_name=_('cantidad cambio'))
    employee_code_id = models.IntegerField(blank=True,null=True, verbose_name=_('codigo empleado'))
    employee_code_name = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('empleado codigo_nombre'))
    client = models.ForeignKey('clients.Clients', on_delete=models.CASCADE)
    facturado = models.BooleanField(default=False)
    errores = models.CharField(max_length=2000, blank=True,null=True)
    def __str__(self):
        return f'{self.id}'
   


class Transaction(CustomBaseModel):
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True,null=True)
    amount = models.IntegerField(blank=True,null=True)
    installments = models.IntegerField(blank=True,null=True)
    payment_method = models.CharField(max_length=200)
    payment_method_type = models.CharField(max_length=200, blank=True,null=True)
    bank = models.CharField(max_length=200, blank=True,null=True)

    def __str__(self):
        return f'{self.id}'