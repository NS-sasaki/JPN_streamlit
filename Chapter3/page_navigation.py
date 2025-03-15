import streamlit as st

# ナビゲーション用のサイドバー
st.sidebar.title("ナビゲーション")
page = st.sidebar.radio("移動先を選択", ["Home", "About", "Contact"])

# メインコンテンツ
if page == "Home":
    st.title("ホームページ")
    st.write("メインコンテンツエリアです。")
elif page == "About":
    st.title("概要")
    st.write("コンテンツの概要を説明します。")
elif page == "Contact":
    st.title("お問い合わせ")
    st.write("以下のチャネルを通じてお問い合わせください。")