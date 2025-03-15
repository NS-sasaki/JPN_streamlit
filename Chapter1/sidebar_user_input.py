import streamlit as st

# サイドバーにタイトルを追加
st.sidebar.title("サイドバーの例")

# サイドバーにテキスト入力ウィジェットを追加
user_input = st.sidebar.text_input("名前を入力してください:")

# メインコンテンツエリアに入力内容を表示
st.write(user_input,"さん　こんにちは")