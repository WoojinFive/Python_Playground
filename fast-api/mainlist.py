from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
import requests

app = FastAPI()

db = []

#----------------------------------------------------------------------------------------------
# data models
#----------------------------------------------------------------------------------------------
class City(BaseModel):
    name: str
    timezone: str


templates = Jinja2Templates(directory="templates")


@app.get("/")
def root():
    return {"Hello": "World!"}

@app.get("/cities")
def get_cities():
    results = []
    for city in db:
        strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
        r = requests.get(strs)
        print("@@@@@@@@@@@", r.json())
        cur_time = r.json()['datetime']
        results.append({'name': city['name'], 'timezone': city['timezone'], 'current_time': cur_time})

    return results

@app.get("/cities/{city_id}")
def get_city(city_id: int):
    city = db[city_id - 1]
    strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
    r = requests.get(strs)
    cur_time = r.json()['datetime']
    
    return {'name': city['name'], 'timezone': city['timezone'], 'current_time': cur_time}

@app.post("/cities")
def create_city(city: City):
    db.append(city.dict())

    return db[-1]

@app.delete("/cities/{city_id}")
def delete_city(city_id: int):
    db.pop(city_id - 1)

    return {}