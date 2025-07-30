from pytube import YouTube
import streamlit as st

st.title("YouTube Downloader (sem servidor!)")

url = st.text_input("Cole a URL do YouTube")

if st.button("Gerar link de download"):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        st.success(f"Download direto disponível:")
        st.markdown(f"[Clique aqui para baixar o áudio]({stream.url})")
    except Exception as e:
        st.error(f"Erro: {e}")
