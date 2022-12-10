"""Celery app config."""

import os

#Celery imports
from celery import Celery

# Django imports
from django.apps import apps, AppConfig
from django.conf import settings

# Celery configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('APP_ENV_SETTINGS'))
app = Celery('apps')
app.config_from_object('django.conf:settings', namespace='CELERY')


"""
    This is the configuration for celery like an app
"""
class CeleryAppConfig(AppConfig):
    name = 'apps.taskapp'
    verbose_name = 'Celery Config'
    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


