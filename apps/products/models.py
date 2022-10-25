from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.payments.models import Payment
from apps.receipts.models import Receipt

# Create your models here.
from config.utils.models import CustomBaseModel




class Product(CustomBaseModel):
    class Meta:
        verbose_name = _('producto')
        verbose_name_plural = _('productos')
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, verbose_name=_('pago'))
    Receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, null=True, verbose_name=_('recibo'))
    price = models.IntegerField(blank=True,null=True, verbose_name=_('precio_con_descuento'))
    discount = models.IntegerField(blank=True,null=True, verbose_name=_('descuento'))
    quantity = models.IntegerField(blank=True,null=True, verbose_name=_('cantidad'))
    product = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('producto'))
    product_brand = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('marca'))
    product_display = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('producto nombre'))
    product_category = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('categoria'))
    product_price = models.IntegerField(blank=True,null=True, verbose_name=_('precio'))
    agenda_receipt_id = models.IntegerField(blank=True,null=True, verbose_name=_('recibo_id_agenda'))
    seller_details = models.CharField(max_length=200, blank=True,null=True, verbose_name=_('detalles_vendedor'))
    
    def __str__(self):
        return f'{self.product}'