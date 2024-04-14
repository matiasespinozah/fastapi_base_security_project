from sqlalchemy.orm import Session

from .user_model import User
from .user_schemas import UserCreate, UserRead


def get_user(user_id: int, db: Session) -> UserRead:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return UserRead.from_orm(user)

    return None


def create_user(user_data: UserCreate, db: Session) -> UserRead:
    new_user = User(nombre=user_data.nombre, apellido=user_data.apellido)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return UserRead.from_orm(new_user)
