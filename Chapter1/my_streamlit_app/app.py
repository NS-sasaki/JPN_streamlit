import streamlit as st
from data_processing import load_data, clean_data
from ui_elements import display_header, display_sidebar
import config

# データを読み込んで加工
data = load_data(config.DATA_FILE)
cleaned_data = clean_data(data)

# UI要素を設定
st.set_page_config(page_title=config.APP_TITLE)
display_header()
user_name = display_sidebar()

# データを表示
st.write(f"こんにちは、{user_name}さん！")
st.dataframe(cleaned_data)