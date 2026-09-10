from django.contrib import admin
from .models import Case, CaseType, OppositeParty, CaseAdvocateAssignment, CaseNote, CaseTimelineEvent

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ['case_number', 'title', 'case_type', 'status', 'priority', 'client', 'next_hearing_date']
    list_filter = ['status', 'priority', 'case_type']
    search_fields = ['case_number', 'title', 'cnr_number']

@admin.register(CaseType)
class CaseTypeAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category']

@admin.register(OppositeParty)
class OppositePartyAdmin(admin.ModelAdmin):
    list_display = ['name', 'case', 'advocate_name']

@admin.register(CaseAdvocateAssignment)
class CaseAdvocateAssignmentAdmin(admin.ModelAdmin):
    list_display = ['case', 'advocate', 'role_in_case', 'is_primary']

@admin.register(CaseNote)
class CaseNoteAdmin(admin.ModelAdmin):
    list_display = ['case', 'title', 'author', 'is_internal_only']

@admin.register(CaseTimelineEvent)
class CaseTimelineEventAdmin(admin.ModelAdmin):
    list_display = ['case', 'event_title', 'event_date']
