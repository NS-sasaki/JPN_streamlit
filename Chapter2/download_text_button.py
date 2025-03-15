import streamlit as st

# カスタムテキストコンテンツ
text_content = "こんにちは！\nこれはサンプルのテキストファイルです。"

# テキストコンテンツ用のダウンロードボタンを作成
st.download_button(
    label="テキストをダウンロード",
    data=text_content,
    file_name='sample_text.txt',
    mime='text/plain'
)