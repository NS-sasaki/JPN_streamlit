import streamlit as st

# ユーザーからのフィードバックを収集
feedback = st.text_area('フィードバックをお願いします')

# フィードバックを表示
if feedback:
    st.write("フィードバックをありがとうございます！")
    st.write("あなたのフィードバック　：",feedback)