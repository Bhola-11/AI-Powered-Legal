from django.urls import path
from . import views

app_name = 'courts'

urlpatterns = [
    path('', views.court_list, name='court_list'),
    path('judges/', views.judge_list, name='judge_list'),
    path('room/<int:pk>/schedule/', views.courtroom_schedule, name='courtroom_schedule'),
]
