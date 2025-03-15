import streamlit as st

# session_stateにカウンターが存在しない場合は初期化
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# ボタンが押された場合、カウンターを増やす
if st.button("カウンターを増やす"):
    st.session_state.counter += 1

# カウンターの現在の値を表示
st.write("更新されたカウンター値:", st.session_state.counter)