from django.contrib import admin

from django.contrib import messages
from django.http import HttpResponseRedirect

from apps.siigos.views import generate_token
from apps.siigos.services import facturar_elctronica_by_payment_id

from apps.payments.models import Payment, Transaction
from apps.bookings.admin import BookingInline
from apps.receipts.admin import ReceiptInline
from apps.clients.admin import ClientsInline
from apps.products.admin import ProductInline

from apps.payments.services import getPaymentFromAgendaPro



class TransactionInline(admin.TabularInline):
    # Product in-line 
    model = Transaction
    can_delete = True
    verbose_name_plural = 'transacciones'

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'Payment',
            'ticker_number',
            'amount',
            'installments',
            'payment_method',
            'payment_method_type',
            'bank',
        )
    search_fields = []
    list_filter = []
    ordering=["-Payment"]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    inlines = [BookingInline, ProductInline, TransactionInline, ReceiptInline]
    list_display = (
        'id',
        'agenda_id', 
        'payment_date', 
        'location_name', 
        'cliente',
        'amount', 
        'facturado',
        "factura",
        'facturable_electronica',
        'errores',
        )
    # list_display_links = ('pk')
    # list_editable = ('phone_number', 'website', 'picture')
    # search_fields = ["client"]
    list_filter = ['location_name','facturado','facturable_electronica','payment_date']
    date_hierarchy = 'payment_date'
    ordering=["-payment_date"]
    actions = ['facturar', 'actualizar_con_agenda_pro']
    save_on_top = True
    change_list_template = "payments/admin/snippets_change_list.html"

    def cliente(self, obj):
        tipo_client = "✅" if not obj.client.consumidor_final else "❌"
        return f'{tipo_client} {obj.client.first_name} {obj.client.last_name}'
    
    def factura(self, obj):
        return obj.comprobante_siigo

    def actualizar_con_agenda_pro(self, request, queryset):
        for payment in queryset:
            # print("-------------------")
            try:
                if payment.facturado == False:
                    getPaymentFromAgendaPro(payment.agenda_id)
            except Exception as e:
                print(e)
                messages.error(request, f'No se pudo traer los datos de id {payment.id} en Agenda Pro :( ')
                return HttpResponseRedirect("/admin/payments/payment/")
        messages.success(request,'los datos de en Agenda Pro se trajeron satisfactoriamente :) ')
        return HttpResponseRedirect("/admin/payments/payment/")
    
    def facturar(self, request, queryset):
        generate_token()
        count = 0
        count_good = 0
        count_bad = 0
        for payment in queryset:
            count += 1
            result = facturar_elctronica_by_payment_id(payment.id)
            if(result):
                count_good+=1 
            else:
                count_bad+=1
        mensaje = f'intentos: {count}, satisfactorios: {count_good}, fallidos: {count_bad}'
        if(count_good):
            messages.success(request, f'{mensaje} :) ')
        else:
            messages.error(request, f'{mensaje} :( ')
