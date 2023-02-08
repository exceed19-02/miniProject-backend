from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Union
from database import mongo_connection

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class light(BaseModel):
    light_id:int
    status: bool
    mode: str
    brightness: int


@app.get("/{id}")
def light(id: int):
    return dict(mongo_connection["light"].find_one({"light_id":id},{"_id":0}))

@app.put("/")
def light():
    mongo_connection["light"].insert_one({"light_id":1})