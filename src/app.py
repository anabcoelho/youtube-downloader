import streamlit as st
import subprocess
import os

st.title("YouTube Audio Downloader com yt-dlp")

url = st.text_input("Insira a URL do YouTube").strip()

if st.button("Baixar áudio"):
    if not url:
        st.error("Por favor, insira uma URL válida.")
    else:
        try:
            output_template = "%(title)s.%(ext)s"
            cmd = [
                "yt-dlp",
                "-x", "--audio-format", "mp3",
                "-o", output_template,
                url,
            ]
            subprocess.run(cmd, check=True)
            # Encontra o arquivo mp3 gerado
            files = [f for f in os.listdir() if f.endswith(".mp3")]
            if not files:
                st.error("Arquivo de áudio não encontrado após o download.")
            else:
                audio_file = files[0]
                with open(audio_file, "rb") as f:
                    st.download_button("Clique para baixar o áudio", f, file_name=audio_file)
                os.remove(audio_file)
        except subprocess.CalledProcessError as e:
            st.error(f"Erro no yt-dlp: {e}")
