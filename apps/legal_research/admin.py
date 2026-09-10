from django.contrib import admin
from .models import StatutoryAct, StatutorySection, CasePrecedent, ResearchNotebook

@admin.register(StatutoryAct)
class StatutoryActAdmin(admin.ModelAdmin):
    list_display = ['title', 'act_number', 'year', 'jurisdiction']

@admin.register(StatutorySection)
class StatutorySectionAdmin(admin.ModelAdmin):
    list_display = ['section_number', 'title', 'act']
    search_fields = ['section_number', 'title', 'content']

@admin.register(CasePrecedent)
class CasePrecedentAdmin(admin.ModelAdmin):
    list_display = ['citation', 'case_name', 'court', 'judgment_date', 'is_landmark']
    search_fields = ['citation', 'case_name', 'ratio_decidendi']
    list_filter = ['is_landmark', 'court']

@admin.register(ResearchNotebook)
class ResearchNotebookAdmin(admin.ModelAdmin):
    list_display = ['title', 'case', 'author']
