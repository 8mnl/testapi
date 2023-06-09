#!/usr/bin/env python3.9
from typing import Union, Optional, List
from uuid import UUID, uuid4
from enum import Enum
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Gender(str, Enum):
    male = "male"
    female = "female"
    diverse = "diverse"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    as_admin = "assistant admin"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

db: List[User] = [
    User(
    id=uuid4(),
    first_name="Dwight",
    last_name="Schrute",
    gender=Gender.male,
    roles=[Role.user, Role.as_admin],
    ),

    User(
    id=uuid4(),
    first_name="Jim",
    last_name="Halpert",
    gender=Gender.male,
    roles=[Role.user],
    ),

    User(
    id=uuid4(),
    first_name="Pam",
    last_name="Beesly",
    gender=Gender.female,
    roles=[Role.user],
    ),

    User(
    id=uuid4(),
    first_name="Michael",
    last_name="Scott",
    gender=Gender.male,
    roles=[Role.admin, Role.user],
    ),
]

class Data(BaseModel):
    status: str
    doctype: Optional[str] = "Invoice"
    price: float
    company: str
    is_active: bool

@app.get("/")
def get_index():
    return {"Status": "GET Method"}

@app.post("/")
def post_index():
    return {"Status": "POST Method"}

@app.get("/data/")
def get_data():
    return {"Status": "New",
            "Doc.-Type": "Invoice",
            "Company": "Random GmbH",
            "Mail": "post@example.com"}

@app.get("/users/")
def get_users():
    return db

@app.post("/postdata/")
def post_data(data: Data):
    # if data.price < 0:
    #     data.price = 0
    return data

@app.get("/parameter/{input_string}")
def get_parameter(input_string: str):
    return {"Parameter": input_string}

@app.get("/queries/")
def get_queries(a: Optional[str] = None, b: Optional[str] = None, c: Optional[str] = None):
    return {"a": a,
            "b": b,
            "c": c,}