from fastapi import HTTPException, status
from fastapi.responses import JSONResponse


class NotFoundException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class ConflictException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)


class UnauthorizedException(Exception):
    def __init__(self, detail: str):
        self.response = JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"message": detail}
        )
