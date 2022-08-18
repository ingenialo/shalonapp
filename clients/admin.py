# Django
from django.contrib import admin

from clients.models import Clients



@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display=["id","email"]
    
  
  
class ClientsInline(admin.TabularInline):
    # Receipt in-line 
    model = Clients
    can_delete = False
    verbose_name_plural = 'clients'
# Register your models here.
