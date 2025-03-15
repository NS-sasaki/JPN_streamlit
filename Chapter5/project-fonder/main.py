import streamlit as st

st.set_page_config(
    page_title="マルチページアプリ",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("メインページ")
st.write("マルチページアプリです。サイドバーからアクセスしたいページに移動してください。")