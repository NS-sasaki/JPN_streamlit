import streamlit as st

# カウンターを初期化
counter = 0

# 現在のカウンター値を表示
st.write("現在のカウンター値:", counter)

# カウンターを増やすボタン
if st.button("カウンターを増やす"):
    counter += 1
    st.write("更新されたカウンター値:", counter)