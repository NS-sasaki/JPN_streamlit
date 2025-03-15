import streamlit as st

# ラベルとキャプション付きのテキスト入力
email = st.text_input("メールアドレス")
st.caption("注：メールアドレスはアカウント確認のみに使用されます。")