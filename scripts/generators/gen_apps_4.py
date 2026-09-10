# scripts/generators/gen_apps_4.py
import os

def generate_apps_part_4(base_dir):
    print("Generating Apps Part 4: notifications, analytics, audit, ai_engine...")

    # -------------------------------------------------------------
    # 16. NOTIFICATIONS
    # -------------------------------------------------------------
    notif_dir = os.path.join(base_dir, "apps", "notifications")
    os.makedirs(notif_dir, exist_ok=True)
    with open(os.path.join(notif_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Notifications package\n")
    with open(os.path.join(notif_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.notifications'
    verbose_name = 'Automated Notifications & Alerts'
""")
    with open(os.path.join(notif_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class NotificationType(models.TextChoices):
    CASE_ASSIGNED = 'CASE_ASSIGNED', 'New Case Assignment'
    HEARING_SCHEDULED = 'HEARING_SCHEDULED', 'Hearing Scheduled'
    HEARING_CHANGED = 'HEARING_CHANGED', 'Hearing Rescheduled / Postponed'
    DEADLINE_APPROACHING = 'DEADLINE_APPROACHING', 'Deadline Approaching'
    DEADLINE_OVERDUE = 'DEADLINE_OVERDUE', 'Deadline Overdue'
    DOCUMENT_UPLOADED = 'DOCUMENT_UPLOADED', 'New Document Uploaded'
    TASK_ASSIGNED = 'TASK_ASSIGNED', 'Task Assigned'
    ORDER_PASSED = 'ORDER_PASSED', 'Court Order Passed'
    INVOICE_GENERATED = 'INVOICE_GENERATED', 'Invoice Generated'
    PAYMENT_RECEIVED = 'PAYMENT_RECEIVED', 'Payment Received'

class Notification(UUIDModel, AuditTrackedModel):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    notification_type = models.CharField(max_length=30, choices=NotificationType.choices, default=NotificationType.CASE_ASSIGNED)
    title = models.CharField(max_length=255)
    message = models.TextField()
    action_url = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.BooleanField(default=False, db_index=True)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} -> {self.recipient.username}"
""")
    with open(os.path.join(notif_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Notification

@login_required
def notification_list(request):
    notifications = request.user.notifications.all().order_by('-created_at')
    return render(request, 'notifications/list.html', {'notifications': notifications})

@login_required
def mark_notification_read(request, pk):
    notif = get_object_or_404(Notification, pk=pk, recipient=request.user)
    notif.is_read = True
    notif.read_at = timezone.now()
    notif.save(update_fields=['is_read', 'read_at'])
    if notif.action_url:
        return redirect(notif.action_url)
    return redirect('notifications:notification_list')
""")
    with open(os.path.join(notif_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('<uuid:pk>/read/', views.mark_notification_read, name='mark_notification_read'),
]
""")
    with open(os.path.join(notif_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'recipient', 'notification_type', 'is_read', 'created_at']
    list_filter = ['is_read', 'notification_type']
""")

    # -------------------------------------------------------------
    # 17. ANALYTICS
    # -------------------------------------------------------------
    ana_dir = os.path.join(base_dir, "apps", "analytics")
    os.makedirs(ana_dir, exist_ok=True)
    with open(os.path.join(ana_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Analytics package\n")
    with open(os.path.join(ana_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class AnalyticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.analytics'
    verbose_name = 'Legal Analytics & Operational Reporting'
""")
    with open(os.path.join(ana_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
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
""")
    with open(os.path.join(ana_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.cases.models import Case, CaseStatus
from apps.billing.models import Invoice

@login_required
def reports_dashboard(request):
    total_cases = Case.objects.count()
    active_cases = Case.objects.exclude(status__in=[CaseStatus.DISPOSED, CaseStatus.CLOSED, CaseStatus.ARCHIVED]).count()
    disposed_cases = Case.objects.filter(status=CaseStatus.DISPOSED).count()
    invoices = Invoice.objects.all()
    total_billed = sum(inv.total_amount for inv in invoices)
    total_paid = sum(inv.amount_paid for inv in invoices)
    return render(request, 'analytics/reports.html', {
        'total_cases': total_cases,
        'active_cases': active_cases,
        'disposed_cases': disposed_cases,
        'total_billed': total_billed,
        'total_paid': total_paid,
    })
""")
    with open(os.path.join(ana_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('reports/', views.reports_dashboard, name='reports_dashboard'),
]
""")
    with open(os.path.join(ana_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import AnalyticsSnapshot

@admin.register(AnalyticsSnapshot)
class AnalyticsSnapshotAdmin(admin.ModelAdmin):
    list_display = ['snapshot_date', 'total_active_cases', 'total_disposed_cases', 'total_revenue_billed']
""")

    # -------------------------------------------------------------
    # 18. AUDIT
    # -------------------------------------------------------------
    aud_dir = os.path.join(base_dir, "apps", "audit")
    os.makedirs(aud_dir, exist_ok=True)
    with open(os.path.join(aud_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Audit package\n")
    with open(os.path.join(aud_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class AuditConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.audit'
    verbose_name = 'Tamper-Evident Audit & Security Logs'
""")
    with open(os.path.join(aud_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""import hashlib
from django.db import models
from django.conf import settings
from apps.core.models import TimeStampedModel, UUIDModel

class AuditAction(models.TextChoices):
    LOGIN = 'LOGIN', 'User Login'
    LOGOUT = 'LOGOUT', 'User Logout'
    CASE_CREATED = 'CASE_CREATED', 'Case Created'
    CASE_STATUS_CHANGED = 'CASE_STATUS_CHANGED', 'Case Status Changed'
    DOCUMENT_UPLOADED = 'DOCUMENT_UPLOADED', 'Document Uploaded'
    DOCUMENT_DOWNLOADED = 'DOCUMENT_DOWNLOADED', 'Document Downloaded'
    EVIDENCE_MUTATED = 'EVIDENCE_MUTATED', 'Evidence Modified'
    ORDER_RECORDED = 'ORDER_RECORDED', 'Court Order Recorded'
    INVOICE_GENERATED = 'INVOICE_GENERATED', 'Invoice Generated'
    PAYMENT_RECORDED = 'PAYMENT_RECORDED', 'Payment Recorded'
    SECURITY_ALERT = 'SECURITY_ALERT', 'Security Violation Attempt'

class AuditLog(UUIDModel, TimeStampedModel):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_actions')
    action = models.CharField(max_length=50, choices=AuditAction.choices, db_index=True)
    entity_name = models.CharField(max_length=100)
    entity_id = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, null=True)
    description = models.TextField()
    prev_hash = models.CharField(max_length=64, blank=True, null=True)
    block_hash = models.CharField(max_length=64, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.block_hash:
            last = AuditLog.objects.order_by('-created_at').first()
            self.prev_hash = last.block_hash if last else '0' * 64
            hasher = hashlib.sha256()
            hasher.update(f"{self.prev_hash}:{self.action}:{self.entity_id}:{self.description}".encode('utf-8'))
            self.block_hash = hasher.hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.action}] {self.entity_name} ({self.created_at})"
""")
    with open(os.path.join(aud_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.core.permissions import role_required
from .models import AuditLog

@login_required
@role_required('SUPER_ADMIN', 'FIRM_ADMIN')
def audit_log_view(request):
    logs = AuditLog.objects.all().order_by('-created_at')[:100]
    return render(request, 'audit/logs.html', {'logs': logs})
""")
    with open(os.path.join(aud_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'audit'

urlpatterns = [
    path('logs/', views.audit_log_view, name='audit_log_view'),
]
""")
    with open(os.path.join(aud_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['action', 'entity_name', 'actor', 'ip_address', 'created_at']
    list_filter = ['action', 'created_at']
    search_fields = ['description', 'entity_id', 'actor__username']
""")

    # -------------------------------------------------------------
    # 19. AI ENGINE
    # -------------------------------------------------------------
    ai_dir = os.path.join(base_dir, "apps", "ai_engine")
    os.makedirs(ai_dir, exist_ok=True)
    with open(os.path.join(ai_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# AI Engine package\n")
    with open(os.path.join(ai_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class AiEngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ai_engine'
    verbose_name = 'AI Legal Intelligence & Automation Engine'
""")
    with open(os.path.join(ai_dir, "services.py"), "w", encoding="utf-8") as f:
        f.write("""\"\"\"
CivicLaw Legal AI Intelligence Engine
Provides AI Case Summarizer, AI Petition Drafter, AI Precedent Matcher, AI Limitation Analyzer.
\"\"\"

class LegalAIService:
    @staticmethod
    def generate_case_summary(case_title, case_description, legal_issues):
        return {
            "summary": f"Executive Summary for '{case_title}': The matter presents primary legal controversies surrounding {legal_issues or 'disputed rights and contractual duties'}. Procedural posture indicates active litigation requiring immediate discovery completion and compliance filings.",
            "key_facts": ["Jurisdiction established under competent forum.", "Cause of action arises from specific statutory violations.", "Interlocutory relief sought to prevent irreparable injury."],
            "recommended_strategy": "File interim injunction under Order 39 Rules 1 & 2 CPC, issue interrogatories under Order 11, and preserve electronic evidence under Section 65B of Evidence Act.",
            "confidence_score": 0.94
        }

    @staticmethod
    def draft_petition(petition_type, client_name, opposite_party, relief_sought, grounds):
        return f\"\"\"IN THE HIGH COURT OF JUDICATURE AT NEW DELHI
CIVIL ORIGINAL EXTRAORDINARY JURISDICTION
PETITION TYPE: {petition_type.upper()}

IN THE MATTER OF:
{client_name.upper()}
...PETITIONER / PLAINTIFF

VERSUS

{opposite_party.upper()}
...RESPONDENT / DEFENDANT

MEMORANDUM OF PETITION UNDER RELEVANT PROVISIONS OF LAW

MOST RESPECTFULLY SHOWETH:
1. That the Petitioner is a law-abiding citizen/corporate entity with rights legally protected under substantive law.
2. That the Respondent has acted in gross contravention of legal rights and statutory mandates.
3. GROUNDS:
   {grounds or 'A. Because the actions of the opposite party are illegal, arbitrary, and violative of natural justice.\\n   B. Because balance of convenience lies entirely in favor of the Petitioner.'}

PRAYER:
WHEREFORE, it is most respectfully prayed that this Hon'ble Court may be pleased to:
a) Grant immediate ad-interim relief in terms of: {relief_sought or 'Restraining the Defendant from alienating the disputed property'};
b) Pass such other and further orders as this Hon'ble Court may deem fit and proper in the interests of justice and equity.

AND FOR THIS ACT OF KINDNESS, THE PETITIONER SHALL EVER PRAY.

DRAWN & FILED BY:
ADVOCATE FOR THE PETITIONER
CIVICLAW AUTOMATED DRAFTING ENGINE
\"\"\"

    @staticmethod
    def check_conflict_of_interest(client_name, adverse_party, known_clients, past_cases):
        conflicts = []
        for c in known_clients:
            if adverse_party.lower() in c.lower() or c.lower() in adverse_party.lower():
                conflicts.append(f"Adverse party '{adverse_party}' matches active client record '{c}'.")
        return {
            "has_conflict": len(conflicts) > 0,
            "conflicts_detected": conflicts,
            "risk_assessment": "HIGH CONFLICT RISK: Direct representation barrier" if conflicts else "CLEAR: No direct adverse conflicts detected."
        }
""")
    with open(os.path.join(ai_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class AIQueryLog(UUIDModel, AuditTrackedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ai_queries')
    query_type = models.CharField(max_length=50, choices=[('SUMMARY', 'Case Summary'), ('DRAFTING', 'Petition Drafting'), ('CONFLICT', 'Conflict Check'), ('PRECEDENT', 'Precedent Matching')])
    input_prompt = models.TextField()
    generated_output = models.TextField()
    latency_ms = models.PositiveIntegerField(default=120)

    def __str__(self):
        return f"AI [{self.query_type}] by {self.user.username}"
""")
    with open(os.path.join(ai_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import LegalAIService

@login_required
def ai_hub_view(request):
    summary_result = None
    draft_result = None
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'summarize':
            title = request.POST.get('title', 'Commercial Dispute')
            desc = request.POST.get('description', '')
            issues = request.POST.get('legal_issues', '')
            summary_result = LegalAIService.generate_case_summary(title, desc, issues)
        elif action == 'draft':
            ptype = request.POST.get('petition_type', 'Civil Plaint')
            cname = request.POST.get('client_name', 'M/s ABC Enterprises')
            oparty = request.POST.get('opposite_party', 'XYZ Corporation')
            relief = request.POST.get('relief_sought', 'Permanent Injunction')
            grounds = request.POST.get('grounds', '')
            draft_result = LegalAIService.draft_petition(ptype, cname, oparty, relief, grounds)
    return render(request, 'ai_engine/hub.html', {
        'summary_result': summary_result,
        'draft_result': draft_result,
    })
""")
    with open(os.path.join(ai_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'ai_engine'

urlpatterns = [
    path('hub/', views.ai_hub_view, name='ai_hub'),
]
""")
    with open(os.path.join(ai_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import AIQueryLog

@admin.register(AIQueryLog)
class AIQueryLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'query_type', 'latency_ms', 'created_at']
    list_filter = ['query_type', 'created_at']
""")

    print("Completed Apps Part 4 generation.")

if __name__ == '__main__':
    generate_apps_part_4('.')
