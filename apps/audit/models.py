import hashlib
from django.db import models
from django.conf import settings
from apps.core.models import TimeStampedModel, UUIDModel

class AuditAction(models.TextChoices):
    LOGIN = 'LOGIN', 'User Login'
    LOGOUT = 'LOGOUT', 'User Logout'
    CASE_CREATED = 'CASE_CREATED', 'Case Created'
    CASE_STATUS_CHANGED = 'CASE_STATUS_CHANGED', 'Case Status Changed'
    DOCUMENT_UPLOADED = 'DOCUMENT_UPLOADED', 'Document Uploaded'
    DOCUMENT_DOWNLOADED = 'DOCUMENT_DOWNLOADED', 'Document Downloaded'
    EVIDENCE_MUTATED = 'EVIDENCE_MUTATED', 'Evidence Modified'
    ORDER_RECORDED = 'ORDER_RECORDED', 'Court Order Recorded'
    INVOICE_GENERATED = 'INVOICE_GENERATED', 'Invoice Generated'
    PAYMENT_RECORDED = 'PAYMENT_RECORDED', 'Payment Recorded'
    SECURITY_ALERT = 'SECURITY_ALERT', 'Security Violation Attempt'

class AuditLog(UUIDModel, TimeStampedModel):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_actions')
    action = models.CharField(max_length=50, choices=AuditAction.choices, db_index=True)
    entity_name = models.CharField(max_length=100)
    entity_id = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, null=True)
    description = models.TextField()
    prev_hash = models.CharField(max_length=64, blank=True, null=True)
    block_hash = models.CharField(max_length=64, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.block_hash:
            last = AuditLog.objects.order_by('-created_at').first()
            self.prev_hash = last.block_hash if last else '0' * 64
            hasher = hashlib.sha256()
            hasher.update(f"{self.prev_hash}:{self.action}:{self.entity_id}:{self.description}".encode('utf-8'))
            self.block_hash = hasher.hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.action}] {self.entity_name} ({self.created_at})"
