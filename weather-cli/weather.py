import requests
from config import API_KEY, BASE_URL


def get_weather(city):
    if not API_KEY:
        raise RuntimeError("Missing API_KEY")
    r = requests.get(
        BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"}, timeout=10
    )
    if r.status_code == 401:
        raise RuntimeError("Invalid API key")
    if r.status_code == 404:
        raise RuntimeError("City not found")
    if r.status_code != 200:
        raise RuntimeError("Weather API error")
    return r.json()
