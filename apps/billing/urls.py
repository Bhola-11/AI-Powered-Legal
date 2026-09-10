from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('time-entries/', views.time_entries_view, name='time_entries'),
    path('<uuid:pk>/', views.invoice_detail, name='invoice_detail'),
]
