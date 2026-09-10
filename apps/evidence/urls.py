from django.urls import path
from . import views

app_name = 'evidence'

urlpatterns = [
    path('', views.evidence_register, name='register'),
    path('<uuid:pk>/', views.evidence_detail, name='detail'),
]
