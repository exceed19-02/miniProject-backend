from fastapi import FastAPI, HTTPException, Body
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

# get all data
@app.get("/")
def get_all_light():
    return list(mongo_connection["light"].find({}, {"_id": 0}))

@app.get("/{id}")
def get_light(id: int):
    if id < 1 or id > 3:
        raise HTTPException(404, detail="light id is invalid")
    return dict(mongo_connection["light"].find_one({"light_id": id}, {"_id": 0}))

# mock data
data=[
    {"light_id":1,"status":True,"mode":"AUTO","brightness":100},
    {"light_id":2,"status":False,"mode":"DISCO","brightness":0},
    {"light_id":3,"status":True,"mode":"MANUAL","brightness":100},
]

# add mock data
@app.post("/AddMock")
def post_light():
    mongo_connection["light"].insert_many(data)

# update data by input light basemodel
@app.put("/update")
def update_light(light_object: light):
    enum_mode = ["AUTO","MANUAL","DISCO"]
    if light_object.light_id < 1 or light_object.light_id > 3:
        raise HTTPException(status_code=400, detail="LightID out of range")
    if light_object.mode not in enum_mode:
        raise HTTPException(status_code=400, detail="Mode not available")
    if light_object.brightness < 0 or light_object.brightness > 100:
        raise HTTPException(status_code=400, detail="Brightness not in range")
    if light_object.mode == "AUTO" or light_object.mode == "DISCO":
        mongo_connection["light"].update_one({"light_id": light_object.light_id},{"$set": {"status": light_object.status, "mode": light_object.mode}})
        return {"success": True, "detail": "Brightness unchanged"}
    mongo_connection["light"].update_one({"light_id": light_object.light_id},{"$set": {"status": light_object.status, "mode": light_object.mode, "brightness": light_object.brightness}})
    return {"success": True}

# delete all data
@app.delete("/")
def deleteLight():
    mongo_connection["light"].delete_many({})