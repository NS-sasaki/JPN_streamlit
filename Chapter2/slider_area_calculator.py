import streamlit as st

# パラメータ用のスライダーを作成
length = st.slider('長さ[m]', min_value=0.0, max_value=10.0, value=5.0)
width = st.slider('幅[m]', min_value=0.0, max_value=10.0, value=3.0)

# 面積を計算して表示
area = length * width
st.write(f"計算された面積: {area} 平方メートル")