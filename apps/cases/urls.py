from django.urls import path
from . import views

app_name = 'cases'

urlpatterns = [
    path('', views.case_list, name='case_list'),
    path('intake/', views.case_intake, name='case_intake'),
    path('<uuid:pk>/', views.case_detail, name='case_detail'),
]
