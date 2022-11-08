from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from apps.payments.models import Payment


# Register your models here.
from apps.products.models import Product
from django.contrib.auth.models import User


# class PaymentInline(admin.TabularInline):
#     model = Payment
#     can_delete = False
#     verbose_name_plural = 'payments'



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     list_display=["id",'product_price',"discount","price","quantity","product","product_brand","product_display",'product_category', 'agenda_receipt_id', 'seller_details']

class ProductInline(admin.TabularInline):
    # Product in-line 
    model = Product
    can_delete = False
    verbose_name_plural = 'productos'