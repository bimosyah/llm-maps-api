import requests
import os
from dotenv import load_dotenv

load_dotenv()
LLM_ENDPOINT = os.getenv("LLM_ENDPOINT", "http://localhost:1234/v1")

def ask_llm(prompt: str) -> str:
    response = requests.post(
        f"{LLM_ENDPOINT}/chat/completions",
        headers={"Content-Type": "application/json"},
        json={
            "model": "mistral",
            "messages": [
                {"role": "system", "content": "You are a travel assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
