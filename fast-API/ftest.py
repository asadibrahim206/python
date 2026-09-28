import json
from typing import Annotated, Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Provide patient ID :", examples=['P001'])]
    name: Annotated[str, Field(..., description="Provide the patient Name: ")]
    city: Annotated[str, Field(..., description="Provide the patient City: ", examples=['Lahore'])]
    age: Annotated[int, Field(..., gt=0, lt=200, description="Provide the patient Age: ")]
    gander: Annotated[Literal['male', 'female', 'other'], Field(description="Provide the patient Gender: ")]
    height: Annotated[float, Field(..., gt=0, lt=50, description="Provide the patient Height: ")]
    weight: Annotated[float, Field(..., gt=0, lt=500, description="Provide the patient Weight: ")]


def load_data():
    try:
        with open("patients.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)


app = FastAPI()

# Decorator placed directly above the endpoint handler
@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()
    
    if patient.id in data:
        # Fixed detail parameter name and status code
        raise HTTPException(status_code=400, detail="This patient ID is already in the database.")
    
    data[patient.id] = patient.model_dump(exclude=['id'])
    save_data(data)
    
return {"message": "Patient created successfully", "patient_id": patient.id}