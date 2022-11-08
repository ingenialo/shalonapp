from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.db import models

from apps.bookings.models import Booking, MockBooking
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

@admin.register(MockBooking)
class MockBookingAdmin(admin.ModelAdmin):


# Register your models here.
    list_display = (
        'pk', 
        'price',
        'discount',
        'service',
        'provider',
        'Payment',
        'created_at',
        'updated_at'
        )

class BookingInline(admin.TabularInline):
    # Booking in-line 
    model = Booking
    can_delete = False
    verbose_name_plural = 'reservas'

class MockBookingInline(admin.TabularInline):
    # Booking in-line 
    model = MockBooking
    can_delete = False
    verbose_name_plural = 'reservas_simuladas'

