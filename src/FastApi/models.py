import uuid
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    user = "User"
    admin = "Admin"


class User(BaseModel):
    name: str
    id: Optional[UUID] = uuid.uuid4()
    gender: Gender
    roles: Role
