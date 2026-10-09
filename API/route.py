from fastapi import FastAPI,HTTPException 
from fastapi.responses import JSONResponse
from pydantic import BaseModel,EmailStr,Field
from typing import Optional, Annotated,Literal
import json

def open_data():
    with open("patients.json" , 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open("patients.json", 'w') as f:
        json.dump(data, f, indent=4)

class Patient(BaseModel):
    id : str
    name : Annotated[str, Field(...,description="this is the name field")]
    age : Annotated[int,  Field(..., gt = 0 , lt = 100,description= "this is for age")]
    city : Annotated[str, Field(..., description="this is for city")]
    gender: Annotated[Literal['male','female'], Field(..., description="this is for gender")]
    height: Annotated[int, Field(..., description="Height")]
    weight: Annotated[int, Field(...,description="weight")]
    Annotated[str, Field(..., description="this is for city")]


app =  FastAPI()

@app.get("/home")
def home():
    return {"message": "hello "}

@app.post("/create_patient")
def create_patient(patient :Patient):
    data = open_data()
    if patient.id in data:
        raise HTTPException(status_code = 400, detail= "patient already existts")
    else:
        data[patient.id] = patient.model_dump()

    save_data(data)

    return JSONResponse(status_code=201 , content = "successfully added")