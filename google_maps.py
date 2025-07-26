import os
import requests
from dotenv import load_dotenv

load_dotenv()
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_place_info(place_name: str):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": place_name,
        "key": GOOGLE_MAPS_API_KEY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if data["results"]:
        place = data["results"][0]
        name = place["name"]
        address = place["formatted_address"]
        location = place["geometry"]["location"]
        lat, lng = location["lat"], location["lng"]
        return {
            "name": name,
            "address": address,
            "maps_url": f"https://www.google.com/maps/search/?api=1&query={lat},{lng}",
            "embed_url": f"https://www.google.com/maps/embed/v1/place?key={GOOGLE_MAPS_API_KEY}&q={lat},{lng}"
        }

    return {"error": "No results found"}
