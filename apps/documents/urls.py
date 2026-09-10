from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('', views.document_vault, name='vault'),
    path('vault/', views.document_vault, name='vault_alias'),
    path('<uuid:pk>/', views.document_detail, name='detail'),
]
