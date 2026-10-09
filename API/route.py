from fastapi import FastAPI,HTTPException 
from fastapi.responses import JSONResponse
from pydantic import BaseModel,EmailStr,Field , field_validator ,  computed_field
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
    height: Annotated[float, Field(..., description="Height")]
    weight: Annotated[float, Field(...,description="weight")]
 
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    
    @field_validator("age")
    @classmethod
    def check_age(cls, value:int) -> int:
        if value < 18:
            raise ValueError("Patient must be at least 18 years old")
        return value

class PatientUpdate(BaseModel)
    name : Annotated[Optional[str], Field(description="this is the name field")]
    age : Annotated[Optional[int],  Field(gt = 0 , lt = 100,description= "this is for age")]
    city : Annotated[Optional[str], Field(description="this is for city")]
    gender: Annotated[Optional[Literal['male','female']], Field(description="this is for gender")]
    height: Annotated[Optional[float], Field(description="Height")]
    weight: Annotated[Optional[float], Field(description="weight")]

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


@app.put("/update_patient/{patient_id}")
def update_patient()