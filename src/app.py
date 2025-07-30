import os
import time
import streamlit as st
import yt_dlp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ffmpeg_path = os.path.join(BASE_DIR, '..', 'ffmpeg', 'bin')
output_directory = os.path.join(BASE_DIR, 'downloads')
os.makedirs(BASE_DIR, exist_ok=True)

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{BASE_DIR}/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        mp3_file = os.path.splitext(filename)[0] + ".mp3"
        return mp3_file

st.title("🎵 YouTube Downloader - Áudio MP3")
url = st.text_input("Cole a URL do vídeo do YouTube")

if st.button("Baixar"):
    if url:
        with st.spinner("Baixando e convertendo..."):
            try:
                mp3_path = download_audio(url)
                with open(mp3_path, "rb") as f:
                    st.success("✅ Download concluído!")
                    st.download_button(
                        label="📥 Baixar MP3",
                        data=f.read(),
                        file_name=os.path.basename(mp3_path),
                        mime="audio/mpeg",
                        key="download-btn"
                    )

                # ⚠️ Apagar o arquivo depois de pequeno atraso
                time.sleep(1)  # Espera garantir que download começou
                if os.path.exists(mp3_path):
                    os.remove(mp3_path)
                    st.info("🗑️ Arquivo temporário removido com sucesso.")

            except Exception as e:
                st.error(f"❌ Erro: {e}")
    else:
        st.warning("⚠️ Por favor, insira uma URL válida.")
