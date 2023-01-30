# Celery
from celery import shared_task


@shared_task(name='url_times_clicked', autoretry_for=(Exception,), retry_kwargs={'max_retries': 2})
def url_times_clicked(pk):
    try:
        from communicator_api.adapters.models.sql.short_url import ShortUrl
        obj = ShortUrl.objects.get(pk=pk)
        obj.times_clicked = obj.times_clicked + 1
        obj.save()
    except Exception:
        pass


@shared_task(name='url_deactive', autoretry_for=(Exception,), retry_kwargs={'max_retries': 2})
def url_deactive(pk):
    try:
        from communicator_api.adapters.models.sql.short_url import ShortUrl
        obj = ShortUrl.objects.get(pk=pk)
        obj.active = False
        obj.save()
    except Exception:
        pass
