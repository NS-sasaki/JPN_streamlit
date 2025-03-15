import streamlit as st

# 範囲を選択するためのスライダーを作成
range_values = st.slider('範囲を選択してください', min_value=0, max_value=100, value=(25, 75))

# 選択された範囲を表示
st.write(f"選択した範囲: {range_values[0]} から {range_values[1]} まで")