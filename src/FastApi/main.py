from typing import List
from uuid import uuid4

from fastapi import FastAPI

from models import User, Gender, Role

app = FastAPI()


db:List[User]=[
    User(
        name="seun",
        id=uuid4(),
        gender=Gender.male,
        roles=Role.user
    ),
    User(
        name="jewel",
        id=uuid4(),
        gender=Gender.female,
        roles=Role.user
    ),
    User(
        name="dabere",
        id=uuid4(),
        gender=Gender.female,
        roles=Role.admin
    )

]


@app.get("/")
async def root():
    return {"message": "hello wee!"}


@app.get("/api/v1/all")
async def getUsers():
    return db