from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('<uuid:pk>/', views.client_detail, name='client_detail'),
    path('conflict-check/', views.conflict_check_view, name='conflict_check'),
]
