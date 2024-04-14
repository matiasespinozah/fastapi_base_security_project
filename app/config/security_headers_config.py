from fastapi import FastAPI, Request

from .settings import settings


def add_security_headers(app: FastAPI):
    @app.middleware("http")
    async def security_headers(request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-XSS-Protection"] = "1; mode=block"

        if settings.env == "prod":
            csp_policy = "default-src 'self'; script-src 'self';"
        else:
            csp_policy = "default-src 'self' 'unsafe-inline' 'unsafe-eval' data: https:; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; img-src 'self' data: https://fastapi.tiangolo.com"

        response.headers["Content-Security-Policy"] = csp_policy
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response
