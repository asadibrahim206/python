from fastapi import FastAPI,Path, HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, computed_field,Field
from typing import Annotated,Literal
import json



class Patient(BaseModel):
    id :     Annotated[str, Field(..., description = "Provide patient ID :" , example = 'P001')]
    name :  Annotated[str, Field(..., description = "Provide the patient Name: ")]
    city :  Annotated[str, Field( ...,description = "Provide the patient City: ", example = 'Lahore')]
    age :   Annotated[int, Field(...,gt = 0,lt = 200, description = "Provide the patient Age: ")]
    gander: Annotated[Literal ['male','female','other'], Field(description = "Provide the patient Gander: ")]
    height: Annotated[float, Field(gt = 0 ,lt =50, description = "Provide the patient Height: ")]
    weight: Annotated[float, Field(gt = 0, lt= 500, description = "Provide the patient Weight: ")]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = self.weight/(self.height**2)
        return bmi

    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return "Under Weight"
        elif self.bmi > 18.5 and self.bmi < 30:
            return "Normal"
        elif self.bmi > 30 and self.bmi < 45:
            return "chuby"
        else:
            return "Obese"

app = FastAPI()


def load_data():
    with open('patients.json' , 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f)



@app.get("/")
def home():
    return "this is the home page of our webapp"


@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")           #PATH PARAMETER
def view_patient(patient_id : str = Path(...,description = "GIVE PATIENT ID" , examples = "P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = "patient not found")

@app.get("/sort")                        #PQuery Parameter
def sort_patients(
    sort_by: str = Query(..., description = "Sort patient by [height,bmi,weight]"), 
    order_by :str = Query('asc',description = "asc -desc")
    ):
    

    valid_fields = ['height', 'bmi', 'weight']
    if sort_by not in valid_fields:
        raise HTTPException (status_code = 400, detail = "invalid field selection")

    if order_by not in ['asc','desc']:
        raise HTTPException (status_code = 400, detail = "invalid order selection")

    data = load_data()

    sort_order = True if order_by== 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse = sort_order)

    return sorted_data

@app.post('/create')
def add_patient(patient:Patient): #we wil directly pass the data to our pydantic model
#LOAD DATA
    data = load_data()
#CHECK IF PATIENT LREADY EXISTIS
    if patient.id in data:
        raise HTTPException(status_code = 400, detail="patent already exists")
#new patiet addded to dict
    data[patient.id] = patient.model_dump(exclude = ['id'])
#save data to json
    save_data(data)

    return JSONResponse(status_code = 201, content = {'message': "patient added successfully..uvi"} )