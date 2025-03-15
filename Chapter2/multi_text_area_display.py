import streamlit as st

# 複数行入力用のテキストエリアを作成
multi_text_area = st.text_area('自己紹介をしてください')

# 入力された自己紹介を表示
if multi_text_area:
    st.write("あなたの自己紹介:")
    st.write(multi_text_area)