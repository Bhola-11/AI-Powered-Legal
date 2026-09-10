from django.urls import path
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
