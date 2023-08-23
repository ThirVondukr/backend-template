import sentry_sdk

from settings import SentrySettings, get_settings


def init_sentry() -> None:
    settings = get_settings(SentrySettings)
    sentry_sdk.init(
        dsn=settings.dsn,
        environment=settings.environment.name,
        traces_sample_rate=settings.traces_sample_rate,
    )
