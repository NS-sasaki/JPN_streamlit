import streamlit as st

# ラジオボタングループを作成
color = st.radio('色を選択してください', ['赤', '緑', '青'])

# 選択された色を表示
st.write(f"あなたが選択した色: {color}")