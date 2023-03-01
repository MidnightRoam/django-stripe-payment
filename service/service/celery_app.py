from celery import Celery
import os

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')

app = Celery('service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# celery beat tasks
app.conf.beat_schedule = {
    'delete_expired_discounts': {
        'task': 'products.tasks.delete_expired_discounts',
        'schedule': crontab(minute='*/1'),
    }
}
