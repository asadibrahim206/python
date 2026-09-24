from fastapi import FastAPI,Path, HTTPException,Query
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