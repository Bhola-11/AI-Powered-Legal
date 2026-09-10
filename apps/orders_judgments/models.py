from django.db import models
from apps.core.models import AuditTrackedModel, UUIDModel

class OrderType(models.TextChoices):
    INTERIM = 'INTERIM', 'Interim Order / Injunction'
    PROCEDURAL = 'PROCEDURAL', 'Procedural Direction'
    CONSENT = 'CONSENT', 'Consent Order'
    FINAL_JUDGMENT = 'FINAL_JUDGMENT', 'Final Judgment & Decree'
    DISMISSAL = 'DISMISSAL', 'Order of Dismissal'

class CourtOrder(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='court_orders')
    hearing = models.ForeignKey('hearings.Hearing', on_delete=models.SET_NULL, null=True, blank=True)
    order_type = models.CharField(max_length=30, choices=OrderType.choices, default=OrderType.INTERIM)
    order_date = models.DateField(db_index=True)
    presiding_judge = models.ForeignKey('courts.Judge', on_delete=models.SET_NULL, null=True)
    summary = models.TextField()
    operative_directions = models.TextField()
    certified_copy = models.FileField(upload_to='court_orders/%Y/%m/', null=True, blank=True)
    requires_compliance = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_order_type_display()} - {self.case.case_number} ({self.order_date})"

class ComplianceItem(AuditTrackedModel):
    order = models.ForeignKey(CourtOrder, on_delete=models.CASCADE, related_name='compliance_items')
    direction_text = models.TextField()
    deadline = models.DateField()
    responsible_party = models.CharField(max_length=150, help_text="Petitioner, Respondent, Registry, Police, Authority")
    is_complied = models.BooleanField(default=False)
    compliance_date = models.DateField(null=True, blank=True)
    compliance_affidavit_filed = models.BooleanField(default=False)
