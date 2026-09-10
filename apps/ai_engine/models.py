from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class AIQueryLog(UUIDModel, AuditTrackedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ai_queries')
    query_type = models.CharField(max_length=50, choices=[('SUMMARY', 'Case Summary'), ('DRAFTING', 'Petition Drafting'), ('CONFLICT', 'Conflict Check'), ('PRECEDENT', 'Precedent Matching')])
    input_prompt = models.TextField()
    generated_output = models.TextField()
    latency_ms = models.PositiveIntegerField(default=120)

    def __str__(self):
        return f"AI [{self.query_type}] by {self.user.username}"
