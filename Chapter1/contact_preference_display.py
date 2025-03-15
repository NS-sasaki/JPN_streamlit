import streamlit as st

# サイドバーにラジオボタンを追加
st.sidebar.title("連絡方法")
contact_method = st.sidebar.radio("好きな連絡方法:", ["メール", "電話", "SNS"])

# 選択した連絡方法を表示
st.write(f"あなたの好きな連絡方法は、 {contact_method}")