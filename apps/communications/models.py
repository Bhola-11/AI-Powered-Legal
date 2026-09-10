from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class MessageThread(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='communication_threads')
    subject = models.CharField(max_length=255)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='message_threads')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.subject} ({self.case.case_number})"

class CaseMessage(UUIDModel, AuditTrackedModel):
    thread = models.ForeignKey(MessageThread, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Msg from {self.sender.username} at {self.created_at}"

class MessageAttachment(AuditTrackedModel):
    message = models.ForeignKey(CaseMessage, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='message_attachments/%Y/%m/')
    filename = models.CharField(max_length=255)
