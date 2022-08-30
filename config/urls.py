"""shalonapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.payments import views
# from clients import views
# from . import views
from .views import test_celery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/', views.list_payments),
    path('celery-test/', test_celery),
    path('testsiigo/', views.testsiigo),
    path('testsiigo_create_client/', views.test_siigo_create_client),

]


# to do:

# crear un modelo company:
# nombre de shalon
# nit
# telefono
# direccion
# agenda_pro_token es un string largo
# siigo_username
# siigo_access_key
# siigo_token

# Crear una factura desde postman al endpoint de prueba Ojo
