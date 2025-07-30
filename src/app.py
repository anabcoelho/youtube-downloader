import streamlit as st
import subprocess
import os
import tempfile
import shutil

st.title("YouTube Audio Downloader com yt-dlp (Áudio Original)")

url = st.text_input("Insira a URL do YouTube").strip()

if st.button("Baixar áudio"):
    if not url:
        st.error("Por favor, insira uma URL válida.")
    else:
        temp_dir = tempfile.mkdtemp()
        try:
            output_template = os.path.join(temp_dir, "%(title)s.%(ext)s")
            cmd = [
                "yt-dlp",
                "-x",
                "-o", output_template,
                url,
            ]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                st.error(f"Erro no yt-dlp:\n{result.stderr}")
            else:
                # Procura o arquivo baixado na pasta temporária
                files = os.listdir(temp_dir)
                audio_files = [f for f in files if f.endswith((".webm", ".m4a", ".opus", ".mp4"))]
                if not audio_files:
                    st.error("Arquivo de áudio não encontrado após o download.")
                else:
                    audio_path = os.path.join(temp_dir, audio_files[0])
                    with open(audio_path, "rb") as f:
                        st.download_button("Clique para baixar o áudio", f, file_name=audio_files[0])
        finally:
            shutil.rmtree(temp_dir)
