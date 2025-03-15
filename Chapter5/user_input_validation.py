import streamlit as st

# ユーザー入力の収集
name = st.text_input("名前を入力してください:")
age = st.number_input("年齢を入力してください:", min_value=0, max_value=120)

# 入力のバリデーション
if st.button("送信"):
    if not name:
        st.error("名前は必ず入力してください。")
    elif age <= 0:
        st.error("年齢は0より大きい値を入力してください。")
    else:
        st.success("ご入力ありがとうございました。")