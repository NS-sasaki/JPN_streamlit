import streamlit as st

# 複数行のコードスニペット
multi_line_code = '''
def add(a, b):
    return a + b

result = add(5, 3)
print("合計は:", result)
'''

# 複数行のコードブロックを表示
st.code(multi_line_code, language='python')