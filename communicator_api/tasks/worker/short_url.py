# Celery
from celery import shared_task


@shared_task(name='url_times_clicked', autoretry_for=(Exception,), retry_kwargs={'max_retries': 2})
def url_times_clicked(pk):
    from communicator_api.adapters.models.sql.short_url import ShortUrl
    ShortUrl.objects.filter(pk=pk).update(times_clicked=+1)


@shared_task(name='url_deactive', autoretry_for=(Exception,), retry_kwargs={'max_retries': 2})
def url_deactive(pk):
    from communicator_api.adapters.models.sql.short_url import ShortUrl
    ShortUrl.objects.filter(pk=pk).update(active=False)
