from django.db import models

from config.utils.models import CustomBaseModel

class Payment(CustomBaseModel):

    # id = models.AutoField(auto_created=True)
    agenda_id = models.IntegerField(blank=True,null=True, unique=True)
    payment_date = models.DateTimeField(blank=True,null=True)
    location_id = models.IntegerField(blank=True,null=True)
    location_name = models.CharField(max_length=200, blank=True,null=True)
    amount = models.IntegerField(blank=True,null=True)
    paid_amount = models.IntegerField(blank=True,null=True)
    change_amount = models.IntegerField(blank=True,null=True)
    employee_code_id = models.IntegerField(blank=True,null=True)
    employee_code_name = models.CharField(max_length=200, blank=True,null=True)
    client = models.ForeignKey('clients.Clients', on_delete=models.CASCADE)


class Payment_Transactions(models.Model):
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    number = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    installments = models.IntegerField(null=True)
    payment_method = models.CharField(max_length=200)
    payment_method_type = models.CharField(max_length=200)
    bank = models.CharField(max_length=200)