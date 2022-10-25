from django.contrib import admin
from .models import DocumentType

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = (
            'id',
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
    change_list_template = "siigos/admin/snippets_change_list_DocumentTypeAdmin.html"
