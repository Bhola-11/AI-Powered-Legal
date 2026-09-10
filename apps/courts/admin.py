from django.contrib import admin
from .models import CourtComplex, CourtRoom, Judge, Bench

@admin.register(CourtComplex)
class CourtComplexAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'city', 'state', 'total_courtrooms']
    list_filter = ['level', 'state']
    search_fields = ['name', 'city']

@admin.register(CourtRoom)
class CourtRoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'court_complex', 'floor', 'has_video_conferencing']

@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'court_complex', 'assigned_courtroom', 'is_active']
    search_fields = ['name']

@admin.register(Bench)
class BenchAdmin(admin.ModelAdmin):
    list_display = ['name', 'court_complex', 'bench_type']
