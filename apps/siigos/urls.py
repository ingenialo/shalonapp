from django.urls import path
from apps.siigos import views

urlpatterns = [
    path('get_customers/', views.get_customers),
    path('get_document_type/', views.get_document_type),
    path('testsiigo_create_client/', views.test_siigo_create_client),
]