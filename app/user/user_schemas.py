from pydantic import BaseModel


class UserBase(BaseModel):
    nombre: str
    apellido: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True
