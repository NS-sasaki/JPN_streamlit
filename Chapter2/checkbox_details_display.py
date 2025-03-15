import streamlit as st

# チェックボックスを作成
show_details = st.checkbox('詳細を表示')

# 条件付きでコンテンツを表示
if show_details:
    st.write("こちらが詳細です")