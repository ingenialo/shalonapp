from django.db import models

from clients.models import Clients


class Payments(models.Model):

    # id = models.AutoField(auto_created=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    location_id = models.IntegerField(null=True)
    location_name = models.IntegerField(null=True)
    # amount = models.IntegerFieldField(required=True)
    paid_amount = models.IntegerField(null=True)
    change_amount = models.IntegerField(null=True)
    employee_code_id = models.IntegerField(null=True , blank=True)
    employee_name = models.CharField(max_length=200)
    client = [Clients]
