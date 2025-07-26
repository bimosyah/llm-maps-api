import os

import requests
from dotenv import load_dotenv

load_dotenv()
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


def get_place_info(place_name: str):
    url = "https://places.googleapis.com/v1/places:searchText"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.location"
    }

    body = {
        "textQuery": place_name
    }

    response = requests.post(url, headers=headers, json=body)

    # Raise if error (will show full trace)
    response.raise_for_status()

    data = response.json()

    if "places" in data and data["places"]:
        place = data["places"][0]
        name = place["displayName"]["text"]
        address = place["formattedAddress"]
        lat = place["location"]["latitude"]
        lng = place["location"]["longitude"]
        return {
            "name": name,
            "address": address,
            "maps_url": f"https://www.google.com/maps/search/?api=1&query={lat},{lng}",
            "embed_url": f"https://www.google.com/maps/embed/v1/place?key={GOOGLE_MAPS_API_KEY}&q={lat},{lng}"
        }

    return {"error": "No results found"}
