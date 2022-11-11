from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.db import models

from apps.bookings.models import Booking
from django.contrib.auth.models import User



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):


# Register your models here.
    list_display = (
        'pk', 
        'Payment',
        'web_origin', 
        'is_session_booked', 
        'agenda_receipt_id', 
        'notes', 
        'provider_lock',
        'price',
        'discount',
        'service',
        'provider',
        # 'add',
        'status',
        'start',
        'end',
        'created_at',
        'updated_at'
        )

class BookingInline(admin.TabularInline):
    # Booking in-line 
    model = Booking
    can_delete = True
    verbose_name_plural = 'reservas'
