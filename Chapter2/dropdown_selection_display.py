import streamlit as st

# 動的なオプションのリスト
options = ['オプション 1', 'オプション 2', 'オプション 3', 'オプション 4']
selected_option = st.selectbox('オプションを選択してください', options)

# 選択されたオプションを表示
st.write(f"あなたが選択したオプション: {selected_option}")