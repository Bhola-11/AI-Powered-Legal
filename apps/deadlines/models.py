from django.db import models
from django.utils import timezone
from apps.core.models import AuditTrackedModel, UUIDModel

class DeadlineType(models.TextChoices):
    STATUTORY_LIMITATION = 'STATUTORY_LIMITATION', 'Statutory Limitation Date'
    COURT_FILING = 'COURT_FILING', 'Court Filing Deadline'
    WRITTEN_STATEMENT = 'WRITTEN_STATEMENT', 'Written Statement / Reply Deadline'
    COMPLIANCE = 'COMPLIANCE', 'Court Order Compliance Deadline'
    APPEAL_PERIOD = 'APPEAL_PERIOD', 'Limitation for Appeal / Review'
    DISCOVERY = 'DISCOVERY', 'Discovery / Interrogatories Response'

class CaseDeadline(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='deadlines')
    title = models.CharField(max_length=255)
    deadline_type = models.CharField(max_length=30, choices=DeadlineType.choices, default=DeadlineType.COURT_FILING)
    due_date = models.DateField(db_index=True)
    statutory_provision = models.CharField(max_length=255, blank=True, null=True, help_text="e.g. Limitation Act Art. 113 or CPC O.VIII R.1")
    is_statutory = models.BooleanField(default=False)
    is_met = models.BooleanField(default=False)
    met_at = models.DateTimeField(null=True, blank=True)
    reminder_days_before = models.CharField(max_length=50, default="30,15,7,2,1")

    def __str__(self):
        return f"{self.title} ({self.due_date})"

    @property
    def is_overdue(self):
        return not self.is_met and self.due_date < timezone.now().date()
