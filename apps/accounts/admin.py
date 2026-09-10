from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('CivicLaw Details', {'fields': ('role', 'phone_number', 'bar_council_enrollment_no', 'law_firm', 'is_verified')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'law_firm', 'is_verified', 'is_staff']
    list_filter = ['role', 'is_verified', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'bar_council_enrollment_no']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialization', 'years_of_experience']
    search_fields = ['user__username', 'specialization']
