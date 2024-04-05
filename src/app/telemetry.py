import logging

import sentry_sdk

from app.settings import LoggingSettings, SentrySettings
from lib.settings import get_settings


def setup_telemetry() -> None:
    sentry_settings = get_settings(SentrySettings)
    sentry_sdk.init(
        dsn=sentry_settings.dsn,
        environment=sentry_settings.environment.name,
        traces_sample_rate=sentry_settings.traces_sample_rate,
    )

    logging_settings = get_settings(LoggingSettings)

    logging.basicConfig(level=logging_settings.level.name)
