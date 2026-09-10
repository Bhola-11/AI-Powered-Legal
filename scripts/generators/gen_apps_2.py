# scripts/generators/gen_apps_2.py
import os

def generate_apps_part_2(base_dir):
    print("Generating Apps Part 2: cases, hearings, documents, evidence, legal_research...")

    # -------------------------------------------------------------
    # 6. CASES
    # -------------------------------------------------------------
    cases_dir = os.path.join(base_dir, "apps", "cases")
    os.makedirs(cases_dir, exist_ok=True)
    with open(os.path.join(cases_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Cases package\n")
    with open(os.path.join(cases_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class CasesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cases'
    verbose_name = 'Case Management & Lifecycle Engine'
""")
    with open(os.path.join(cases_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""import uuid
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
""")
    with open(os.path.join(cases_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Case, CaseStatus, OppositeParty, CaseAdvocateAssignment, CaseTimelineEvent, CaseNote

@login_required
def case_list(request):
    cases = Case.objects.filter(is_deleted=False).select_related('client', 'case_type', 'court_complex')
    return render(request, 'cases/case_list.html', {'cases': cases})

@login_required
def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    timeline = case.timeline_events.all().order_by('-event_date')
    notes = case.notes.all().order_by('-created_at')
    if request.user.is_client():
        notes = notes.filter(is_internal_only=False)
    advocates = case.assigned_advocates.all()
    opposite_parties = case.opposite_parties.all()
    return render(request, 'cases/case_detail.html', {
        'case': case,
        'timeline': timeline,
        'notes': notes,
        'advocates': advocates,
        'opposite_parties': opposite_parties,
    })

@login_required
def case_intake(request):
    return render(request, 'cases/case_intake.html')
""")
    with open(os.path.join(cases_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'cases'

urlpatterns = [
    path('', views.case_list, name='case_list'),
    path('intake/', views.case_intake, name='case_intake'),
    path('<uuid:pk>/', views.case_detail, name='case_detail'),
]
""")
    with open(os.path.join(cases_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import Case, CaseType, OppositeParty, CaseAdvocateAssignment, CaseNote, CaseTimelineEvent

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ['case_number', 'title', 'case_type', 'status', 'priority', 'client', 'next_hearing_date']
    list_filter = ['status', 'priority', 'case_type']
    search_fields = ['case_number', 'title', 'cnr_number']

@admin.register(CaseType)
class CaseTypeAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category']

@admin.register(OppositeParty)
class OppositePartyAdmin(admin.ModelAdmin):
    list_display = ['name', 'case', 'advocate_name']

@admin.register(CaseAdvocateAssignment)
class CaseAdvocateAssignmentAdmin(admin.ModelAdmin):
    list_display = ['case', 'advocate', 'role_in_case', 'is_primary']

@admin.register(CaseNote)
class CaseNoteAdmin(admin.ModelAdmin):
    list_display = ['case', 'title', 'author', 'is_internal_only']

@admin.register(CaseTimelineEvent)
class CaseTimelineEventAdmin(admin.ModelAdmin):
    list_display = ['case', 'event_title', 'event_date']
""")

    # -------------------------------------------------------------
    # 7. HEARINGS
    # -------------------------------------------------------------
    hear_dir = os.path.join(base_dir, "apps", "hearings")
    os.makedirs(hear_dir, exist_ok=True)
    with open(os.path.join(hear_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Hearings package\n")
    with open(os.path.join(hear_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class HearingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.hearings'
    verbose_name = 'Hearings, Calendar & Daily Board'
""")
    with open(os.path.join(hear_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class HearingType(models.TextChoices):
    ADMISSION = 'ADMISSION', 'Admission Hearing'
    FRAME_ISSUES = 'FRAME_ISSUES', 'Framing of Issues'
    EVIDENCE = 'EVIDENCE', 'Evidence & Witness Cross-Examination'
    INTERIM_RELIEF = 'INTERIM_RELIEF', 'Interim Relief / Injunction'
    FINAL_ARGUMENTS = 'FINAL_ARGUMENTS', 'Final Arguments'
    JUDGMENT = 'JUDGMENT', 'Pronouncement of Judgment'
    MISCELLANEOUS = 'MISCELLANEOUS', 'Miscellaneous / Compliance'

class Hearing(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='hearings')
    hearing_date = models.DateField(db_index=True)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    courtroom = models.ForeignKey('courts.CourtRoom', on_delete=models.SET_NULL, null=True, blank=True)
    judge = models.ForeignKey('courts.Judge', on_delete=models.SET_NULL, null=True, blank=True)
    hearing_type = models.CharField(max_length=30, choices=HearingType.choices, default=HearingType.ADMISSION)
    purpose = models.TextField()
    attending_advocate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    attendance_recorded = models.BooleanField(default=False)
    outcome_summary = models.TextField(blank=True, null=True)
    next_hearing_date = models.DateField(null=True, blank=True)
    interim_orders_passed = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Hearing for {self.case.case_number} on {self.hearing_date}"

class DailyBoard(AuditTrackedModel):
    board_date = models.DateField(unique=True)
    court_complex = models.ForeignKey('courts.CourtComplex', on_delete=models.CASCADE, related_name='daily_boards')
    total_matters = models.PositiveIntegerField(default=0)
    board_file = models.FileField(upload_to='cause_lists/', null=True, blank=True)

    def __str__(self):
        return f"Daily Board - {self.court_complex.name} ({self.board_date})"
""")
    with open(os.path.join(hear_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Hearing, DailyBoard

@login_required
def hearing_list(request):
    hearings = Hearing.objects.filter(is_deleted=False).select_related('case', 'judge', 'courtroom').order_by('hearing_date')
    return render(request, 'hearings/hearing_list.html', {'hearings': hearings})

@login_required
def hearing_detail(request, pk):
    hearing = get_object_or_404(Hearing, pk=pk)
    return render(request, 'hearings/hearing_detail.html', {'hearing': hearing})

@login_required
def daily_board_view(request):
    boards = DailyBoard.objects.all().order_by('-board_date')
    return render(request, 'hearings/daily_board.html', {'boards': boards})

@login_required
def calendar_view(request):
    return render(request, 'hearings/calendar.html')
""")
    with open(os.path.join(hear_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'hearings'

urlpatterns = [
    path('', views.hearing_list, name='hearing_list'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('daily-board/', views.daily_board_view, name='daily_board'),
    path('<uuid:pk>/', views.hearing_detail, name='hearing_detail'),
]
""")
    with open(os.path.join(hear_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import Hearing, DailyBoard

@admin.register(Hearing)
class HearingAdmin(admin.ModelAdmin):
    list_display = ['case', 'hearing_date', 'start_time', 'hearing_type', 'judge', 'is_completed']
    list_filter = ['hearing_type', 'is_completed', 'hearing_date']

@admin.register(DailyBoard)
class DailyBoardAdmin(admin.ModelAdmin):
    list_display = ['board_date', 'court_complex', 'total_matters']
""")

    # -------------------------------------------------------------
    # 8. DOCUMENTS
    # -------------------------------------------------------------
    doc_dir = os.path.join(base_dir, "apps", "documents")
    os.makedirs(doc_dir, exist_ok=True)
    with open(os.path.join(doc_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Documents package\n")
    with open(os.path.join(doc_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class DocumentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.documents'
    verbose_name = 'Legal Document Management & Vault'
""")
    with open(os.path.join(doc_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""import hashlib
from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class DocumentCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class LegalDocument(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='documents')
    category = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True, related_name='documents')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='legal_docs/%Y/%m/')
    file_sha256 = models.CharField(max_length=64, blank=True, null=True, help_text="Cryptographic integrity hash")
    file_size_bytes = models.BigIntegerField(default=0)
    current_version = models.PositiveIntegerField(default=1)
    is_client_visible = models.BooleanField(default=False)
    is_confidential = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (v{self.current_version})"

    def compute_hash(self):
        if self.file:
            sha = hashlib.sha256()
            for chunk in self.file.chunks():
                sha.update(chunk)
            self.file_sha256 = sha.hexdigest()

class DocumentVersion(AuditTrackedModel):
    document = models.ForeignKey(LegalDocument, on_delete=models.CASCADE, related_name='versions')
    version_number = models.PositiveIntegerField()
    file = models.FileField(upload_to='legal_docs/versions/')
    file_sha256 = models.CharField(max_length=64)
    change_notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('document', 'version_number')
""")
    with open(os.path.join(doc_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LegalDocument, DocumentCategory

@login_required
def document_vault(request):
    docs = LegalDocument.objects.filter(is_deleted=False).select_related('case', 'category')
    if request.user.is_client():
        docs = docs.filter(is_client_visible=True)
    return render(request, 'documents/vault.html', {'documents': docs})

@login_required
def document_detail(request, pk):
    doc = get_object_or_404(LegalDocument, pk=pk)
    versions = doc.versions.all().order_by('-version_number')
    return render(request, 'documents/detail.html', {'document': doc, 'versions': versions})
""")
    with open(os.path.join(doc_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('', views.document_vault, name='vault'),
    path('<uuid:pk>/', views.document_detail, name='detail'),
]
""")
    with open(os.path.join(doc_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import DocumentCategory, LegalDocument, DocumentVersion

@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'case', 'category', 'current_version', 'is_client_visible', 'is_confidential']
    list_filter = ['category', 'is_client_visible', 'is_confidential']
    search_fields = ['title', 'file_sha256']

@admin.register(DocumentVersion)
class DocumentVersionAdmin(admin.ModelAdmin):
    list_display = ['document', 'version_number', 'file_sha256']
""")

    # -------------------------------------------------------------
    # 9. EVIDENCE
    # -------------------------------------------------------------
    ev_dir = os.path.join(base_dir, "apps", "evidence")
    os.makedirs(ev_dir, exist_ok=True)
    with open(os.path.join(ev_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Evidence package\n")
    with open(os.path.join(ev_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class EvidenceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.evidence'
    verbose_name = 'Evidence Register & Chain of Custody'
""")
    with open(os.path.join(ev_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class EvidenceCategory(models.TextChoices):
    DOCUMENTARY = 'DOCUMENTARY', 'Documentary Evidence'
    ELECTRONIC = 'ELECTRONIC', 'Electronic / Digital Record'
    PHYSICAL = 'PHYSICAL', 'Physical / Forensic Material'
    TESTIMONIAL = 'TESTIMONIAL', 'Deposition / Witness Statement'

class EvidenceItem(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='evidence_items')
    item_code = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=30, choices=EvidenceCategory.choices, default=EvidenceCategory.DOCUMENTARY)
    description = models.TextField()
    source_origin = models.CharField(max_length=255, help_text="Where and from whom obtained")
    collection_date = models.DateField()
    current_custodian = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='held_evidence')
    custody_location = models.CharField(max_length=255, default='Law Firm Vault')
    admissibility_status = models.CharField(max_length=30, default='SUBMITTED', choices=[('SUBMITTED', 'Submitted'), ('MARKED_EXHIBIT', 'Marked as Exhibit'), ('OBJECTED', 'Objected by Adverse Party'), ('ADMITTED', 'Admitted in Evidence'), ('REJECTED', 'Rejected by Court')])
    exhibit_mark = models.CharField(max_length=30, blank=True, null=True, help_text="e.g. Ex. P-1 or Ex. D-2")

    def __str__(self):
        return f"[{self.item_code}] {self.title}"

class ChainOfCustodyLog(AuditTrackedModel):
    evidence = models.ForeignKey(EvidenceItem, on_delete=models.CASCADE, related_name='custody_logs')
    transferred_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='custody_transfers_sent')
    transferred_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='custody_transfers_received')
    transfer_date = models.DateTimeField(auto_now_add=True)
    purpose_of_transfer = models.TextField()
    security_seal_number = models.CharField(max_length=100, blank=True, null=True)

class WitnessEvidenceLink(AuditTrackedModel):
    evidence = models.ForeignKey(EvidenceItem, on_delete=models.CASCADE, related_name='witness_links')
    witness_name = models.CharField(max_length=255)
    statement_summary = models.TextField()
""")
    with open(os.path.join(ev_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EvidenceItem, ChainOfCustodyLog

@login_required
def evidence_register(request):
    items = EvidenceItem.objects.filter(is_deleted=False).select_related('case', 'current_custodian')
    return render(request, 'evidence/register.html', {'items': items})

@login_required
def evidence_detail(request, pk):
    item = get_object_or_404(EvidenceItem, pk=pk)
    custody_logs = item.custody_logs.all().order_by('-transfer_date')
    return render(request, 'evidence/detail.html', {'item': item, 'custody_logs': custody_logs})
""")
    with open(os.path.join(ev_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'evidence'

urlpatterns = [
    path('', views.evidence_register, name='register'),
    path('<uuid:pk>/', views.evidence_detail, name='detail'),
]
""")
    with open(os.path.join(ev_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import EvidenceItem, ChainOfCustodyLog, WitnessEvidenceLink

@admin.register(EvidenceItem)
class EvidenceItemAdmin(admin.ModelAdmin):
    list_display = ['item_code', 'title', 'case', 'category', 'admissibility_status', 'exhibit_mark']
    list_filter = ['category', 'admissibility_status']
    search_fields = ['item_code', 'title', 'exhibit_mark']

@admin.register(ChainOfCustodyLog)
class ChainOfCustodyLogAdmin(admin.ModelAdmin):
    list_display = ['evidence', 'transferred_from', 'transferred_to', 'transfer_date']
""")

    # -------------------------------------------------------------
    # 10. LEGAL RESEARCH
    # -------------------------------------------------------------
    res_dir = os.path.join(base_dir, "apps", "legal_research")
    os.makedirs(res_dir, exist_ok=True)
    with open(os.path.join(res_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Legal research package\n")
    with open(os.path.join(res_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class LegalResearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.legal_research'
    verbose_name = 'Legal Research Workspace & Precedents'
""")
    with open(os.path.join(res_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class StatutoryAct(AuditTrackedModel):
    title = models.CharField(max_length=255, unique=True)
    act_number = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    preamble = models.TextField(blank=True, null=True)
    jurisdiction = models.CharField(max_length=100, default='National')

    def __str__(self):
        return f"{self.title} ({self.year})"

class StatutorySection(AuditTrackedModel):
    act = models.ForeignKey(StatutoryAct, on_delete=models.CASCADE, related_name='sections')
    section_number = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    content = models.TextField()
    explanations = models.TextField(blank=True, null=True)
    punishment_or_remedy = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Sec. {self.section_number} - {self.act.title}"

class CasePrecedent(UUIDModel, AuditTrackedModel):
    citation = models.CharField(max_length=150, unique=True, db_index=True)
    case_name = models.CharField(max_length=300)
    court = models.CharField(max_length=150)
    judgment_date = models.DateField()
    bench = models.CharField(max_length=255, blank=True, null=True)
    headnotes = models.TextField()
    ratio_decidendi = models.TextField()
    legal_principles = models.TextField()
    is_landmark = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.case_name} [{self.citation}]"

class ResearchNotebook(AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='research_notes', null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    associated_precedents = models.ManyToManyField(CasePrecedent, blank=True)
    associated_sections = models.ManyToManyField(StatutorySection, blank=True)

    def __str__(self):
        return self.title
""")
    with open(os.path.join(res_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import StatutoryAct, StatutorySection, CasePrecedent, ResearchNotebook

@login_required
def acts_list(request):
    acts = StatutoryAct.objects.all().order_by('title')
    return render(request, 'research/acts_list.html', {'acts': acts})

@login_required
def act_detail(request, pk):
    act = get_object_or_404(StatutoryAct, pk=pk)
    sections = act.sections.all().order_by('id')
    return render(request, 'research/act_detail.html', {'act': act, 'sections': sections})

@login_required
def precedent_list(request):
    precedents = CasePrecedent.objects.all().order_by('-judgment_date')
    return render(request, 'research/precedent_list.html', {'precedents': precedents})

@login_required
def precedent_detail(request, pk):
    prec = get_object_or_404(CasePrecedent, pk=pk)
    return render(request, 'research/precedent_detail.html', {'precedent': prec})

@login_required
def notebook_view(request):
    notebooks = ResearchNotebook.objects.filter(author=request.user)
    return render(request, 'research/notebook.html', {'notebooks': notebooks})
""")
    with open(os.path.join(res_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'legal_research'

urlpatterns = [
    path('acts/', views.acts_list, name='acts_list'),
    path('acts/<int:pk>/', views.act_detail, name='act_detail'),
    path('precedents/', views.precedent_list, name='precedent_list'),
    path('precedents/<uuid:pk>/', views.precedent_detail, name='precedent_detail'),
    path('notebook/', views.notebook_view, name='notebook'),
]
""")
    with open(os.path.join(res_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import StatutoryAct, StatutorySection, CasePrecedent, ResearchNotebook

@admin.register(StatutoryAct)
class StatutoryActAdmin(admin.ModelAdmin):
    list_display = ['title', 'act_number', 'year', 'jurisdiction']

@admin.register(StatutorySection)
class StatutorySectionAdmin(admin.ModelAdmin):
    list_display = ['section_number', 'title', 'act']
    search_fields = ['section_number', 'title', 'content']

@admin.register(CasePrecedent)
class CasePrecedentAdmin(admin.ModelAdmin):
    list_display = ['citation', 'case_name', 'court', 'judgment_date', 'is_landmark']
    search_fields = ['citation', 'case_name', 'ratio_decidendi']
    list_filter = ['is_landmark', 'court']

@admin.register(ResearchNotebook)
class ResearchNotebookAdmin(admin.ModelAdmin):
    list_display = ['title', 'case', 'author']
""")

    print("Completed Apps Part 2 generation.")

if __name__ == '__main__':
    generate_apps_part_2('.')
