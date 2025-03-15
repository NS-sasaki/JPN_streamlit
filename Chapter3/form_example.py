import streamlit as st

# フォームの作成
with st.form(key='my_form'):
    name = st.text_input("名前を入力してください")
    age = st.number_input("年齢を入力してください", min_value=0, max_value=120)
    submitted = st.form_submit_button("送信")
  
    if submitted:
        st.success(f"こんにちは、{name}さん！あなたは{age}歳ですね。")