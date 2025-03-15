import streamlit as st

# デフォルト選択付きのマルチセレクトウィジェットを作成
fruits = st.multiselect('好きなフルーツを選択してください', ['リンゴ', 'バナナ', 'さくらんぼ', 'デーツ'], default=['リンゴ', 'デーツ'])

# 選択されたフルーツを表示
st.write(f"選択したフルーツ: {', '.join(fruits)}")