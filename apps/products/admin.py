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
     list_display=["price","discount","quantity","product","product_brand","product_display",'product_category','product_price', 'agenda_id', 'seller_details']
    #  inlines = [PaymentInline]


# Register your models here.


class ProductInline(admin.TabularInline):
    # Product in-line 
    model = Product
    can_delete = False
    verbose_name_plural = 'products'