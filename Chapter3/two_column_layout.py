import streamlit as st

# カスタム幅のカラムを作成
# 比率を指定してカラムの幅を調整
col1, col2 = st.columns([1, 2])

with col1:
    st.write("このカラムは狭めです。")

with col2:
    st.write("このカラムは広めです。")