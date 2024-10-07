from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    username: str


class UserRead(UserBase):
    pass
