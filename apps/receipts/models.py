from django.db import models
from apps.payments.models import Payment
from config.utils.models import CustomBaseModel

class Receipt(CustomBaseModel):
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True,null=True)
    date = models.IntegerField(blank=True,null=True)
    number = models.IntegerField(blank=True,null=True)
    receipt_type = models.TextField(max_length=200, blank=True,null=True)

