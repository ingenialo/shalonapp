from django.db import models

# from clients.models import Client


class Payments(models.Model):

    id = models.AutoField(auto_created=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    location_id = models.IntegerField()
    location_name = models.IntegerField()
    # amount = models.IntegerFieldField(required=True)
    # paid_amount = models.IntegerField()
    # change_amount = models.IntegerField()
    employee_code_id = models.IntegerField()
    employee_name = models.CharField()
    # client = [Client]
    
    
# Create your models here.
