from django.contrib import admin
from .models import AnalyticsSnapshot

@admin.register(AnalyticsSnapshot)
class AnalyticsSnapshotAdmin(admin.ModelAdmin):
    list_display = ['snapshot_date', 'total_active_cases', 'total_disposed_cases', 'total_revenue_billed']
