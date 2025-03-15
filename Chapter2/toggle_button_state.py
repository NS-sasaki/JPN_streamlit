import streamlit as st

# セッションステートの初期化
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

# 状態をトグルするボタン
if st.button('状態を切り替える'):
    st.session_state.button_clicked = not st.session_state.button_clicked

# 現在の状態を表示
st.write("ボタンの状態:", st.session_state.button_clicked)