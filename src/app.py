import streamlit as st
import requests

st.title("YouTube Downloader (via Invidious)")

url = st.text_input("Cole a URL do YouTube")

def extract_video_id(url):
    import re
    # Match padrão para YouTube
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

if st.button("Gerar link de download"):
    video_id = extract_video_id(url)
    if not video_id:
        st.error("URL inválida.")
    else:
        try:
            # Usar uma instância pública do Invidious
            invidious_url = f"https://yewtu.be/api/v1/videos/{video_id}"
            response = requests.get(invidious_url)
            if response.status_code == 200:
                video_info = response.json()
                title = video_info['title']
                audio_streams = [s for s in video_info['formatStreams'] if 'audio' in s['type']]
                if audio_streams:
                    audio_url = audio_streams[0]['url']
                    st.success(f"{title}")
                    st.markdown(f"[Clique aqui para baixar o áudio]({audio_url})")
                else:
                    st.error("Nenhuma faixa de áudio encontrada.")
            else:
                st.error("Erro ao buscar informações do vídeo.")
        except Exception as e:
            st.error(f"Erro: {e}")
