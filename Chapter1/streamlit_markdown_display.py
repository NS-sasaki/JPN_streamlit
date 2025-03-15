import streamlit as st

# 太字と斜体のテキストを表示
st.markdown("**太字のテキスト**と*斜体のテキスト*")

# 箇条書きリストを作成
st.markdown("""
- アイテム 1
- アイテム 2
- アイテム 3
""")

# ハイパーリンクを追加
st.markdown("[Streamlitドキュメント](https://docs.streamlit.io)")