from django.db import models
from apps.payments.models import Payment


# Create your models here.
from config.utils.models import CustomBaseModel




class Product(CustomBaseModel):
    Payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(blank=True,null=True)
    discount = models.IntegerField(blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    product = models.CharField(max_length=200, blank=True,null=True)
    product_brand = models.CharField(max_length=200, blank=True,null=True)
    product_display = models.CharField(max_length=200, blank=True,null=True)
    product_category = models.CharField(max_length=200, blank=True,null=True)
    product_price = models.IntegerField(blank=True,null=True)
    agenda_id = models.IntegerField(blank=True,null=True, unique=True)
    seller_details = models.CharField(max_length=200, blank=True,null=True)
    