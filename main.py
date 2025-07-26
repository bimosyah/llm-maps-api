from fastapi import FastAPI, Query
from llm import ask_llm
from google_maps import get_place_info

app = FastAPI()

@app.get("/search")
def search_location(prompt: str = Query(..., description="e.g. Best food in Jakarta")):
    llm_response = ask_llm(f"Give a place name based on: {prompt}")
    place_data = get_place_info(llm_response)
    return {
        "original_query": prompt,
        "llm_response": llm_response,
        "maps": place_data
    }
