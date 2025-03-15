import streamlit as st

# ラベル付きのテキスト入力
name = st.text_input("フルネームを入力してください")

# ラベル付きの数値入力
age = st.number_input("年齢を入力してください", min_value=0, max_value=100)