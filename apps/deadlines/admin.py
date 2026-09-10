from django.contrib import admin
from .models import CaseDeadline

@admin.register(CaseDeadline)
class CaseDeadlineAdmin(admin.ModelAdmin):
    list_display = ['title', 'case', 'deadline_type', 'due_date', 'is_statutory', 'is_met']
    list_filter = ['deadline_type', 'is_statutory', 'is_met', 'due_date']
