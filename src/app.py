import streamlit as st
import yt_dlp
import tempfile
import os
import shutil

st.title("YouTube Audio Downloader com yt-dlp (Áudio Original)")

url = st.text_input("Insira a URL do YouTube").strip()

if st.button("Baixar áudio"):
    if not url:
        st.error("Por favor, insira uma URL válida.")
    else:
        temp_dir = tempfile.mkdtemp()
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/115.0.0.0 Safari/537.36',
                'nocheckcertificate': True,
                'quiet': True,
                'postprocessors': [],  # Sem conversão, só baixar áudio original
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            # Procura o arquivo baixado
            files = os.listdir(temp_dir)
            audio_files = [f for f in files if f.endswith(('.webm', '.m4a', '.opus', '.mp4'))]

            if not audio_files:
                st.error("Arquivo de áudio não encontrado após o download.")
            else:
                audio_path = os.path.join(temp_dir, audio_files[0])
                with open(audio_path, "rb") as f:
                    st.download_button("Clique para baixar o áudio", f, file_name=audio_files[0])

        except Exception as e:
            st.error(f"Erro ao baixar: {e}")

        finally:
            shutil.rmtree(temp_dir)
