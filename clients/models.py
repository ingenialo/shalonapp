from django.db import models


class Clients(models.Model):
    
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    identification_number = models.CharField(max_length=200 ,blank=False, unique=True) 
    phone = models.CharField(max_length=200 ,unique=True, blank=False)
    second_phone = models.CharField(max_length=200 ,unique=True, blank=True)
    age = models.IntegerField(blank=True)
    birth_day = models.IntegerField(blank=True)
    birth_month = models.IntegerField(blank=True)
    birth_year = models.IntegerField(blank=True)
    record_number = models.IntegerField(blank=True)
    address = models.CharField(max_length=200 ,blank=False)
    district = models.CharField(max_length=200 ,blank=True)
    city = models.CharField(max_length=200 ,blank=True)
    

# Create your models here.
