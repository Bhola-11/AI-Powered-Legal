from django.urls import path
from . import views

app_name = 'ai_engine'

urlpatterns = [
    path('', views.ai_hub_view, name='ai_hub_root'),
    path('hub/', views.ai_hub_view, name='ai_hub'),
]
