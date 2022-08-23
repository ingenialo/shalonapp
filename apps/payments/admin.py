from django.contrib import admin

# Register your models here.
from apps.payments.models import Payment
from apps.bookings.admin import BookingInline
from apps.receipts.admin import ReceiptInline
from apps.clients.admin import ClientsInline





@admin.register(Payment)



class PaymentAdmin(admin.ModelAdmin):
    inlines = [BookingInline,ReceiptInline, ]

# Register your models here.
    list_display = (
        'agenda_id', 
        'payment_date', 
        'location_name', 
        'client',
        'amount', 
        'paid_amount',
        )
    # list_display_links = ('pk')
    # list_editable = ('phone_number', 'website', 'picture')
    search_fields = []        
    list_filter = []
    ordering=["-payment_date"]
