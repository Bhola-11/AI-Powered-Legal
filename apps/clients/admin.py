from django.contrib import admin
from .models import ClientProfile, KYCVerification, ConflictCheckResult

@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'client_type', 'email', 'phone', 'is_verified', 'conflict_check_cleared']
    search_fields = ['display_name', 'email', 'tax_id_or_pan']
    list_filter = ['client_type', 'is_verified', 'conflict_check_cleared']

@admin.register(KYCVerification)
class KYCVerificationAdmin(admin.ModelAdmin):
    list_display = ['client', 'document_type', 'document_number', 'status', 'verified_at']

@admin.register(ConflictCheckResult)
class ConflictCheckResultAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'adverse_party_searched', 'is_conflict_found', 'cleared_at']
