import streamlit as st
from pytube import YouTube
from pytube.cli import on_progress
import os

st.title("YouTube Audio Downloader com pytube")

url = st.text_input("Cole a URL do YouTube")

if st.button("Baixar áudio"):
    if not url:
        st.error("Por favor, insira uma URL válida.")
    else:
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            audio_stream = yt.streams.filter(only_audio=True).order_by("abr").desc().first()
            if not audio_stream:
                st.error("Não foi possível encontrar stream de áudio.")
            else:
                filename = f"{yt.title}.mp4"
                # Faz o download para arquivo local
                audio_stream.download(filename=filename)
                # Oferece botão de download no Streamlit
                with open(filename, "rb") as f:
                    st.download_button("Clique para baixar o áudio", f, file_name=filename)
                # Remove arquivo depois do download
                os.remove(filename)
        except Exception as e:
            st.error(f"Erro ao baixar áudio: {e}")
