from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class ClientType(models.TextChoices):
    INDIVIDUAL = 'INDIVIDUAL', 'Individual Person'
    CORPORATE = 'CORPORATE', 'Corporate Enterprise'
    GOVERNMENT = 'GOVERNMENT', 'Government Entity'
    NGO = 'NGO', 'Non-Profit Organization'

class ClientProfile(UUIDModel, AuditTrackedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_profile', null=True, blank=True)
    client_type = models.CharField(max_length=20, choices=ClientType.choices, default=ClientType.INDIVIDUAL)
    display_name = models.CharField(max_length=255, db_index=True)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    tax_id_or_pan = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    billing_address = models.TextField()
    is_verified = models.BooleanField(default=False)
    conflict_check_cleared = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.display_name

class KYCVerification(AuditTrackedModel):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='kyc_records')
    document_type = models.CharField(max_length=100, help_text="Passport, National ID, Certificate of Incorporation")
    document_number = models.CharField(max_length=100)
    verified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='PENDING', choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')])
    remarks = models.TextField(blank=True, null=True)

class ConflictCheckResult(AuditTrackedModel):
    client_name = models.CharField(max_length=255)
    adverse_party_searched = models.CharField(max_length=255)
    is_conflict_found = models.BooleanField(default=False)
    conflict_details = models.TextField(blank=True, null=True)
    cleared_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    cleared_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Conflict Check: {self.client_name} vs {self.adverse_party_searched}"
