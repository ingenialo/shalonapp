from django.db import models
from apps.payments.models import Payment
from config.utils.models import CustomBaseModel

class Receipt(CustomBaseModel):
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    agenda_id = models.IntegerField(blank=True,null=True, unique=True)
    amount = models.IntegerField(blank=True,null=True)
    date = models.DateTimeField(blank=True,null=True)
    number = models.CharField(blank=True,null=True, max_length=200)
    receipt_type = models.TextField(max_length=200, blank=True,null=True)

