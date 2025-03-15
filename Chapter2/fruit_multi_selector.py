import streamlit as st

# マルチセレクトウィジェットを作成
fruits = st.multiselect('好きなフルーツを選択してください', ['リンゴ', 'バナナ', 'さくらんぼ', 'デーツ'])

# 選択されたフルーツを表示
st.write(f"選択したフルーツ: {', '.join(fruits)}")