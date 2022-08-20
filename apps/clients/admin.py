# Django
from django.contrib import admin

from apps.clients.models import Clients



@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display=["id","agenda_id","email","first_name","last_name","identification_number"]
    
  
  
class ClientsInline(admin.TabularInline):
    # Receipt in-line 
    model = Clients
    can_delete = False
    verbose_name_plural = 'clients'
# Register your models here.
