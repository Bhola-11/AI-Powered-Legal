from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import TimeStampedModel

class Role(models.TextChoices):
    SUPER_ADMIN = 'SUPER_ADMIN', 'Super Admin'
    FIRM_ADMIN = 'FIRM_ADMIN', 'Law Firm Admin'
    LAWYER = 'LAWYER', 'Advocate / Lawyer'
    PARALEGAL = 'PARALEGAL', 'Paralegal / Legal Assistant'
    CLIENT = 'CLIENT', 'Client'

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CLIENT, db_index=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    bar_council_enrollment_no = models.CharField(max_length=50, blank=True, null=True, help_text="Bar Council Enrollment Number for Advocates")
    law_firm = models.ForeignKey('firms.LawFirm', on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    is_verified = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def is_super_admin(self):
        return self.role == Role.SUPER_ADMIN or self.is_superuser

    def is_firm_admin(self):
        return self.role == Role.FIRM_ADMIN

    def is_lawyer(self):
        return self.role == Role.LAWYER

    def is_paralegal(self):
        return self.role == Role.PARALEGAL

    def is_client(self):
        return self.role == Role.CLIENT

class UserProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=255, blank=True, null=True, help_text="e.g. Civil Litigation, Criminal Defense, Corporate Law")
    years_of_experience = models.PositiveIntegerField(default=0)
    chamber_address = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.get_full_name() or self.user.username}"
