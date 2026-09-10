from django.contrib import admin
from .models import CaseTask, WorkflowStage, TaskChecklist

@admin.register(CaseTask)
class CaseTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'case', 'assignee', 'priority', 'status', 'due_date']
    list_filter = ['status', 'priority', 'due_date']

@admin.register(WorkflowStage)
class WorkflowStageAdmin(admin.ModelAdmin):
    list_display = ['stage_order', 'name']

@admin.register(TaskChecklist)
class TaskChecklistAdmin(admin.ModelAdmin):
    list_display = ['item_title', 'task', 'is_completed']
