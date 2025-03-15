import streamlit as st

# フルーツ選択用のセレクトボックスを作成
fruit = st.selectbox('フルーツを選択してください', ['リンゴ', 'バナナ', 'さくらんぼ'])

# 選択されたフルーツを表示
st.write(f"あなたが選択したフルーツ: {fruit}")