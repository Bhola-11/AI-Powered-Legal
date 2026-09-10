from django.db import models
from apps.core.models import AuditTrackedModel

class CourtLevel(models.TextChoices):
    SUPREME_COURT = 'SUPREME_COURT', 'Supreme Court of India'
    HIGH_COURT = 'HIGH_COURT', 'High Court'
    DISTRICT_COURT = 'DISTRICT_COURT', 'District & Sessions Court'
    TRIBUNAL = 'TRIBUNAL', 'Special Tribunal (NCLT/DRT/CAT)'
    MAGISTRATE_COURT = 'MAGISTRATE_COURT', 'Magistrate Court'

class CourtComplex(AuditTrackedModel):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=30, choices=CourtLevel.choices, default=CourtLevel.DISTRICT_COURT)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    total_courtrooms = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"

class CourtRoom(AuditTrackedModel):
    court_complex = models.ForeignKey(CourtComplex, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=50)
    floor = models.CharField(max_length=20, default='Ground')
    has_video_conferencing = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(default=50)

    def __str__(self):
        return f"Room {self.room_number} - {self.court_complex.name}"

class Judge(AuditTrackedModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=100, default='Hon’ble Justice')
    court_complex = models.ForeignKey(CourtComplex, on_delete=models.CASCADE, related_name='judges')
    assigned_courtroom = models.ForeignKey(CourtRoom, on_delete=models.SET_NULL, null=True, blank=True)
    specialization = models.CharField(max_length=255, blank=True, null=True, help_text="e.g. Constitutional Bench, Commercial Division")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} {self.name}"

class Bench(AuditTrackedModel):
    name = models.CharField(max_length=255)
    court_complex = models.ForeignKey(CourtComplex, on_delete=models.CASCADE, related_name='benches')
    bench_type = models.CharField(max_length=50, choices=[('SINGLE', 'Single Judge Bench'), ('DIVISION', 'Division Bench'), ('FULL', 'Full Bench'), ('CONSTITUTION', 'Constitution Bench')])
    presiding_judges = models.ManyToManyField(Judge, related_name='benches')

    def __str__(self):
        return f"{self.name} - {self.court_complex.name}"
