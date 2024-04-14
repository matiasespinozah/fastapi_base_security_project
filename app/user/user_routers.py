from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..common.http_exceptions import NotFoundException
from ..dependencies import get_db
from .user_schemas import UserCreate, UserRead
from .user_service import create_user, get_user

user_router = APIRouter()


@user_router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(user_id, db)
    if user is None:
        raise NotFoundException("usuario no encontrado")
    return user


@user_router.post("/", response_model=UserRead)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)
