from django.contrib import admin

# Register your models here.
from apps.payments.models import Payment
from apps.bookings.admin import BookingInline
from apps.receipts.admin import ReceiptInline
from apps.clients.admin import ClientsInline




@admin.register(Payment)



class PaymentAdmin(admin.ModelAdmin):
    inlines = [BookingInline]
    
class PaymentAdmin(admin.ModelAdmin):
    inlines = [ReceiptInline]

class PaymentAdmin(admin.ModelAdmin):
    inlines = [ClientsInline]


# Register your models here.
    list_display = (
        # 'pk', 
        'payment_date', 
        'location_id', 
        'location_name', 
        'amount', 
        'paid_amount',
        'change_amount',
        'employee_code_id',
        'employee_name',
        'client'
        )
    # list_display_links = ('pk')
    # list_editable = ('phone_number', 'website', 'picture')
    search_fields = []        
    list_filter = []
class PaymentInline(admin.TabularInline):
    # Receipt in-line 
    model = Payment
    can_delete = False
    verbose_name_plural = 'payments'