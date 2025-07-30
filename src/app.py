import streamlit as st
import requests
import re

INSTANCES = [
    "https://invidious.snopyta.org",
    "https://yewtu.be",
    "https://invidious.kavin.rocks",
    "https://invidious.tube",
    "https://vid.mint.lgbt"
]

def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

st.title("YouTube Downloader (via Invidious Instâncias)")

url = st.text_input("Cole a URL do YouTube")

if st.button("Gerar link de download"):
    video_id = extract_video_id(url)
    if not video_id:
        st.error("URL inválida.")
    else:
        for base in INSTANCES:
            api_url = f"{base}/api/v1/videos/{video_id}"
            try:
                resp = requests.get(api_url, timeout=10)
                if resp.status_code == 200:
                    js = resp.json()
                    streams = [s for s in js.get("formatStreams", []) if "audio" in s.get("type", "")]
                    if streams:
                        st.success(f"🎧 {js.get('title')}")
                        st.markdown(f"[Clique aqui para baixar o áudio]({streams[0]['url']})")
                        break
                    else:
                        st.error("Nenhuma faixa de áudio encontrada.")
                        break
            except Exception:
                continue
        else:
            st.error("Nenhuma instância Invidious respondeu corretamente. Tente novamente mais tarde.")
