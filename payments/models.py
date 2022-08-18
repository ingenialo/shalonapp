from django.db import models

from clients.models import Clients



class Payment(models.Model):

    # id = models.AutoField(auto_created=True)
    agenda_id = models.IntegerField(null=True, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    location_id = models.IntegerField(null=True)
    location_name = models.CharField(null=True, max_length=200)
    amount = models.IntegerField(null=True)
    paid_amount = models.IntegerField(null=True)
    change_amount = models.IntegerField(null=True)
    employee_code_id = models.IntegerField(null=True , blank=True)
    employee_name = models.CharField(max_length=200)
    client = models.ForeignKey('clients.Clients', on_delete=models.CASCADE)


class Payment_Transactions(models.Model):
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    number = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    installments = models.IntegerField(null=True)
    payment_method = models.CharField(max_length=200)
    payment_method_type = models.CharField(max_length=200)
    bank = models.CharField(max_length=200)