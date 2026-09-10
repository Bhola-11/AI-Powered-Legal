from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['action', 'entity_name', 'actor', 'ip_address', 'created_at']
    list_filter = ['action', 'created_at']
    search_fields = ['description', 'entity_id', 'actor__username']
