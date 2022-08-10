from django.contrib import admin

# Register your models here.
from receipts.models import Receipt



@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):


# Register your models here.
    list_display = (
        # 'id', 
        # 'amount', 
        'date', 
        'number', 
        'receipt_type',
        )
    # list_display_links = ('pk')
    # list_editable = ('phone_number', 'website', 'picture')
    search_fields = []        
    list_filter = []