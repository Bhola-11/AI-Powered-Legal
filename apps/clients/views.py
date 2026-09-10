from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ClientProfile, KYCVerification, ConflictCheckResult

@login_required
def client_list(request):
    clients = ClientProfile.objects.filter(is_deleted=False)
    return render(request, 'clients/client_list.html', {'clients': clients})

@login_required
def client_detail(request, pk):
    client = get_object_or_404(ClientProfile, pk=pk)
    kyc_records = client.kyc_records.all()
    return render(request, 'clients/client_detail.html', {'client': client, 'kyc_records': kyc_records})

@login_required
def conflict_check_view(request):
    results = ConflictCheckResult.objects.all().order_by('-created_at')[:20]
    return render(request, 'clients/conflict_check.html', {'results': results})
