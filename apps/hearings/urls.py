from django.urls import path
from . import views

app_name = 'hearings'

urlpatterns = [
    path('', views.hearing_list, name='hearing_list'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('daily-board/', views.daily_board_view, name='daily_board'),
    path('<uuid:pk>/', views.hearing_detail, name='hearing_detail'),
]
