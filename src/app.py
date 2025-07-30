import streamlit as st
import subprocess
import os

st.title("YouTube Audio Downloader com yt-dlp (Áudio Original)")

url = st.text_input("Insira a URL do YouTube").strip()

if st.button("Baixar áudio"):
    if not url:
        st.error("Por favor, insira uma URL válida.")
    else:
        try:
            output_template = "%(title)s.%(ext)s"
            cmd = [
                "yt-dlp",
                "-x",  # Extrai só o áudio
                "-o", output_template,
                url,
            ]
            subprocess.run(cmd, check=True)

            # Procura arquivo de áudio gerado
            audio_files = [f for f in os.listdir() if f.endswith((".webm", ".m4a", ".opus", ".mp4"))]
            if not audio_files:
                st.error("Não foi possível encontrar o arquivo de áudio após o download.")
            else:
                audio_file = audio_files[0]
                with open(audio_file, "rb") as f:
                    st.download_button("Clique para baixar o áudio", f, file_name=audio_file)
                os.remove(audio_file)
        except subprocess.CalledProcessError as e:
            st.error(f"Erro no yt-dlp: {e}")
