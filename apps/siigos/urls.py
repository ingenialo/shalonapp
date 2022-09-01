from django.urls import path
from apps.siigos import views

urlpatterns = [
    path('get_document_type/', views.get_document_type),
]