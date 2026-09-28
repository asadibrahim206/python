from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import json
from typing import Annotated, Literal , Optional


class Patient(BaseModel):
    id :     Annotated[str, Field(..., description = "Provide patient ID :" , example = 'P001')]
    name :  Annotated[str, Field(..., description = "Provide the patient Name: ")]
    city :  Annotated[str, Field( ...,description = "Provide the patient City: ", example = 'Lahore')]
    age :   Annotated[int, Field(...,gt = 0,lt = 200, description = "Provide the patient Age: ")]
    gander: Annotated[Literal ['male','female','other'], Field(description = "Provide the patient Gander: ")]
    height: Annotated[float, Field(gt = 0 ,lt =50, description = "Provide the patient Height: ")]
    weight: Annotated[float, Field(gt = 0, lt= 500, description = "Provide the patient Weight: ")]

class PatientUpdate(BaseModel):
        name :  Annotated[Optional[str], Field(default =None )]
        city :  Annotated[Optional[str], Field(default = None)]
        age :   Annotated[Optional[int], Field(default = None, gt = 0)]
        gander: Annotated[Optional[Literal['male','female','other']], Field(default = None)]
        height: Annotated[Optional[float], Field(default = None,gt = 0)]
        weight: Annotated[Optional[float], Field(default = None, gt = 0)]

def load_data():
    with open("patients.json", 'r') as f:
        data = json.load(f)
    return data


def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)


app = FastAPI()

#POST
@app.post("/make")
def create_patient(patient : Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code = 400 , detail = "this person already exists")
    data[patient.id] = patient.model_dump(exclude=id)
    save_data(data)

#PUT
@app.put("/change")
def edit_patient(patient : PatientUpdate):
    data = load_data()

    if patient.id not in data: 
        raise HTTPException(status_code = 404, detail = " patient is not in data") #
    existing_patient = data[patient.id]  #let say id is P001 , the patient with this id will be stored in var.
    
