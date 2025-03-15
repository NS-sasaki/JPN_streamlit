import streamlit as st

# 数値入力の収集
number = st.text_input("数値を入力してください:")

# 数値入力のバリデーション
try:
    number = float(number)
    st.success(f"入力された数値は {number} です。")
except ValueError:
    st.error("有効な数値を入力してください。")