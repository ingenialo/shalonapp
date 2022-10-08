from django.db import models
from config.utils.models import CustomBaseModel

class Clients(CustomBaseModel):
    
    agenda_id = models.IntegerField(blank=True,null=True, unique=True)
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    document_type = models.CharField(max_length=100, blank=True,null=True) 
    identification_number = models.CharField(max_length=200, unique=True, blank=True,null=True) 
    phone = models.CharField(max_length=200, blank=True,null=True)
    second_phone = models.CharField(max_length=200, blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    birth_day = models.IntegerField(blank=True,null=True)
    birth_month = models.IntegerField(blank=True,null=True)
    birth_year = models.IntegerField(blank=True,null=True)
    record_number = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=200 ,blank=True,null=True)
    district = models.CharField(max_length=200, blank=True,null=True)
    city = models.CharField(max_length=200 ,blank=True,null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Create your models here.
