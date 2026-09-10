from django.urls import path
from . import views

app_name = 'communications'

urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('<uuid:pk>/', views.thread_detail, name='thread_detail'),
]
