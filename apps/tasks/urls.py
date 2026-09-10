from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('kanban/', views.kanban_view, name='kanban'),
    path('<uuid:pk>/', views.task_detail, name='task_detail'),
]
