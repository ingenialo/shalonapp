from django.urls import path, include

from apps.payments import views

urlpatterns = [
    path('get-payments-by-date', views.getPaymentsByDate),
    path('agenda_id/<int:id_agenda_pro>', views.get_payment),
]