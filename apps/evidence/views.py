from django.shortcuts import render, get_object_or_404
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
