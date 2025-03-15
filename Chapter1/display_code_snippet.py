import streamlit as st

# シンプルなPython関数を定義
code = '''
def greet(name):
    return f"こんにちは、{name}！"
'''

# シンタックスハイライト付きでコードブロックを表示
st.code(code, language='python')