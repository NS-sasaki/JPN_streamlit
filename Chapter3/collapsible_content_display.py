import streamlit as st

# 折りたたみセクションにさらにコンテンツを追加
with st.expander("詳細"):
    st.header("折りたたみヘッダー")
    st.write("ここに詳細な説明やデータがあります。")
    st.code("""
def example_function():
    return "これは折りたたみセクション内のコードブロックです。"
""")