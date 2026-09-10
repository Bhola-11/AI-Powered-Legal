from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('<uuid:pk>/read/', views.mark_notification_read, name='mark_notification_read'),
]
