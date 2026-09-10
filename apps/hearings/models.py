from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class HearingType(models.TextChoices):
    ADMISSION = 'ADMISSION', 'Admission Hearing'
    FRAME_ISSUES = 'FRAME_ISSUES', 'Framing of Issues'
    EVIDENCE = 'EVIDENCE', 'Evidence & Witness Cross-Examination'
    INTERIM_RELIEF = 'INTERIM_RELIEF', 'Interim Relief / Injunction'
    FINAL_ARGUMENTS = 'FINAL_ARGUMENTS', 'Final Arguments'
    JUDGMENT = 'JUDGMENT', 'Pronouncement of Judgment'
    MISCELLANEOUS = 'MISCELLANEOUS', 'Miscellaneous / Compliance'

class Hearing(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='hearings')
    hearing_date = models.DateField(db_index=True)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    courtroom = models.ForeignKey('courts.CourtRoom', on_delete=models.SET_NULL, null=True, blank=True)
    judge = models.ForeignKey('courts.Judge', on_delete=models.SET_NULL, null=True, blank=True)
    hearing_type = models.CharField(max_length=30, choices=HearingType.choices, default=HearingType.ADMISSION)
    purpose = models.TextField()
    attending_advocate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    attendance_recorded = models.BooleanField(default=False)
    outcome_summary = models.TextField(blank=True, null=True)
    next_hearing_date = models.DateField(null=True, blank=True)
    interim_orders_passed = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Hearing for {self.case.case_number} on {self.hearing_date}"

class DailyBoard(AuditTrackedModel):
    board_date = models.DateField(unique=True)
    court_complex = models.ForeignKey('courts.CourtComplex', on_delete=models.CASCADE, related_name='daily_boards')
    total_matters = models.PositiveIntegerField(default=0)
    board_file = models.FileField(upload_to='cause_lists/', null=True, blank=True)

    def __str__(self):
        return f"Daily Board - {self.court_complex.name} ({self.board_date})"
