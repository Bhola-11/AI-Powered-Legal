from django.contrib import admin
from .models import Hearing, DailyBoard

@admin.register(Hearing)
class HearingAdmin(admin.ModelAdmin):
    list_display = ['case', 'hearing_date', 'start_time', 'hearing_type', 'judge', 'is_completed']
    list_filter = ['hearing_type', 'is_completed', 'hearing_date']

@admin.register(DailyBoard)
class DailyBoardAdmin(admin.ModelAdmin):
    list_display = ['board_date', 'court_complex', 'total_matters']
