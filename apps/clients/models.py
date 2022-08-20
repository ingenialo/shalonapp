from django.db import models


class Clients(models.Model):
    
    agenda_id = models.IntegerField(null=True, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    identification_number = models.CharField(max_length=200 ,blank=False, unique=True) 
    phone = models.CharField(max_length=200, blank=False)
    second_phone = models.CharField(max_length=200 ,unique=True, blank=True,null=True)
    age = models.IntegerField(blank=True, null=True,default=None)
    birth_day = models.IntegerField(blank=True, null=True,default=None)
    birth_month = models.IntegerField(blank=True, null=True,default=None)
    birth_year = models.IntegerField(blank=True, null=True,default=None)
    record_number = models.IntegerField(blank=True, null=True,default=None)
    address = models.CharField(max_length=200 ,blank=False)
    district = models.CharField(max_length=200 ,blank=True)
    city = models.CharField(max_length=200 ,blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Create your models here.
