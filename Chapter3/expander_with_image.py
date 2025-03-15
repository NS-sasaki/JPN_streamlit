import streamlit as st

# 折りたたみ可能なセクションを作成
with st.expander("詳細情報"):
    st.write("これは隠すことも表示することもできる追加のコンテンツです。")
    st.image("Python.png", caption="サンプル画像")