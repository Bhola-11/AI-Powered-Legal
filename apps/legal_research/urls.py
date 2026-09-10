from django.urls import path
from . import views

app_name = 'legal_research'

urlpatterns = [
    path('', views.acts_list, name='research_root'),
    path('acts/', views.acts_list, name='acts_list'),
    path('acts/<int:pk>/', views.act_detail, name='act_detail'),
    path('precedents/', views.precedent_list, name='precedent_list'),
    path('precedents/<uuid:pk>/', views.precedent_detail, name='precedent_detail'),
    path('notebook/', views.notebook_view, name='notebook'),
]
