from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.db import models

# from bookings.admin import BookingInline
# from payments.admin import PaymentInline
# from clients.admin import ClientsInline

# Register your models here.
from django.contrib.auth.models import User
from apps.receipts.models import Receipt



@admin.register(Receipt)


# class ReceiptAdmin(admin.ModelAdmin):
#     inlines = [BookingInline]
    
# class ReceiptAdmin(admin.ModelAdmin):
#     inlines = [PaymentInline]

# class ReceiptAdmin(admin.ModelAdmin):
#     inlines = [ClientsInline]



class ReceiptAdmin(admin.ModelAdmin):


# Register your models here.
    list_display = (
        'id', 
        'agenda_id',
        'amount', 
        'date', 
        'number', 
        'receipt_type',
        'created_at',
        'updated_at'
        )
    
    
class ReceiptInline(admin.TabularInline):
    # Receipt in-line 
    model = Receipt
    can_delete = False
    verbose_name_plural = 'receipts'
    
    
    # list_display_links = ('pk')
    # list_editable = ('phone_number', 'website', 'picture')
    search_fields = []        
    list_filter = []