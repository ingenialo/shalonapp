from django.db import models


class Client(models.Model):
    
    id = models.AutoField(auto_created=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    identification_number = models.CharField(blank=False, unique=True) 
    phone = models.CharField(unique=True, blank=False)
    second_phone = models.CharField(unique=True, blank=True)
    age = models.IntegerField(blank=True)
    birth_day = models.IntegerField(blank=True)
    birth_month = models.IntegerField(blank=True)
    birth_year = models.IntegerField(blank=True)
    record_number = models.IntegerField(blank=True)
    address = models.CharField(blank=False)
    district = models.CharField(blank=True)
    city = models.CharField(blank=True)
    

# Create your models here.
