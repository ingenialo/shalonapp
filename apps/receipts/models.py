from django.db import models
from apps.payments.models import Payment
from config.utils.models import CustomBaseModel

class Receipt(CustomBaseModel):
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(null=True)
    receipt_type = models.TextField(max_length=200)

