import streamlit as st
import subprocess
import os

st.title("YouTube Audio Downloader com yt-dlp")

url = st.text_input("Insira a URL do YouTube")

if st.button("Baixar áudio"):
    try:
        out_file = "audio.mp3"
        cmd = [
            "yt-dlp",
            "-x", "--audio-format", "mp3",
            "-o", out_file,
            url,
        ]
        subprocess.run(cmd, check=True)
        with open(out_file, "rb") as f:
            st.download_button("Clique para baixar o áudio", f, file_name=out_file)
        os.remove(out_file)
    except Exception as e:
        st.error(f"Erro ao baixar: {e}")
