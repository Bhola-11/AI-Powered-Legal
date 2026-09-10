from django.shortcuts import render, get_object_or_404, redirect
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
