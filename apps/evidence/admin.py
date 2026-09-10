from django.contrib import admin
from .models import EvidenceItem, ChainOfCustodyLog, WitnessEvidenceLink

@admin.register(EvidenceItem)
class EvidenceItemAdmin(admin.ModelAdmin):
    list_display = ['item_code', 'title', 'case', 'category', 'admissibility_status', 'exhibit_mark']
    list_filter = ['category', 'admissibility_status']
    search_fields = ['item_code', 'title', 'exhibit_mark']

@admin.register(ChainOfCustodyLog)
class ChainOfCustodyLogAdmin(admin.ModelAdmin):
    list_display = ['evidence', 'transferred_from', 'transferred_to', 'transfer_date']
