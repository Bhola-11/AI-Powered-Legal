from django.shortcuts import render, redirect
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
