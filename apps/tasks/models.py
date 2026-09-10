from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class TaskStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    BLOCKED = 'BLOCKED', 'Blocked'
    COMPLETED = 'COMPLETED', 'Completed'
    CANCELLED = 'CANCELLED', 'Cancelled'

class TaskPriority(models.TextChoices):
    CRITICAL = 'CRITICAL', 'Critical'
    HIGH = 'HIGH', 'High'
    MEDIUM = 'MEDIUM', 'Medium'
    LOW = 'LOW', 'Low'

class WorkflowStage(AuditTrackedModel):
    name = models.CharField(max_length=100)
    stage_order = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.stage_order}. {self.name}"

class CaseTask(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='tasks')
    hearing = models.ForeignKey('hearings.Hearing', on_delete=models.SET_NULL, null=True, blank=True, related_name='followup_tasks')
    workflow_stage = models.ForeignKey(WorkflowStage, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='assigned_tasks')
    priority = models.CharField(max_length=20, choices=TaskPriority.choices, default=TaskPriority.MEDIUM)
    status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.PENDING, db_index=True)
    due_date = models.DateField(db_index=True)
    completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"[{self.status}] {self.title}"

class TaskChecklist(AuditTrackedModel):
    task = models.ForeignKey(CaseTask, on_delete=models.CASCADE, related_name='checklists')
    item_title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
