# Celery
from celery import shared_task
from datetime import datetime


@shared_task(name='deactive_short_url_date', autoretry_for=(Exception,), retry_kwargs={'max_retries': 2})
def deactive_short_url_date():
    try:
        from communicator_api.adapters.models.sql.short_url import ShortUrl

        now = datetime.now()
        ShortUrl.objects.filter(expiration_date=now.date()).update(active=False)
    except Exception:
        pass
