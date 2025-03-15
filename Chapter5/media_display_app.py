import streamlit as st

# 画像の表示
st.write("#### 製品画像")
st.image("path/to/your/valid_image.jpg", caption="製品概要")

# 音声の再生
st.write("#### 製品サウンドトラック")
st.audio("path/to/your/audio.mp3", format="audio/mp3")

# 動画の表示
st.write("#### 製品デモ動画")
st.video("path/to/your/video.mp4", format="video/mp4")