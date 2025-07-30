import streamlit as st
from pytube import YouTube
import re

st.title("YouTube Downloader (link direto do navegador)")

url = st.text_input("Cole a URL do YouTube")

def is_valid_youtube_url(url):
    youtube_regex = r"(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+"
    return re.match(youtube_regex, url)

if st.button("Gerar link de download"):
    if not is_valid_youtube_url(url):
        st.error("URL inválida. Certifique-se de colar o link completo do vídeo do YouTube.")
    else:
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            st.success("Link de download gerado com sucesso!")
            st.markdown(f"[Clique aqui para baixar o áudio]({stream.url})")
        except Exception as e:
            st.error(f"Erro ao processar vídeo: {e}")
