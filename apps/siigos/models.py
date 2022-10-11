from django.db import models
from config.utils.models import CustomBaseModel

class DocumentType(CustomBaseModel):
    siigo_id= models.IntegerField(blank=True,null=True, unique=True)
    name= models.CharField(max_length=100, blank=True,null=True)
    type= models.CharField(max_length=100, blank=True,null=True)
    active= models.BooleanField(null=True)
    due_date= models.DateTimeField(blank=True,null=True)
    