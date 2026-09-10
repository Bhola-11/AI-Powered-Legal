from django.db import models
from apps.core.models import AuditTrackedModel, UUIDModel

class LawFirm(UUIDModel, AuditTrackedModel):
    name = models.CharField(max_length=255, unique=True)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    tax_id = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    website = models.URLField(blank=True, null=True)
    primary_office_address = models.TextField()
    is_active = models.BooleanField(default=True)
    max_lawyers = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.name

class BranchOffice(AuditTrackedModel):
    firm = models.ForeignKey(LawFirm, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField()
    contact_phone = models.CharField(max_length=30)
    is_headquarters = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.firm.name}"

class PracticeArea(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    firms = models.ManyToManyField(LawFirm, related_name='practice_areas', blank=True)

    def __str__(self):
        return self.name

class FirmSetting(AuditTrackedModel):
    firm = models.OneToOneField(LawFirm, on_delete=models.CASCADE, related_name='settings')
    invoice_prefix = models.CharField(max_length=10, default="INV-")
    default_hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=250.00)
    tax_rate_percent = models.DecimalField(max_digits=5, decimal_places=2, default=18.00)
    enable_client_portal = models.BooleanField(default=True)
    automatic_reminders = models.BooleanField(default=True)

    def __str__(self):
        return f"Settings for {self.firm.name}"
