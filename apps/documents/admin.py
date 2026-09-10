from django.contrib import admin
from .models import DocumentCategory, LegalDocument, DocumentVersion

@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'case', 'category', 'current_version', 'is_client_visible', 'is_confidential']
    list_filter = ['category', 'is_client_visible', 'is_confidential']
    search_fields = ['title', 'file_sha256']

@admin.register(DocumentVersion)
class DocumentVersionAdmin(admin.ModelAdmin):
    list_display = ['document', 'version_number', 'file_sha256']
