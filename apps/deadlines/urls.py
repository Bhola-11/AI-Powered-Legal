from django.urls import path
from . import views

app_name = 'deadlines'

urlpatterns = [
    path('', views.deadline_list, name='deadline_list'),
    path('calculator/', views.limitation_calculator_view, name='limitation_calculator'),
]
