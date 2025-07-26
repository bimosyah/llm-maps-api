from fastapi import FastAPI, Query

from google_maps import get_place_info
from llm import ask_llm
from openai_llm import ask_openai

app = FastAPI()


@app.get("/search")
def search_location(
        prompt: str = Query(..., description="e.g. Best food in Jakarta"),
        llm: str = Query("local", description="Choose 'local' or 'openai'")
):
    if llm == "openai":
        llm_response = ask_openai(
            f"""
            Dari pertanyaan: "{prompt}",
            berikan hanya 1 nama tempat yang spesifik dan cocok untuk dicari di Google Maps.
            Jangan tambahkan penjelasan. Tulis hanya nama tempatnya saja.
            """
        )
    else:
        llm_response = ask_llm(
            f"""
            Dari pertanyaan: "{prompt}",
            berikan hanya 1 nama tempat yang spesifik dan cocok untuk dicari di Google Maps.
            Jangan tambahkan penjelasan. Tulis hanya nama tempatnya saja.
            """
        )

    place_data = get_place_info(llm_response)

    return {
        "original_prompt": prompt,
        "llm_source": llm,
        "llm_response": llm_response,
        "maps": place_data
    }
