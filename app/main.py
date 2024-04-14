from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from .common.http_exceptions import ConflictException, NotFoundException
from .config.exception_handlers import (
    conflict_exception_handler,
    general_exception_handler,
    not_found_exception_handler,
)
from .config.limiter_config import get_limiter_config
from .config.logging_config import configure_logging
from .config.security_headers_config import add_security_headers
from .config.settings import settings
from .user.user_routers import user_router

# Configura logging al iniciar el módulo
configure_logging()

# Crea la aplicación FastAPI
app = FastAPI(title="Estandar API", version="1.0")


def configure_app():
    configure_middlewares()
    configure_exception_handlers()
    configure_routes()


def configure_middlewares():
    limiter = get_limiter_config()
    app.state.limiter = limiter
    app.add_middleware(SlowAPIMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def configure_exception_handlers():
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    app.add_exception_handler(NotFoundException, not_found_exception_handler)
    app.add_exception_handler(ConflictException, conflict_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)


def configure_routes():
    app.include_router(user_router, prefix="/users")
    add_security_headers(app)


# Configura la aplicación
configure_app()
