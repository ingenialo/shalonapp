from django.urls import path
from apps.siigos import views

urlpatterns = [
    path('get_customers/', views.get_customers),
    path('get_document_type/', views.get_document_type),
    path('test_siigo_create_client/', views.test_siigo_create_client),
    path('test_siigo_facturar/', views.test_siigo_facturar),
    path('facturar_electronica/<int:id_payment>/', views.facturar_electronica_payment),
]