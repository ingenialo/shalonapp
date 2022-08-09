from django.contrib import admin

from bookings.models import Bookings



@admin.register(Bookings)
class BookingAdmin(admin.ModelAdmin):


# Register your models here.
    list_display = (
        'pk', 
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
    # list_display_links = ('pk')
    # list_editable = ('phone_number', 'website', 'picture')
    search_fields = []        
    list_filter = []
    
    
    
      
    
    
    
    
     
    
   
    
    
    
     
    
    