import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def ask_openai(prompt: str) -> str:
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=[
                                                  {"role": "system", "content": "You are a travel assistant."},
                                                  {"role": "user", "content": prompt}
                                              ])
    return response.choices[0].message.content.strip()
