from datetime import datetime
from django.utils import timezone

from service.celery_app import app
from .models import ItemDiscount


@app.task
def delete_expired_discounts():
    """Delete expired product discounts"""
    current_time = timezone.now()
    items = ItemDiscount.objects.filter(end_date__lte=current_time)
    if items:
        items.delete()
    else:
        pass
