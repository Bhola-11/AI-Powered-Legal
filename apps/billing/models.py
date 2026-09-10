from django.db import models
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
