from django.db import models

# Create your models here.

class Receipt(models.Model):

    id = models
    # amount = models.ForeignKey('')
    date = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(null=True)
    receipt_type = models.TextField(max_length=200)

