from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CourtComplex, CourtRoom, Judge, Bench

@login_required
def court_list(request):
    courts = CourtComplex.objects.all().order_by('state', 'name')
    return render(request, 'courts/court_list.html', {'courts': courts})

@login_required
def judge_list(request):
    judges = Judge.objects.filter(is_active=True).select_related('court_complex', 'assigned_courtroom')
    return render(request, 'courts/judge_list.html', {'judges': judges})

@login_required
def courtroom_schedule(request, pk):
    room = get_object_or_404(CourtRoom, pk=pk)
    return render(request, 'courts/courtroom_schedule.html', {'room': room})
