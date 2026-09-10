from django.contrib import admin
from .models import LawFirm, BranchOffice, PracticeArea, FirmSetting

@admin.register(LawFirm)
class LawFirmAdmin(admin.ModelAdmin):
    list_display = ['name', 'registration_number', 'email', 'phone', 'is_active']
    search_fields = ['name', 'registration_number']

@admin.register(BranchOffice)
class BranchOfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'firm', 'city', 'state', 'is_headquarters']
    list_filter = ['is_headquarters', 'state']

@admin.register(PracticeArea)
class PracticeAreaAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(FirmSetting)
class FirmSettingAdmin(admin.ModelAdmin):
    list_display = ['firm', 'invoice_prefix', 'default_hourly_rate', 'tax_rate_percent']
