from fastapi import FastAPI,Path, HTTPException
import json


app = FastAPI()

def load_data():
    with open('patients.json' , 'r') as f:
        data = json.load(f)
    return data


@app.get("/")
def home():
    return "this is the home page of our webapp"


@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")           #PATH PARAMETER
def view_patient(patient_id : str = Path(...,description = "GIVE PATIENT ID" , example = "P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = "patient not found")