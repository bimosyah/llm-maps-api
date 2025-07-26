from fastapi import FastAPI, Query

from google_maps import get_place_info
from llm import ask_llm

app = FastAPI()


@app.get("/search")
def search_location(prompt: str = Query(..., description="e.g. Best food in Jakarta")):
    llm_response = ask_llm(
        f"""
        Dari pertanyaan: "{prompt}",
        berikan hanya 1 nama tempat yang spesifik dan cocok untuk dicari di Google Maps.
        Jangan tambahkan penjelasan. Tulis hanya nama tempatnya saja.
        """
    )
    place_data = get_place_info(llm_response)

    return {
        "original_query": prompt,
        "llm_response": llm_response,
        "maps": place_data
    }
