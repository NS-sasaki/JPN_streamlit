import streamlit as st

# サイドバーにスライダーを追加
age = st.sidebar.slider("年齢を選択してください:", 0, 100, 25)

# サイドバーにセレクトボックスを追加
occupation = st.sidebar.selectbox("職業を選択してください:", ["エンジニア", "医者", "アーティスト"])

# 選択したオプションをメインコンテンツエリアに表示
st.write("年齢:", age)
st.write("職業:", occupation)