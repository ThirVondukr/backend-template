from datetime import UTC, datetime


def utc_now() -> datetime:
    return datetime.now(tz=UTC)  # pragma: no cover
