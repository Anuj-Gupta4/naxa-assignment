from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "naxa.settings")
app = Celery("naxa")

app.conf.enable_utc = False

app.conf.update(timezone="Asia/Kathmandu")

app.config_from_object(settings, namespace="CELERY")

# Celery Beat Settings
app.conf.beat_schedule = {
    "send-birthday-greetings": {
        "task": "assignments.tasks.send_birthday_greetings",
        "schedule": crontab(minute=0, hour=0),  # Runs at midnight every day
    },
}

app.autodiscover_tasks()
