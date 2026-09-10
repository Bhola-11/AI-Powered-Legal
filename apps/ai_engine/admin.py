from django.contrib import admin
from .models import AIQueryLog

@admin.register(AIQueryLog)
class AIQueryLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'query_type', 'latency_ms', 'created_at']
    list_filter = ['query_type', 'created_at']
