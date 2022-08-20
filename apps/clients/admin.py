# Django
from django.contrib import admin

from apps.clients.models import Clients
from apps.payments.models import Payment
class PaymentInline(admin.TabularInline):
    model = Payment
    can_delete = False
    verbose_name_plural = 'payments'

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display=["id","agenda_id","email","first_name","last_name","identification_number",'created_at','updated_at']
    inlines = [PaymentInline]
  
  
class ClientsInline(admin.TabularInline):
    # Receipt in-line 
    model = Clients
    can_delete = False
    verbose_name_plural = 'clients'
# Register your models here.