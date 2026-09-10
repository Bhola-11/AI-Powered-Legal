from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Hearing, DailyBoard

@login_required
def hearing_list(request):
    hearings = Hearing.objects.filter(is_deleted=False).select_related('case', 'judge', 'courtroom').order_by('hearing_date')
    return render(request, 'hearings/hearing_list.html', {'hearings': hearings})

@login_required
def hearing_detail(request, pk):
    hearing = get_object_or_404(Hearing, pk=pk)
    return render(request, 'hearings/hearing_detail.html', {'hearing': hearing})

@login_required
def daily_board_view(request):
    boards = DailyBoard.objects.all().order_by('-board_date')
    return render(request, 'hearings/daily_board.html', {'boards': boards})

@login_required
def calendar_view(request):
    return render(request, 'hearings/calendar.html')
