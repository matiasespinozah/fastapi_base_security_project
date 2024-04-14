import logging
from datetime import datetime

from fastapi import Request
from fastapi.responses import JSONResponse

from ..common.http_exceptions import ConflictException, NotFoundException


async def conflict_exception_handler(_: Request, exc: ConflictException):
    return JSONResponse(
        status_code=409,
        content={
            "message": exc.detail,
            "status": 409,
            "error": "Conflict",
            "timestamp": datetime.now().isoformat(),
        },
    )


async def not_found_exception_handler(_: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "message": exc.detail,
            "status": 404,
            "error": "Not Found",
            "timestamp": datetime.now().isoformat(),
        },
    )


async def general_exception_handler(_: Request, exc: Exception):
    logging.error("An internal server error occurred: %s", exc)

    return JSONResponse(
        status_code=500,
        content={
            "message": "An internal server error occurred",
            "status": 500,
            "error": "Internal Server Error",
            "timestamp": datetime.now().isoformat(),
        },
    )
