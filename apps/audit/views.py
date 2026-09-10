from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.core.permissions import role_required
from .models import AuditLog

@login_required
@role_required('SUPER_ADMIN', 'FIRM_ADMIN')
def audit_log_view(request):
    logs = AuditLog.objects.all().order_by('-created_at')[:100]
    return render(request, 'audit/logs.html', {'logs': logs})
