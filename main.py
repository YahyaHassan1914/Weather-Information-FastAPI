from fastapi import FastAPI, HTTPException
import requests
import json

# Open the JSON file with api key
with open('api_key.json', 'r') as file:
    api_key = json.load(file)

app = FastAPI()

# Replace with your actual API key and endpoint
WEATHER_API_KEY = api_key["api_key"]
WEATHER_API_URL = 'http://api.weatherapi.com/v1/current.json'

@app.get("/weather")
def get_weather(city: str):
    params = {
        'key': WEATHER_API_KEY,
        'q': city,
    }
    response = requests.get(WEATHER_API_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Weather data not found")
