from fastapi import FastAPI
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