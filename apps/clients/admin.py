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
    list_display=["id","agenda_id","email","cliente", "document_type", "identification_number","siigo",'created_at','updated_at']
    search_fields = ["first_name"]
    #list_filter = ['identification_number']
    inlines = [PaymentInline]
    def cliente(self, obj):
        tipo_client = "✅" if not obj.consumidor_final else "❌"
        return f'{tipo_client} {obj.first_name} {obj.last_name}'
  
  
class ClientsInline(admin.TabularInline):
    # Receipt in-line 
    model = Clients
    can_delete = False
    verbose_name_plural = 'clients'
# Register your models here.
