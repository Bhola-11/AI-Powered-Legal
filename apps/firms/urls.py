from django.urls import path
from . import views

app_name = 'firms'

urlpatterns = [
    path('', views.branch_list, name='firm_root'),
    path('<uuid:pk>/', views.firm_detail, name='firm_detail'),
    path('branches/', views.branch_list, name='branch_list'),
]
