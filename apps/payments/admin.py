from django.contrib import admin

# Register your models here.
from apps.payments.models import Payment, Transaction
from apps.bookings.admin import BookingInline
from apps.receipts.admin import ReceiptInline
from apps.clients.admin import ClientsInline
from apps.products.admin import ProductInline



class TransactionInline(admin.TabularInline):
    # Product in-line 
    model = Transaction
    can_delete = False
    verbose_name_plural = 'transactions'

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
    inlines = [BookingInline, ProductInline, ReceiptInline, TransactionInline]
    list_display = (
        'agenda_id', 
        'payment_date', 
        'location_name', 
        'client',
        'amount', 
        'paid_amount',
        'facturado',
        'errores',
        )
    # list_display_links = ('pk')
    # list_editable = ('phone_number', 'website', 'picture')
    search_fields = []        
    list_filter = ['location_name','facturado']
    ordering=["-payment_date"]
