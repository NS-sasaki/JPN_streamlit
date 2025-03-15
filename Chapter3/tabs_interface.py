import streamlit as st

# タブを作成
tab1, tab2, tab3 = st.tabs(["タブ 1", "タブ 2", "タブ 3"])

# 最初のタブにコンテンツを追加
with tab1:
    st.header("タブ 1です")
    st.write("これは最初のタブのコンテンツです。")

# 2番目のタブにコンテンツを追加
with tab2:
    st.header("タブ 2です")
    st.image("Python.png", caption="タブ 2のサンプル画像")

# 3番目のタブにコンテンツを追加
with tab3:
    st.header("タブ 3です")
    st.write("これは3番目のタブのコンテンツです。")