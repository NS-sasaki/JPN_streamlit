import streamlit as st

def display_header():
    st.title("My Streamlit App")

def display_sidebar():
    st.sidebar.title("サイドバー")
    user_input = st.sidebar.text_input("名前を入力してください:")
    return user_input