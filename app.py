import requests
import streamlit as st

st.set_page_config(page_title="LLM Comparison - Local vs OpenAI", layout="wide")
st.title("🗺️ Compare Local LLM vs OpenAI for Location-Based Prompts")
st.write(
    "Masukkan pertanyaan seperti 'tempat makan enak di Jakarta' lalu bandingkan hasil dari **Local LLM (via LM Studio)** dan **OpenAI GPT**.")

query = st.text_input("Tulis pertanyaan lokasi:")


def fetch_from_backend(prompt, source):
    try:
        response = requests.get("http://localhost:8000/search", params={
            "prompt": prompt,
            "llm": source
        })
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


if query:
    col1, col2 = st.columns(2)

    with st.spinner("Meminta jawaban dari Local LLM..."):
        local_data = fetch_from_backend(query, "local")
    with col1:
        st.subheader("📦 mistralai/mathstral-7b-v0.1 (via LM Studio)")
        if "error" in local_data:
            st.error(f"Gagal: {local_data['error']}")
        else:
            st.markdown(f"**Prompt:** {local_data.get('original_prompt')}")
            st.markdown(f"**Jawaban LLM:** {local_data.get('llm_response')}")
            maps = local_data.get("maps", {})
            if "name" in maps:
                st.markdown(f"**Nama Tempat:** {maps.get('name')}")
                st.markdown(f"**Alamat:** {maps.get('address')}")
                st.markdown(f"[🧭 Buka di Google Maps]({maps.get('maps_url')})")
                st.components.v1.iframe(maps.get("embed_url", ""), height=450)

    with st.spinner("Meminta jawaban dari OpenAI GPT..."):
        openai_data = fetch_from_backend(query, "openai")
    with col2:
        st.subheader("☁️ OpenAI API gpt-3.5-turbo")
        if "error" in openai_data:
            st.error(f"Gagal: {openai_data['error']}")
        else:
            st.markdown(f"**Prompt:** {openai_data.get('original_prompt')}")
            st.markdown(f"**Jawaban LLM:** {openai_data.get('llm_response')}")
            maps = openai_data.get("maps", {})
            if "name" in maps:
                st.markdown(f"**Nama Tempat:** {maps.get('name')}")
                st.markdown(f"**Alamat:** {maps.get('address')}")
                st.markdown(f"[🧭 Buka di Google Maps]({maps.get('maps_url')})")
                st.components.v1.iframe(maps.get("embed_url", ""), height=450)
