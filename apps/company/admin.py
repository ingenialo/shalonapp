from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
            'nombre',
            'razon_social',
            'nit',
            'ciudad',
            'direccion',
            'telefono_a',
            'telefono_b',
            'telefono_c',
            'sitioweb',
            'mail',
            'slogan',
            'status',
            'created_at',
            'updated_at',
        )
    search_fields = []
    list_filter = []
