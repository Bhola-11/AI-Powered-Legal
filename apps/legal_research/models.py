from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class StatutoryAct(AuditTrackedModel):
    title = models.CharField(max_length=255, unique=True)
    act_number = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    preamble = models.TextField(blank=True, null=True)
    jurisdiction = models.CharField(max_length=100, default='National')

    def __str__(self):
        return f"{self.title} ({self.year})"

class StatutorySection(AuditTrackedModel):
    act = models.ForeignKey(StatutoryAct, on_delete=models.CASCADE, related_name='sections')
    section_number = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    content = models.TextField()
    explanations = models.TextField(blank=True, null=True)
    punishment_or_remedy = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Sec. {self.section_number} - {self.act.title}"

class CasePrecedent(UUIDModel, AuditTrackedModel):
    citation = models.CharField(max_length=150, unique=True, db_index=True)
    case_name = models.CharField(max_length=300)
    court = models.CharField(max_length=150)
    judgment_date = models.DateField()
    bench = models.CharField(max_length=255, blank=True, null=True)
    headnotes = models.TextField()
    ratio_decidendi = models.TextField()
    legal_principles = models.TextField()
    is_landmark = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.case_name} [{self.citation}]"

class ResearchNotebook(AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='research_notes', null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    associated_precedents = models.ManyToManyField(CasePrecedent, blank=True)
    associated_sections = models.ManyToManyField(StatutorySection, blank=True)

    def __str__(self):
        return self.title
