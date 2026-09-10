from django.shortcuts import render
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
