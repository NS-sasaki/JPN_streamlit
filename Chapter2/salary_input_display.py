import streamlit as st

# 特定のステップサイズとフォーマットを設定した数値入力を作成
salary = st.number_input('給与を入力してください', min_value=0, step=1000, format="%d")

# 入力された給与を表示
st.write(f"あなたの給与は: ¥{salary}")