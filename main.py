from typing import Dict

import uvicorn as uvicorn
from fastapi import FastAPI

from models.event import Event
from services.database import Database
from services.weather import WeatherService

app = FastAPI()
db = Database()
weather_service = WeatherService()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/events/")
async def get_all_events():
    return db.get_all_data()


@app.post("/events/")
async def create_event(event: Event):
    if event.tags and "outdoor" in event.tags:
        event.forecast = weather_service.get_weather(event.location)
    db.insert_data(event)
    return event


@app.get("/events/{event_id}")
async def get_event(event_id: int):
    return db.get_record_by_id(event_id)


@app.patch("/events/{event_id}")
async def update_event(event_id: int, data: Dict[str, str]):
    return db.update_data(event_id, data)


@app.delete("/events/{event_id}")
async def delete_event(event_id: int):
    return db.delete_data(event_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)