import streamlit as st

# ナビゲーション用のラジオボタンをサイドバーに追加
page = st.sidebar.radio("移動先を選択:", ["Home", "About", "Contact"])

# 選択されたページに基づいてコンテンツを表示
if page == "Home":
    st.write("ホームページへようこそ！")
elif page == "About":
    st.write("これは概要のページです。")
else:
    st.write("お問い合わせは contact@example.com まで。")