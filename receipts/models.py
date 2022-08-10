from django.db import models

# Create your models here.

class Receipt(models.Model):

    id = models
    amount = models.ManyToManyField('')
    date = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField()
    receipt_type = models.TextField()
