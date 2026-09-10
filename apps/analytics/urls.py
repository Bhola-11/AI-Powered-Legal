from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.reports_dashboard, name='reports_root'),
    path('reports/', views.reports_dashboard, name='reports_dashboard'),
]
