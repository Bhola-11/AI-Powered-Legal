# scripts/generators/gen_apps_1.py
import os

def generate_apps_part_1(base_dir):
    print("Generating Apps Part 1: core, accounts, firms, clients, courts...")
    
    # -------------------------------------------------------------
    # 1. CORE
    # -------------------------------------------------------------
    core_dir = os.path.join(base_dir, "apps", "core")
    os.makedirs(core_dir, exist_ok=True)
    with open(os.path.join(core_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Core package\n")
    with open(os.path.join(core_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'Core System Infrastructure'
""")
    with open(os.path.join(core_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False, db_index=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=['is_deleted', 'deleted_at'])

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save(update_fields=['is_deleted', 'deleted_at'])

class AuditTrackedModel(TimeStampedModel, SoftDeleteModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created",
        help_text="User who created this record"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated",
        help_text="User who last updated this record"
    )

    class Meta:
        abstract = True
""")
    with open(os.path.join(core_dir, "middleware.py"), "w", encoding="utf-8") as f:
        f.write("""import time
import uuid
from django.utils.deprecation import MiddlewareMixin

class AuditMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.request_id = str(uuid.uuid4())
        request.start_time = time.time()
        
    def process_response(self, request, response):
        duration = time.time() - getattr(request, 'start_time', time.time())
        response['X-Request-ID'] = getattr(request, 'request_id', 'unknown')
        response['X-Response-Time-Ms'] = str(round(duration * 1000, 2))
        return response

class TenantContextMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            request.firm = getattr(request.user, 'law_firm', None)
        else:
            request.firm = None
""")
    with open(os.path.join(core_dir, "permissions.py"), "w", encoding="utf-8") as f:
        f.write("""from functools import wraps
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import AccessMixin

def role_required(*allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied("Authentication required.")
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            if hasattr(request.user, 'role') and request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied("You do not have the required role to access this resource.")
        return _wrapped_view
    return decorator

class RoleRequiredMixin(AccessMixin):
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        if hasattr(request.user, 'role') and request.user.role in self.allowed_roles:
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()
""")
    with open(os.path.join(core_dir, "context_processors.py"), "w", encoding="utf-8") as f:
        f.write("""from django.conf import settings

def civiclaw_context(request):
    return {
        'PLATFORM_NAME': getattr(settings, 'CIVICLAW_PLATFORM_NAME', 'CivicLaw Enterprise'),
        'PLATFORM_TAGLINE': getattr(settings, 'CIVICLAW_PLATFORM_TAGLINE', 'AI-Powered Legal Suite'),
        'PLATFORM_VERSION': getattr(settings, 'CIVICLAW_VERSION', '2.4.0'),
        'current_user_role': getattr(request.user, 'role', 'GUEST') if request.user.is_authenticated else 'ANONYMOUS',
    }
""")
    os.makedirs(os.path.join(core_dir, "templatetags"), exist_ok=True)
    with open(os.path.join(core_dir, "templatetags", "__init__.py"), "w", encoding="utf-8") as f:
        f.write("")
    with open(os.path.join(core_dir, "templatetags", "civiclaw_tags.py"), "w", encoding="utf-8") as f:
        f.write("""from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def status_badge(status):
    badge_map = {
        'DRAFT': 'badge-secondary',
        'INTAKE': 'badge-info',
        'ACTIVE': 'badge-primary',
        'HEARING_SCHEDULED': 'badge-warning',
        'JUDGMENT_RESERVED': 'badge-dark',
        'DISPOSED': 'badge-success',
        'CLOSED': 'badge-secondary',
        'PAID': 'badge-success',
        'OVERDUE': 'badge-danger',
        'PENDING': 'badge-warning',
    }
    cls = badge_map.get(str(status).upper(), 'badge-light')
    return mark_safe(f'<span class="badge {cls}">{status}</span>')

@register.filter
def priority_badge(priority):
    p_map = {
        'CRITICAL': 'badge-danger',
        'HIGH': 'badge-warning',
        'MEDIUM': 'badge-info',
        'LOW': 'badge-secondary',
    }
    cls = p_map.get(str(priority).upper(), 'badge-light')
    return mark_safe(f'<span class="badge {cls}">{priority}</span>')
""")

    # -------------------------------------------------------------
    # 2. ACCOUNTS
    # -------------------------------------------------------------
    acc_dir = os.path.join(base_dir, "apps", "accounts")
    os.makedirs(acc_dir, exist_ok=True)
    with open(os.path.join(acc_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Accounts package\n")
    with open(os.path.join(acc_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
    verbose_name = 'User Accounts & Access Control'
""")
    with open(os.path.join(acc_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
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
""")
    with open(os.path.join(acc_dir, "forms.py"), "w", encoding="utf-8") as f:
        f.write("""from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, UserProfile, Role

class CivicLawLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username or Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class CivicLawRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=Role.choices, widget=forms.Select(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    bar_council_enrollment_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'If applicable'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'phone_number', 'bar_council_enrollment_no']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'specialization', 'years_of_experience', 'chamber_address', 'emergency_contact']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamber_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),
        }
""")
    with open(os.path.join(acc_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from .models import User, UserProfile, Role
from .forms import CivicLawLoginForm, CivicLawRegistrationForm, UserProfileForm

class CivicLawLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CivicLawLoginForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('accounts:dashboard_redirect')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

class CivicLawRegisterView(CreateView):
    model = User
    form_class = CivicLawRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        return response

@login_required
def dashboard_redirect(request):
    user = request.user
    if user.is_superuser or user.role == Role.SUPER_ADMIN:
        return redirect('accounts:super_admin_dashboard')
    elif user.role == Role.FIRM_ADMIN:
        return redirect('accounts:firm_admin_dashboard')
    elif user.role == Role.LAWYER:
        return redirect('accounts:lawyer_dashboard')
    elif user.role == Role.PARALEGAL:
        return redirect('accounts:paralegal_dashboard')
    elif user.role == Role.CLIENT:
        return redirect('accounts:client_dashboard')
    return redirect('accounts:login')

@login_required
def super_admin_dashboard(request):
    return render(request, 'dashboards/super_admin.html')

@login_required
def firm_admin_dashboard(request):
    return render(request, 'dashboards/firm_admin.html')

@login_required
def lawyer_dashboard(request):
    return render(request, 'dashboards/lawyer.html')

@login_required
def paralegal_dashboard(request):
    return render(request, 'dashboards/paralegal.html')

@login_required
def client_dashboard(request):
    return render(request, 'dashboards/client.html')

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})
""")
    with open(os.path.join(acc_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CivicLawLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.CivicLawRegisterView.as_view(), name='register'),
    path('redirect/', views.dashboard_redirect, name='dashboard_redirect'),
    path('dashboard/super-admin/', views.super_admin_dashboard, name='super_admin_dashboard'),
    path('dashboard/firm-admin/', views.firm_admin_dashboard, name='firm_admin_dashboard'),
    path('dashboard/lawyer/', views.lawyer_dashboard, name='lawyer_dashboard'),
    path('dashboard/paralegal/', views.paralegal_dashboard, name='paralegal_dashboard'),
    path('dashboard/client/', views.client_dashboard, name='client_dashboard'),
    path('profile/', views.profile_view, name='profile'),
]
""")
    with open(os.path.join(acc_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
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
""")

    # -------------------------------------------------------------
    # 3. FIRMS
    # -------------------------------------------------------------
    firm_dir = os.path.join(base_dir, "apps", "firms")
    os.makedirs(firm_dir, exist_ok=True)
    with open(os.path.join(firm_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Firms package\n")
    with open(os.path.join(firm_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class FirmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.firms'
    verbose_name = 'Law Firm & Practice Management'
""")
    with open(os.path.join(firm_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from apps.core.models import AuditTrackedModel, UUIDModel

class LawFirm(UUIDModel, AuditTrackedModel):
    name = models.CharField(max_length=255, unique=True)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    tax_id = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    website = models.URLField(blank=True, null=True)
    primary_office_address = models.TextField()
    is_active = models.BooleanField(default=True)
    max_lawyers = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.name

class BranchOffice(AuditTrackedModel):
    firm = models.ForeignKey(LawFirm, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField()
    contact_phone = models.CharField(max_length=30)
    is_headquarters = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.firm.name}"

class PracticeArea(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    firms = models.ManyToManyField(LawFirm, related_name='practice_areas', blank=True)

    def __str__(self):
        return self.name

class FirmSetting(AuditTrackedModel):
    firm = models.OneToOneField(LawFirm, on_delete=models.CASCADE, related_name='settings')
    invoice_prefix = models.CharField(max_length=10, default="INV-")
    default_hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=250.00)
    tax_rate_percent = models.DecimalField(max_digits=5, decimal_places=2, default=18.00)
    enable_client_portal = models.BooleanField(default=True)
    automatic_reminders = models.BooleanField(default=True)

    def __str__(self):
        return f"Settings for {self.firm.name}"
""")
    with open(os.path.join(firm_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import LawFirm, BranchOffice, PracticeArea

@login_required
def firm_detail(request, pk):
    firm = get_object_or_404(LawFirm, pk=pk)
    branches = firm.branches.all()
    practice_areas = firm.practice_areas.all()
    members = firm.members.all()
    return render(request, 'firms/firm_detail.html', {
        'firm': firm,
        'branches': branches,
        'practice_areas': practice_areas,
        'members': members,
    })

@login_required
def branch_list(request):
    branches = BranchOffice.objects.all()
    return render(request, 'firms/branch_list.html', {'branches': branches})
""")
    with open(os.path.join(firm_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'firms'

urlpatterns = [
    path('<uuid:pk>/', views.firm_detail, name='firm_detail'),
    path('branches/', views.branch_list, name='branch_list'),
]
""")
    with open(os.path.join(firm_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import LawFirm, BranchOffice, PracticeArea, FirmSetting

@admin.register(LawFirm)
class LawFirmAdmin(admin.ModelAdmin):
    list_display = ['name', 'registration_number', 'email', 'phone', 'is_active']
    search_fields = ['name', 'registration_number']

@admin.register(BranchOffice)
class BranchOfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'firm', 'city', 'state', 'is_headquarters']
    list_filter = ['is_headquarters', 'state']

@admin.register(PracticeArea)
class PracticeAreaAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(FirmSetting)
class FirmSettingAdmin(admin.ModelAdmin):
    list_display = ['firm', 'invoice_prefix', 'default_hourly_rate', 'tax_rate_percent']
""")

    # -------------------------------------------------------------
    # 4. CLIENTS
    # -------------------------------------------------------------
    cli_dir = os.path.join(base_dir, "apps", "clients")
    os.makedirs(cli_dir, exist_ok=True)
    with open(os.path.join(cli_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Clients package\n")
    with open(os.path.join(cli_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class ClientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.clients'
    verbose_name = 'Client Management & Verification'
""")
    with open(os.path.join(cli_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from django.conf import settings
from apps.core.models import AuditTrackedModel, UUIDModel

class ClientType(models.TextChoices):
    INDIVIDUAL = 'INDIVIDUAL', 'Individual Person'
    CORPORATE = 'CORPORATE', 'Corporate Enterprise'
    GOVERNMENT = 'GOVERNMENT', 'Government Entity'
    NGO = 'NGO', 'Non-Profit Organization'

class ClientProfile(UUIDModel, AuditTrackedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_profile', null=True, blank=True)
    client_type = models.CharField(max_length=20, choices=ClientType.choices, default=ClientType.INDIVIDUAL)
    display_name = models.CharField(max_length=255, db_index=True)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    tax_id_or_pan = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    billing_address = models.TextField()
    is_verified = models.BooleanField(default=False)
    conflict_check_cleared = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.display_name

class KYCVerification(AuditTrackedModel):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='kyc_records')
    document_type = models.CharField(max_length=100, help_text="Passport, National ID, Certificate of Incorporation")
    document_number = models.CharField(max_length=100)
    verified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='PENDING', choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')])
    remarks = models.TextField(blank=True, null=True)

class ConflictCheckResult(AuditTrackedModel):
    client_name = models.CharField(max_length=255)
    adverse_party_searched = models.CharField(max_length=255)
    is_conflict_found = models.BooleanField(default=False)
    conflict_details = models.TextField(blank=True, null=True)
    cleared_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    cleared_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Conflict Check: {self.client_name} vs {self.adverse_party_searched}"
""")
    with open(os.path.join(cli_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ClientProfile, KYCVerification, ConflictCheckResult

@login_required
def client_list(request):
    clients = ClientProfile.objects.filter(is_deleted=False)
    return render(request, 'clients/client_list.html', {'clients': clients})

@login_required
def client_detail(request, pk):
    client = get_object_or_404(ClientProfile, pk=pk)
    kyc_records = client.kyc_records.all()
    return render(request, 'clients/client_detail.html', {'client': client, 'kyc_records': kyc_records})

@login_required
def conflict_check_view(request):
    results = ConflictCheckResult.objects.all().order_by('-created_at')[:20]
    return render(request, 'clients/conflict_check.html', {'results': results})
""")
    with open(os.path.join(cli_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('<uuid:pk>/', views.client_detail, name='client_detail'),
    path('conflict-check/', views.conflict_check_view, name='conflict_check'),
]
""")
    with open(os.path.join(cli_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
from .models import ClientProfile, KYCVerification, ConflictCheckResult

@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'client_type', 'email', 'phone', 'is_verified', 'conflict_check_cleared']
    search_fields = ['display_name', 'email', 'tax_id_or_pan']
    list_filter = ['client_type', 'is_verified', 'conflict_check_cleared']

@admin.register(KYCVerification)
class KYCVerificationAdmin(admin.ModelAdmin):
    list_display = ['client', 'document_type', 'document_number', 'status', 'verified_at']

@admin.register(ConflictCheckResult)
class ConflictCheckResultAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'adverse_party_searched', 'is_conflict_found', 'cleared_at']
""")

    # -------------------------------------------------------------
    # 5. COURTS
    # -------------------------------------------------------------
    court_dir = os.path.join(base_dir, "apps", "courts")
    os.makedirs(court_dir, exist_ok=True)
    with open(os.path.join(court_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Courts package\n")
    with open(os.path.join(court_dir, "apps.py"), "w", encoding="utf-8") as f:
        f.write("""from django.apps import AppConfig

class CourtsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.courts'
    verbose_name = 'Courts, Judges & Benches'
""")
    with open(os.path.join(court_dir, "models.py"), "w", encoding="utf-8") as f:
        f.write("""from django.db import models
from apps.core.models import AuditTrackedModel

class CourtLevel(models.TextChoices):
    SUPREME_COURT = 'SUPREME_COURT', 'Supreme Court of India'
    HIGH_COURT = 'HIGH_COURT', 'High Court'
    DISTRICT_COURT = 'DISTRICT_COURT', 'District & Sessions Court'
    TRIBUNAL = 'TRIBUNAL', 'Special Tribunal (NCLT/DRT/CAT)'
    MAGISTRATE_COURT = 'MAGISTRATE_COURT', 'Magistrate Court'

class CourtComplex(AuditTrackedModel):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=30, choices=CourtLevel.choices, default=CourtLevel.DISTRICT_COURT)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    total_courtrooms = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"

class CourtRoom(AuditTrackedModel):
    court_complex = models.ForeignKey(CourtComplex, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=50)
    floor = models.CharField(max_length=20, default='Ground')
    has_video_conferencing = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(default=50)

    def __str__(self):
        return f"Room {self.room_number} - {self.court_complex.name}"

class Judge(AuditTrackedModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=100, default='Hon’ble Justice')
    court_complex = models.ForeignKey(CourtComplex, on_delete=models.CASCADE, related_name='judges')
    assigned_courtroom = models.ForeignKey(CourtRoom, on_delete=models.SET_NULL, null=True, blank=True)
    specialization = models.CharField(max_length=255, blank=True, null=True, help_text="e.g. Constitutional Bench, Commercial Division")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} {self.name}"

class Bench(AuditTrackedModel):
    name = models.CharField(max_length=255)
    court_complex = models.ForeignKey(CourtComplex, on_delete=models.CASCADE, related_name='benches')
    bench_type = models.CharField(max_length=50, choices=[('SINGLE', 'Single Judge Bench'), ('DIVISION', 'Division Bench'), ('FULL', 'Full Bench'), ('CONSTITUTION', 'Constitution Bench')])
    presiding_judges = models.ManyToManyField(Judge, related_name='benches')

    def __str__(self):
        return f"{self.name} - {self.court_complex.name}"
""")
    with open(os.path.join(court_dir, "views.py"), "w", encoding="utf-8") as f:
        f.write("""from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CourtComplex, CourtRoom, Judge, Bench

@login_required
def court_list(request):
    courts = CourtComplex.objects.all().order_by('state', 'name')
    return render(request, 'courts/court_list.html', {'courts': courts})

@login_required
def judge_list(request):
    judges = Judge.objects.filter(is_active=True).select_related('court_complex', 'assigned_courtroom')
    return render(request, 'courts/judge_list.html', {'judges': judges})

@login_required
def courtroom_schedule(request, pk):
    room = get_object_or_404(CourtRoom, pk=pk)
    return render(request, 'courts/courtroom_schedule.html', {'room': room})
""")
    with open(os.path.join(court_dir, "urls.py"), "w", encoding="utf-8") as f:
        f.write("""from django.urls import path
from . import views

app_name = 'courts'

urlpatterns = [
    path('', views.court_list, name='court_list'),
    path('judges/', views.judge_list, name='judge_list'),
    path('room/<int:pk>/schedule/', views.courtroom_schedule, name='courtroom_schedule'),
]
""")
    with open(os.path.join(court_dir, "admin.py"), "w", encoding="utf-8") as f:
        f.write("""from django.contrib import admin
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
""")

    print("Completed Apps Part 1 generation.")

if __name__ == '__main__':
    generate_apps_part_1('.')
