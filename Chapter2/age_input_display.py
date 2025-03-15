import streamlit as st

# 数値入力フィールドを作成
age = st.number_input('年齢を入力してください', min_value=0, max_value=120, value=25)

# 入力された年齢を表示
st.write(f"あなたの年齢は: {age}歳です")