from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.db import models

from bookings.models import Booking
from django.contrib.auth.models import User



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):


# Register your models here.
    list_display = (
        'pk', 
        'Payment',
        'web_origin', 
        'is_session_booked', 
        'receipt_id', 
        'notes', 
        'provider_lock',
        'price',
        'discount',
        'service',
        'provider',
        # 'add',
        'status',
        'start',
        'end'
        )

class BookingInline(admin.TabularInline):
    # Booking in-line 
    model = Booking
    can_delete = False
    verbose_name_plural = 'bookings'