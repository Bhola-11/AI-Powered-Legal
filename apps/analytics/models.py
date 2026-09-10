from django.db import models
from apps.core.models import AuditTrackedModel

class AnalyticsSnapshot(AuditTrackedModel):
    snapshot_date = models.DateField(unique=True)
    total_active_cases = models.PositiveIntegerField(default=0)
    total_disposed_cases = models.PositiveIntegerField(default=0)
    total_hearings_held = models.PositiveIntegerField(default=0)
    total_revenue_billed = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    total_revenue_collected = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    compliance_rate_percent = models.DecimalField(max_digits=5, decimal_places=2, default=95.00)

    def __str__(self):
        return f"Analytics Snapshot ({self.snapshot_date})"
