from celery import Celery

from settings import CelerySettings, get_settings


def create_celery() -> Celery:
    redis_settings = get_settings(CelerySettings)
    app = Celery(
        broker=redis_settings.broker_url,
        backend=redis_settings.backend_url,
    )
    app.conf.update()
    app.autodiscover_tasks(packages=[])
    app.conf.beat_schedule = {}
    return app
