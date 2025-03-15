import streamlit as st

# 温度を選択するためのスライダーを作成
temperature = st.slider('温度を選択してください', min_value=-50, max_value=50, value=20)

# 選択された温度を表示
st.write(f"選択した温度: {temperature}°C")