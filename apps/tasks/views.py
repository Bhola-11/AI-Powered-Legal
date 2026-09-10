from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CaseTask, WorkflowStage

@login_required
def task_list(request):
    tasks = CaseTask.objects.filter(is_deleted=False).select_related('case', 'assignee')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def kanban_view(request):
    tasks = CaseTask.objects.filter(is_deleted=False).select_related('case', 'assignee')
    return render(request, 'tasks/kanban.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(CaseTask, pk=pk)
    checklists = task.checklists.all()
    return render(request, 'tasks/detail.html', {'task': task, 'checklists': checklists})
