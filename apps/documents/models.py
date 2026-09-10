import hashlib
from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class DocumentCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class LegalDocument(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='documents')
    category = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True, related_name='documents')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='legal_docs/%Y/%m/')
    file_sha256 = models.CharField(max_length=64, blank=True, null=True, help_text="Cryptographic integrity hash")
    file_size_bytes = models.BigIntegerField(default=0)
    current_version = models.PositiveIntegerField(default=1)
    is_client_visible = models.BooleanField(default=False)
    is_confidential = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (v{self.current_version})"

    def compute_hash(self):
        if self.file:
            sha = hashlib.sha256()
            for chunk in self.file.chunks():
                sha.update(chunk)
            self.file_sha256 = sha.hexdigest()

class DocumentVersion(AuditTrackedModel):
    document = models.ForeignKey(LegalDocument, on_delete=models.CASCADE, related_name='versions')
    version_number = models.PositiveIntegerField()
    file = models.FileField(upload_to='legal_docs/versions/')
    file_sha256 = models.CharField(max_length=64)
    change_notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('document', 'version_number')
