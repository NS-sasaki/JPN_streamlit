import streamlit as st

# 動的なリスト
options = ['オプション 1', 'オプション 2', 'オプション 3', 'オプション 4']
selected_options = st.multiselect('オプションを選択してください', options)

# 選択されたオプションを表示
st.write(f"選択したオプション: {', '.join(selected_options)}")