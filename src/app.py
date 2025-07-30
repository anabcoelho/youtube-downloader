import streamlit as st
import requests
import re

PIPED_INSTANCES = [
    "https://pipedapi.kavin.rocks",
    "https://piped.video",
    "https://pipedapi.adminforge.de",
    "https://pipedapi.smnz.de"
]

def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

st.title("YouTube Downloader (via Piped API)")

url = st.text_input("Cole a URL do YouTube")

if st.button("Gerar link de áudio"):
    video_id = extract_video_id(url)
    if not video_id:
        st.error("URL inválida.")
    else:
        for base in PIPED_INSTANCES:
            api_url = f"{base}/streams/{video_id}"
            try:
                resp = requests.get(api_url, timeout=10)
                if resp.status_code == 200:
                    data = resp.json()
                    audio = data.get("audioStreams", [])
                    if audio:
                        stream = audio[0]
                        title = data.get("title", "Áudio do vídeo")
                        st.success(f"🎧 {title}")
                        st.markdown(f"[Clique aqui para baixar o áudio]({stream['url']})")
                        break
            except Exception:
                continue
        else:
            st.error("Nenhuma instância Piped retornou dados. Tente novamente mais tarde.")
