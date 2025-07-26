import requests
import streamlit as st

st.title("🗺️ LLM Travel Assistant")
query = st.text_input("Mau ke mana hari ini?")

if query:
    st.write("Sedang mencari...")
    res = requests.get("http://localhost:8000/search", params={"prompt": query})
    data = res.json()
    if "error" in data.get("maps", {}):
        st.error("Tempat tidak ditemukan.")
    else:
        st.success(f"📍 {data['maps']['name']}")
        st.write(f"Alamat: {data['maps']['address']}")
        st.markdown(f"[Buka di Google Maps]({data['maps']['maps_url']})")
        st.components.v1.iframe(data['maps']['embed_url'], height=450)
