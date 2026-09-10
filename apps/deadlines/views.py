from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CaseDeadline

@login_required
def deadline_list(request):
    deadlines = CaseDeadline.objects.filter(is_deleted=False).select_related('case').order_by('due_date')
    return render(request, 'deadlines/list.html', {'deadlines': deadlines})

@login_required
def limitation_calculator_view(request):
    return render(request, 'deadlines/limitation_calculator.html')
