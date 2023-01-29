# Celery
from celery import shared_task


@shared_task(name='test_beat', autoretry_for=(Exception,), retry_kwargs={'max_retries': 2})
def test_beat():
    return {"test": True}
