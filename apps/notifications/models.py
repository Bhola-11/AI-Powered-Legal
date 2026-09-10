from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class NotificationType(models.TextChoices):
    CASE_ASSIGNED = 'CASE_ASSIGNED', 'New Case Assignment'
    HEARING_SCHEDULED = 'HEARING_SCHEDULED', 'Hearing Scheduled'
    HEARING_CHANGED = 'HEARING_CHANGED', 'Hearing Rescheduled / Postponed'
    DEADLINE_APPROACHING = 'DEADLINE_APPROACHING', 'Deadline Approaching'
    DEADLINE_OVERDUE = 'DEADLINE_OVERDUE', 'Deadline Overdue'
    DOCUMENT_UPLOADED = 'DOCUMENT_UPLOADED', 'New Document Uploaded'
    TASK_ASSIGNED = 'TASK_ASSIGNED', 'Task Assigned'
    ORDER_PASSED = 'ORDER_PASSED', 'Court Order Passed'
    INVOICE_GENERATED = 'INVOICE_GENERATED', 'Invoice Generated'
    PAYMENT_RECEIVED = 'PAYMENT_RECEIVED', 'Payment Received'

class Notification(UUIDModel, AuditTrackedModel):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    notification_type = models.CharField(max_length=30, choices=NotificationType.choices, default=NotificationType.CASE_ASSIGNED)
    title = models.CharField(max_length=255)
    message = models.TextField()
    action_url = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.BooleanField(default=False, db_index=True)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} -> {self.recipient.username}"
