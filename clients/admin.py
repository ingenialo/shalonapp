# Django
from django.contrib import admin

from clients.models import Clients



@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    pass 
    
  
# Register your models here.
