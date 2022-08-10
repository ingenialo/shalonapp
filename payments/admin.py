from django.contrib import admin

# Register your models here.
from payments.models import Payment



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):


# Register your models here.
    list_display = (
        'pk', 
        'payment_date', 
        'location_id', 
        'location_name', 
        'amount', 
        'paid_amount',
        'change_amount',
        'employee_code_id',
        'employee_name',
        # 'client'
        )
    # list_display_links = ('pk')
    # list_editable = ('phone_number', 'website', 'picture')
    search_fields = []        
    list_filter = []
    
    
    
    
    
    
    # 
     
    
    
    
    