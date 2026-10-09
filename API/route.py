from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
import json

def open_data():
    with open("patients.json" , 'r') as f:
        data = json.load(f)
    return data

print(open_data())
class Patient(BaseModel):
    id : int
    name :str
    email: EmailStr

patient = Patient()

app =  FastAPI()

@app.get("/home")
def home():
    return {"message": "hello "}

@app.post("/create_patient")
def create_patient(Patient :patient):
    data = open_data()