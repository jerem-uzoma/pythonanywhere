from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# Set the DJANGO_SETTINGS_MODULE environment variable for the celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

app = Celery('blog')

# Import the CELERY settings from the Django settings file
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load the task module from all registered apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
