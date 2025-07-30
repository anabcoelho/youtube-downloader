import streamlit as st
from pytube import YouTube
import os

st.title("YouTube Downloader (via pytube)")

url = st.text_input("Insira a URL do YouTube")

if st.button("Baixar áudio"):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        filename = yt.title + ".mp4"
        audio_stream.download(filename=filename)
        with open(filename, "rb") as f:
            st.download_button("Clique para baixar o áudio", f, file_name=filename)
        os.remove(filename)
    except Exception as e:
        st.error(f"Erro ao baixar: {e}")
