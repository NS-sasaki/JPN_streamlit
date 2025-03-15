import streamlit as st

# 言語切り替え用のトグルスイッチを作成
language = st.toggle("言語を切り替え", value=False)

# 言語に基づいてコンテンツを表示
if language:
    st.write("こんにちは、はじめまして！")  # 日本語で表示
else:
    st.write("Hello, World!")  # 英語で表示