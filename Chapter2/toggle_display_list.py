import streamlit as st

# リスト表示用のチェックボックスを作成
show_list = st.checkbox('リストを表示')

# 条件付きで項目のリストを表示
if show_list:
    st.write("こちらがアイテムのリストです:")
    st.write(["アイテム1", "アイテム2", "アイテム3"])