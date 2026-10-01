import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chuck.settings")

app = Celery("chuck")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "get_joke_3s": {"task": "norris.tasks.get_joke", "schedule": 8.0}
}
