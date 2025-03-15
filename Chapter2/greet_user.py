import streamlit as st

# テキスト入力フィールドを作成
name = st.text_input('あなたの名前を入力してください')

# 入力された名前を表示
if name:
    st.write(f"こんにちは、{name}さん！")