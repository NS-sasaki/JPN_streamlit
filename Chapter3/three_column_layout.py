import streamlit as st

# 3つのカラムを作成
col1, col2, col3 = st.columns(3)

# 最初のカラムにコンテンツを追加
with col1:
    st.header("カラム 1")
    st.write("これは最初のカラムのテキストです。")

# 2番目のカラムにコンテンツを追加
with col2:
    st.header("カラム 2")
    st.image("python.png", caption="サンプル画像")

# 3番目のカラムにコンテンツを追加
with col3:
    st.header("カラム 3")
    st.write("これは3番目のカラムのテキストです。")