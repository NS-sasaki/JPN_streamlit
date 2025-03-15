import streamlit as st

# ファイルアップローダーを作成
uploaded_file = st.file_uploader('ファイルをアップロードしてください', type=['csv', 'txt'])

# アップロードされたファイル名を表示
if uploaded_file is not None:
    st.write(f"アップロードされたファイル: {uploaded_file.name}")