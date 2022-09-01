from django.contrib import admin
from .models import DocumentType

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = (
            'siigo_id',
            'name',
            'type',
            'active',
            'due_date',
            'created_at',
            'updated_at',
        )
    search_fields = []
    list_filter = []
