from django.contrib import admin
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
