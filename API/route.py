from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,EmailStr
import json

def open_data():
    with open("patients.json" , 'r') as f:
        data = json.load(f)
    return data


class Patient(BaseModel):
    id : int
    name :str
    email: EmailStr



app =  FastAPI()

@app.get("/home")
def home():
    return {"message": "hello "}

@app.post("/create_patient/{patient_id}")
def create_patient(patient_id,patient :Patient):
    data = open_data()
    if patient_id in data:
        raise HTTPException(status_code = "400", detail= "patient already existts")
