from django.shortcuts import render, get_object_or_404
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
