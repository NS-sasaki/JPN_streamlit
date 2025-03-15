import streamlit as st

# ヘルプテキスト付きのテキスト入力
email = st.text_input("メールアドレス", help="有効なメールアドレスを入力してください。")

# ヘルプテキスト付きのスライダー
rating = st.slider("サービスを評価してください", 1, 5, help="1 = 不満, 5 = 非常に満足")