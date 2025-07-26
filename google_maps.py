import json
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

    # 🔍 DEBUG PRINT: Show request details
    print("\n=== REQUEST DEBUG ===")
    print("URL:", url)
    print("Headers:", json.dumps(headers, indent=2))
    print("Body:", json.dumps(body, indent=2))

    response = requests.post(url, headers=headers, json=body)

    # Raise if error (will show full trace)
    response.raise_for_status()

    # 🔍 DEBUG PRINT: Response
    data = response.json()
    print("\n=== RESPONSE DEBUG ===")
    print(json.dumps(data, indent=2))

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
