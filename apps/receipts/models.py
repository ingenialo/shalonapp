from django.db import models
from payments.models import Payment

# Create your models here.

class Receipt(models.Model):

    id = models
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(null=True)
    receipt_type = models.TextField(max_length=200)

