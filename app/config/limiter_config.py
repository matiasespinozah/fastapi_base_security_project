from slowapi import Limiter
from slowapi.util import get_remote_address

from .settings import settings


def get_limiter_config():
    return Limiter(
        key_func=get_remote_address, default_limits=[f"{settings.rate_limit_per_minute}/minute"]
    )
