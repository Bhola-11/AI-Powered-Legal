from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class EvidenceCategory(models.TextChoices):
    DOCUMENTARY = 'DOCUMENTARY', 'Documentary Evidence'
    ELECTRONIC = 'ELECTRONIC', 'Electronic / Digital Record'
    PHYSICAL = 'PHYSICAL', 'Physical / Forensic Material'
    TESTIMONIAL = 'TESTIMONIAL', 'Deposition / Witness Statement'

class EvidenceItem(UUIDModel, AuditTrackedModel):
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='evidence_items')
    item_code = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=30, choices=EvidenceCategory.choices, default=EvidenceCategory.DOCUMENTARY)
    description = models.TextField()
    source_origin = models.CharField(max_length=255, help_text="Where and from whom obtained")
    collection_date = models.DateField()
    current_custodian = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='held_evidence')
    custody_location = models.CharField(max_length=255, default='Law Firm Vault')
    admissibility_status = models.CharField(max_length=30, default='SUBMITTED', choices=[('SUBMITTED', 'Submitted'), ('MARKED_EXHIBIT', 'Marked as Exhibit'), ('OBJECTED', 'Objected by Adverse Party'), ('ADMITTED', 'Admitted in Evidence'), ('REJECTED', 'Rejected by Court')])
    exhibit_mark = models.CharField(max_length=30, blank=True, null=True, help_text="e.g. Ex. P-1 or Ex. D-2")

    def __str__(self):
        return f"[{self.item_code}] {self.title}"

class ChainOfCustodyLog(AuditTrackedModel):
    evidence = models.ForeignKey(EvidenceItem, on_delete=models.CASCADE, related_name='custody_logs')
    transferred_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='custody_transfers_sent')
    transferred_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='custody_transfers_received')
    transfer_date = models.DateTimeField(auto_now_add=True)
    purpose_of_transfer = models.TextField()
    security_seal_number = models.CharField(max_length=100, blank=True, null=True)

class WitnessEvidenceLink(AuditTrackedModel):
    evidence = models.ForeignKey(EvidenceItem, on_delete=models.CASCADE, related_name='witness_links')
    witness_name = models.CharField(max_length=255)
    statement_summary = models.TextField()
