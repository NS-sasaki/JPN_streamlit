import streamlit as st
import re

# メール入力の収集
email = st.text_input("メールアドレスを入力してください:")

# メール形式のバリデーション
if st.button("メールアドレスを検証"):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        st.success("有効なメールアドレスです！")
    else:
        st.error("無効なメール形式です。")