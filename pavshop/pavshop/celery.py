# django_celery/celery.py

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pavshop.settings")
app = Celery("pavshop")
app.config_from_object("django.conf:settings", namespace="CELERY")

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
app.autodiscover_tasks()

