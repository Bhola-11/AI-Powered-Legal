from django.contrib import admin
from .models import CourtOrder, ComplianceItem

@admin.register(CourtOrder)
class CourtOrderAdmin(admin.ModelAdmin):
    list_display = ['case', 'order_type', 'order_date', 'presiding_judge', 'requires_compliance']
    list_filter = ['order_type', 'requires_compliance', 'order_date']

@admin.register(ComplianceItem)
class ComplianceItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'responsible_party', 'deadline', 'is_complied']
