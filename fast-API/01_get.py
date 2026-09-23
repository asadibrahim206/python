from fastapi import FastApi
import json

def load_data():
    with open('patient.json' , 'r') as f:
        data = json.load(f)
    return data

app = FastApi()

app.get("/")
    def view():
        data = load_data()
        return data