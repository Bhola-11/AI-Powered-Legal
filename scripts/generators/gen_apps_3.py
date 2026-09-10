# scripts/generators/gen_apps_3.py
import os

def generate_apps_part_3(base_dir):
    print("Generating Apps Part 3: tasks, deadlines, communications, billing, orders_judgments...")

    # -------------------------------------------------------------
    # 11. TASKS
    # -------------------------------------------------------------
    task_dir = os.path.join(base_dir, "apps", "tasks")
    os.makedirs(task_dir, exist_ok=True)
    with open(os.path.join(task_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Tasks package\n")
    with open(os.path.join(task_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tasks'
    verbose_name = 'Task & Workflow Management'
""")
    with open(os.path.join(task_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class TaskStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    BLOCKED = 'BLOCKED', 'Blocked'
    COMPLETED = 'COMPLETED', 'Completed'
    CANCELLED = 'CANCELLED', 'Cancelled'

class TaskPriority(models.TextChoices):
    CRITICAL = 'CRITICAL', 'Critical'
    HIGH = 'HIGH', 'High'
    MEDIUM = 'MEDIUM', 'Medium'
    LOW = 'LOW', 'Low'

class WorkflowStage(AuditTrackedModel):
    name = models.CharField(max_length=100)
    stage_order = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.stage_order}. {self.name}"

class CaseTask(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='tasks')
    hearing = models.ForeignKey('hearings.Hearing', on_delete=models.SET_NULL, null=True, blank=True, related_name='followup_tasks')
    workflow_stage = models.ForeignKey(WorkflowStage, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='assigned_tasks')
    priority = models.CharField(max_length=20, choices=TaskPriority.choices, default=TaskPriority.MEDIUM)
    status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.PENDING, db_index=True)
    due_date = models.DateField(db_index=True)
    completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"[{self.status}] {self.title}"

class TaskChecklist(AuditTrackedModel):
    task = models.ForeignKey(CaseTask, on_delete=models.CASCADE, related_name='checklists')
    item_title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
""")
    with open(os.path.join(task_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CaseTask, WorkflowStage

@login_required
def task_list(request):
    tasks = CaseTask.objects.filter(is_deleted=False).select_related('case', 'assignee')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def kanban_view(request):
    tasks = CaseTask.objects.filter(is_deleted=False).select_related('case', 'assignee')
    return render(request, 'tasks/kanban.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(CaseTask, pk=pk)
    checklists = task.checklists.all()
    return render(request, 'tasks/detail.html', {'task': task, 'checklists': checklists})
""")
    with open(os.path.join(task_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('kanban/', views.kanban_view, name='kanban'),
    path('<uuid:pk>/', views.task_detail, name='task_detail'),
]
""")
    with open(os.path.join(task_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import CaseTask, WorkflowStage, TaskChecklist

@admin.register(CaseTask)
class CaseTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'case', 'assignee', 'priority', 'status', 'due_date']
    list_filter = ['status', 'priority', 'due_date']

@admin.register(WorkflowStage)
class WorkflowStageAdmin(admin.ModelAdmin):
    list_display = ['stage_order', 'name']

@admin.register(TaskChecklist)
class TaskChecklistAdmin(admin.ModelAdmin):
    list_display = ['item_title', 'task', 'is_completed']
""")

    # -------------------------------------------------------------
    # 12. DEADLINES
    # -------------------------------------------------------------
    dl_dir = os.path.join(base_dir, "apps", "deadlines")
    os.makedirs(dl_dir, exist_ok=True)
    with open(os.path.join(dl_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Deadlines package\n")
    with open(os.path.join(dl_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class DeadlinesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.deadlines'
    verbose_name = 'Deadlines & Limitation Tracking Engine'
""")
    with open(os.path.join(dl_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from django.utils import timezone
from apps.core.models import AuditTrackedModel, UUIDModel

class DeadlineType(models.TextChoices):
    STATUTORY_LIMITATION = 'STATUTORY_LIMITATION', 'Statutory Limitation Date'
    COURT_FILING = 'COURT_FILING', 'Court Filing Deadline'
    WRITTEN_STATEMENT = 'WRITTEN_STATEMENT', 'Written Statement / Reply Deadline'
    COMPLIANCE = 'COMPLIANCE', 'Court Order Compliance Deadline'
    APPEAL_PERIOD = 'APPEAL_PERIOD', 'Limitation for Appeal / Review'
    DISCOVERY = 'DISCOVERY', 'Discovery / Interrogatories Response'

class CaseDeadline(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='deadlines')
    title = models.CharField(max_length=255)
    deadline_type = models.CharField(max_length=30, choices=DeadlineType.choices, default=DeadlineType.COURT_FILING)
    due_date = models.DateField(db_index=True)
    statutory_provision = models.CharField(max_length=255, blank=True, null=True, help_text="e.g. Limitation Act Art. 113 or CPC O.VIII R.1")
    is_statutory = models.BooleanField(default=False)
    is_met = models.BooleanField(default=False)
    met_at = models.DateTimeField(null=True, blank=True)
    reminder_days_before = models.CharField(max_length=50, default="30,15,7,2,1")

    def __str__(self):
        return f"{self.title} ({self.due_date})"

    @property
    def is_overdue(self):
        return not self.is_met and self.due_date < timezone.now().date()
""")
    with open(os.path.join(dl_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CaseDeadline

@login_required
def deadline_list(request):
    deadlines = CaseDeadline.objects.filter(is_deleted=False).select_related('case').order_by('due_date')
    return render(request, 'deadlines/list.html', {'deadlines': deadlines})

@login_required
def limitation_calculator_view(request):
    return render(request, 'deadlines/limitation_calculator.html')
""")
    with open(os.path.join(dl_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'deadlines'

urlpatterns = [
    path('', views.deadline_list, name='deadline_list'),
    path('calculator/', views.limitation_calculator_view, name='limitation_calculator'),
]
""")
    with open(os.path.join(dl_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import CaseDeadline

@admin.register(CaseDeadline)
class CaseDeadlineAdmin(admin.ModelAdmin):
    list_display = ['title', 'case', 'deadline_type', 'due_date', 'is_statutory', 'is_met']
    list_filter = ['deadline_type', 'is_statutory', 'is_met', 'due_date']
""")

    # -------------------------------------------------------------
    # 13. COMMUNICATIONS
    # -------------------------------------------------------------
    comm_dir = os.path.join(base_dir, "apps", "communications")
    os.makedirs(comm_dir, exist_ok=True)
    with open(os.path.join(comm_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Communications package\n")
    with open(os.path.join(comm_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class CommunicationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.communications'
    verbose_name = 'Client Communication & Secure Messaging'
""")
    with open(os.path.join(comm_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class MessageThread(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='communication_threads')
    subject = models.CharField(max_length=255)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='message_threads')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.subject} ({self.case.case_number})"

class CaseMessage(UUIDModel, AuditTrackedModel):
    thread = models.ForeignKey(MessageThread, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Msg from {self.sender.username} at {self.created_at}"

class MessageAttachment(AuditTrackedModel):
    message = models.ForeignKey(CaseMessage, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='message_attachments/%Y/%m/')
    filename = models.CharField(max_length=255)
""")
    with open(os.path.join(comm_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MessageThread, CaseMessage

@login_required
def thread_list(request):
    threads = request.user.message_threads.filter(is_deleted=False).select_related('case')
    return render(request, 'communications/thread_list.html', {'threads': threads})

@login_required
def thread_detail(request, pk):
    thread = get_object_or_404(MessageThread, pk=pk)
    messages = thread.messages.all().select_related('sender').order_by('created_at')
    return render(request, 'communications/thread_detail.html', {'thread': thread, 'messages': messages})
""")
    with open(os.path.join(comm_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'communications'

urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('<uuid:pk>/', views.thread_detail, name='thread_detail'),
]
""")
    with open(os.path.join(comm_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import MessageThread, CaseMessage, MessageAttachment

@admin.register(MessageThread)
class MessageThreadAdmin(admin.ModelAdmin):
    list_display = ['subject', 'case', 'is_active', 'created_at']

@admin.register(CaseMessage)
class CaseMessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'thread', 'is_read', 'created_at']
""")

    # -------------------------------------------------------------
    # 14. BILLING
    # -------------------------------------------------------------
    bill_dir = os.path.join(base_dir, "apps", "billing")
    os.makedirs(bill_dir, exist_ok=True)
    with open(os.path.join(bill_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Billing package\n")
    with open(os.path.join(bill_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class BillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.billing'
    verbose_name = 'Billing, Invoicing & Financial Ledger'
""")
    with open(os.path.join(bill_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class InvoiceStatus(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft'
    ISSUED = 'ISSUED', 'Issued'
    PARTIALLY_PAID = 'PARTIALLY_PAID', 'Partially Paid'
    PAID = 'PAID', 'Paid in Full'
    OVERDUE = 'OVERDUE', 'Overdue'
    CANCELLED = 'CANCELLED', 'Cancelled'

class BillableTimeEntry(AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='time_entries')
    advocate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='billable_hours')
    entry_date = models.DateField()
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_invoiced = models.BooleanField(default=False)

    @property
    def total_amount(self):
        return self.hours * self.hourly_rate

class CaseExpense(AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='expenses')
    expense_date = models.DateField()
    expense_category = models.CharField(max_length=50, choices=[('COURT_FEE', 'Court Filing Fee'), ('PROCESS_SERVER', 'Process Server / Summons Fee'), ('PRINTING', 'Photocopying & Printing'), ('EXPERT_WITNESS', 'Expert Witness Disbursement'), ('TRAVEL', 'Travel & Lodging'), ('MISC', 'Miscellaneous')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_reimbursable = models.BooleanField(default=True)
    is_invoiced = models.BooleanField(default=False)

class Invoice(UUIDModel, AuditTrackedModel):
    invoice_number = models.CharField(max_length=50, unique=True)
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='invoices')
    client = models.ForeignKey('clients.ClientProfile', on_delete=models.PROTECT, related_name='invoices')
    status = models.CharField(max_length=20, choices=InvoiceStatus.choices, default=InvoiceStatus.DRAFT)
    issue_date = models.DateField()
    due_date = models.DateField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    @property
    def balance_due(self):
        return self.total_amount - self.amount_paid

    def __str__(self):
        return f"{self.invoice_number} ({self.status})"

class InvoiceLineItem(AuditTrackedModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=1.0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)

class PaymentReceipt(UUIDModel, AuditTrackedModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    receipt_number = models.CharField(max_length=50, unique=True)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('BANK_TRANSFER', 'Bank Wire / NEFT / RTGS'), ('CHEQUE', 'Cheque / Demand Draft'), ('CARD', 'Credit / Debit Card'), ('CASH', 'Cash'), ('UPI', 'UPI / Instant Payment')])
    transaction_reference = models.CharField(max_length=100, blank=True, null=True)
""")
    with open(os.path.join(bill_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Invoice, BillableTimeEntry, CaseExpense

@login_required
def invoice_list(request):
    invoices = Invoice.objects.filter(is_deleted=False).select_related('case', 'client').order_by('-issue_date')
    if request.user.is_client():
        invoices = invoices.filter(client__user=request.user)
    return render(request, 'billing/invoice_list.html', {'invoices': invoices})

@login_required
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    items = invoice.items.all()
    payments = invoice.payments.all()
    return render(request, 'billing/invoice_detail.html', {'invoice': invoice, 'items': items, 'payments': payments})

@login_required
def time_entries_view(request):
    entries = BillableTimeEntry.objects.filter(is_deleted=False).select_related('case', 'advocate')
    return render(request, 'billing/time_entries.html', {'entries': entries})
""")
    with open(os.path.join(bill_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('time-entries/', views.time_entries_view, name='time_entries'),
    path('<uuid:pk>/', views.invoice_detail, name='invoice_detail'),
]
""")
    with open(os.path.join(bill_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import Invoice, InvoiceLineItem, BillableTimeEntry, CaseExpense, PaymentReceipt

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'case', 'client', 'status', 'total_amount', 'amount_paid', 'due_date']
    list_filter = ['status', 'due_date']

@admin.register(BillableTimeEntry)
class BillableTimeEntryAdmin(admin.ModelAdmin):
    list_display = ['case', 'advocate', 'entry_date', 'hours', 'hourly_rate', 'is_invoiced']

@admin.register(CaseExpense)
class CaseExpenseAdmin(admin.ModelAdmin):
    list_display = ['case', 'expense_category', 'amount', 'expense_date', 'is_invoiced']

@admin.register(PaymentReceipt)
class PaymentReceiptAdmin(admin.ModelAdmin):
    list_display = ['receipt_number', 'invoice', 'amount', 'payment_date', 'payment_method']
""")

    # -------------------------------------------------------------
    # 15. ORDERS & JUDGMENTS
    # -------------------------------------------------------------
    ord_dir = os.path.join(base_dir, "apps", "orders_judgments")
    os.makedirs(ord_dir, exist_ok=True)
    with open(os.path.join(ord_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Orders & Judgments package\n")
    with open(os.path.join(ord_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class OrdersJudgmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.orders_judgments'
    verbose_name = 'Orders, Judgments & Compliance Engine'
""")
    with open(os.path.join(ord_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
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
""")
    with open(os.path.join(ord_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CourtOrder, ComplianceItem

@login_required
def order_list(request):
    orders = CourtOrder.objects.filter(is_deleted=False).select_related('case', 'presiding_judge').order_by('-order_date')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(CourtOrder, pk=pk)
    compliance_items = order.compliance_items.all()
    return render(request, 'orders/order_detail.html', {'order': order, 'compliance_items': compliance_items})
""")
    with open(os.path.join(ord_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'orders_judgments'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<uuid:pk>/', views.order_detail, name='order_detail'),
]
""")
    with open(os.path.join(ord_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import CourtOrder, ComplianceItem

@admin.register(CourtOrder)
class CourtOrderAdmin(admin.ModelAdmin):
    list_display = ['case', 'order_type', 'order_date', 'presiding_judge', 'requires_compliance']
    list_filter = ['order_type', 'requires_compliance', 'order_date']

@admin.register(ComplianceItem)
class ComplianceItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'responsible_party', 'deadline', 'is_complied']
""")

    print("Completed Apps Part 3 generation.")

if __name__ == '__main__':
    generate_apps_part_3('.')
