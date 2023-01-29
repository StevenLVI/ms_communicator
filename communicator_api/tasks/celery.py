"""Celery app config."""

import os
from celery import Celery
from django.apps import apps, AppConfig
from django.conf import settings
from celery.schedules import crontab

if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


app = Celery('communicator_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'America/Bogota'

app.conf.beat_schedule = {
    'worker_periodic': {
        'task': 'deactive_short_url_date',
        'schedule': crontab(hour='23', minute='59', day_of_week='*'),
        'args': ()
    },
}


class CeleryAppConfig(AppConfig):
    name = 'communicator_api.tasks.worker'

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


class CeleryAppConfigBeat(AppConfig):
    name = 'communicator_api.tasks.beat'

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)
