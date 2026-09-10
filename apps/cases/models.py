import uuid
from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class CaseStatus(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft'
    INTAKE = 'INTAKE', 'Case Intake'
    CONFLICT_CHECK = 'CONFLICT_CHECK', 'Conflict Check'
    VERIFICATION = 'VERIFICATION', 'Client Verification'
    REGISTERED = 'REGISTERED', 'Case Registered'
    COURT_ASSIGNED = 'COURT_ASSIGNED', 'Court Assigned'
    ADVOCATE_ASSIGNED = 'ADVOCATE_ASSIGNED', 'Advocate Assigned'
    DOCUMENTS_COLLECTED = 'DOCUMENTS_COLLECTED', 'Document Collection'
    EVIDENCE_PREPARED = 'EVIDENCE_PREPARED', 'Evidence Preparation'
    HEARING_SCHEDULED = 'HEARING_SCHEDULED', 'Hearing Scheduled'
    HEARING_HELD = 'HEARING_HELD', 'Hearing In Session'
    ORDER_RECORDED = 'ORDER_RECORDED', 'Order Recorded'
    FOLLOWUP_TASKS = 'FOLLOWUP_TASKS', 'Follow-up Tasks'
    NEXT_HEARING = 'NEXT_HEARING', 'Next Hearing'
    DISPOSED = 'DISPOSED', 'Disposed'
    COMPLIANCE = 'COMPLIANCE', 'Compliance Tracking'
    CLOSED = 'CLOSED', 'Case Closed'
    ARCHIVED = 'ARCHIVED', 'Archived'

class CasePriority(models.TextChoices):
    CRITICAL = 'CRITICAL', 'Critical / Urgent'
    HIGH = 'HIGH', 'High'
    MEDIUM = 'MEDIUM', 'Medium'
    LOW = 'LOW', 'Low'

class CaseType(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=50, choices=[('CIVIL', 'Civil'), ('CRIMINAL', 'Criminal'), ('CONSTITUTIONAL', 'Constitutional'), ('COMMERCIAL', 'Commercial'), ('ARBITRATION', 'Arbitration'), ('FAMILY', 'Family')])
    default_limitation_days = models.PositiveIntegerField(default=90)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Case(UUIDModel, AuditTrackedModel):
    case_number = models.CharField(max_length=100, unique=True, db_index=True)
    internal_reference = models.CharField(max_length=100, blank=True, null=True)
    cnr_number = models.CharField(max_length=50, blank=True, null=True, help_text="Case Number Record for National Judicial Data Grid")
    title = models.CharField(max_length=300)
    case_type = models.ForeignKey(CaseType, on_delete=models.PROTECT, related_name='cases')
    court_complex = models.ForeignKey('courts.CourtComplex', on_delete=models.SET_NULL, null=True, blank=True, related_name='cases')
    courtroom = models.ForeignKey('courts.CourtRoom', on_delete=models.SET_NULL, null=True, blank=True, related_name='cases')
    presiding_judge = models.ForeignKey('courts.Judge', on_delete=models.SET_NULL, null=True, blank=True, related_name='cases')
    status = models.CharField(max_length=30, choices=CaseStatus.choices, default=CaseStatus.DRAFT, db_index=True)
    priority = models.CharField(max_length=20, choices=CasePriority.choices, default=CasePriority.MEDIUM)
    client = models.ForeignKey('clients.ClientProfile', on_delete=models.PROTECT, related_name='cases')
    law_firm = models.ForeignKey('firms.LawFirm', on_delete=models.CASCADE, related_name='cases', null=True, blank=True)
    filing_date = models.DateField(null=True, blank=True)
    next_hearing_date = models.DateField(null=True, blank=True)
    case_value = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    legal_issues = models.TextField(blank=True, null=True)
    relevant_laws = models.TextField(blank=True, null=True)
    confidentiality_level = models.CharField(max_length=20, default='STANDARD', choices=[('STANDARD', 'Standard Firm Access'), ('RESTRICTED', 'Restricted Counsel Only'), ('SEALED', 'Sealed Matter')])

    def __str__(self):
        return f"[{self.case_number}] {self.title}"

class OppositeParty(AuditTrackedModel):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='opposite_parties')
    name = models.CharField(max_length=255)
    advocate_name = models.CharField(max_length=255, blank=True, null=True)
    advocate_contact = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

class CaseAdvocateAssignment(AuditTrackedModel):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='assigned_advocates')
    advocate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='case_assignments')
    role_in_case = models.CharField(max_length=50, default='LEAD_COUNSEL', choices=[('LEAD_COUNSEL', 'Lead Counsel'), ('BRIEFING_COUNSEL', 'Briefing Counsel'), ('ASSOCIATE', 'Associate Advocate'), ('ADVOCATE_ON_RECORD', 'Advocate on Record')])
    assigned_at = models.DateTimeField(auto_now_add=True)
    is_primary = models.BooleanField(default=False)

class CaseNote(AuditTrackedModel):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='notes')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_internal_only = models.BooleanField(default=True, help_text="Strictly isolated from clients")

class CaseTimelineEvent(AuditTrackedModel):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='timeline_events')
    event_title = models.CharField(max_length=255)
    event_description = models.TextField(blank=True, null=True)
    event_type = models.CharField(max_length=50, default='STATUS_CHANGE')
    event_date = models.DateTimeField()
