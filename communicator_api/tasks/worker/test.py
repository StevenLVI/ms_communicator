# Celery
from celery import shared_task


@shared_task(name='test', autoretry_for=(Exception,), retry_kwargs={'max_retries': 2})
def test(x, y):
    return x + y
