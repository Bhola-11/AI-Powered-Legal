from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import LawFirm, BranchOffice, PracticeArea

@login_required
def firm_detail(request, pk):
    firm = get_object_or_404(LawFirm, pk=pk)
    branches = firm.branches.all()
    practice_areas = firm.practice_areas.all()
    members = firm.members.all()
    return render(request, 'firms/firm_detail.html', {
        'firm': firm,
        'branches': branches,
        'practice_areas': practice_areas,
        'members': members,
    })

@login_required
def branch_list(request):
    branches = BranchOffice.objects.all()
    return render(request, 'firms/branch_list.html', {'branches': branches})
