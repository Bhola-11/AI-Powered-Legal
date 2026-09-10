from django.urls import path
from . import views

app_name = 'orders_judgments'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<uuid:pk>/', views.order_detail, name='order_detail'),
]
