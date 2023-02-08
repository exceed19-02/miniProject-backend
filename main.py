from fastapi import FastAPI, HTTPException
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
    if id < 1 or id > 3:
        raise HTTPException(404, detail="light id is invalid")
    return dict(mongo_connection["light"].find_one({"light_id": id}, {"_id": 0}))

data=[
    {"light_id":1,"status":True,"mode":"AUTO","brightness":100},
    {"light_id":2,"status":False,"mode":"DISCO","brightness":0},
    {"light_id":3,"status":True,"mode":"MANUAL","brightness":100},
]

@app.post("/AddMock")
def light():
    mongo_connection["light"].insert_many(data)

# delete all data
@app.delete("/")
def deleteLight():
    mongo_connection["light"].delete_many({})