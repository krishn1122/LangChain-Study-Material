from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def helllo():
    return {"message": "PAtient Management System"}

@app.get('/about')
def about():
    return {"message": "A fully functional patient management system built with FastAPI."}

@app.get('/view')
def view():
    data = load_data()
    return data