import streamlit as st
import pandas as pd

# サンプルデータ
data = {
    '製品': ['A', 'B', 'C', 'A', 'B', 'C'],
    '売上': [100, 150, 200, 130, 170, 210],
    '月': ['1月', '1月', '1月', '2月', '2月', '2月']
}
df = pd.DataFrame(data)

# 製品を絞り込むためのユーザー入力
product_filter = st.text_input("絞り込む製品名を入力してください:")

# ユーザー入力に基づくデータのフィルタリング
if product_filter:
    filtered_data = df[df['製品'] == product_filter]
else:
    filtered_data = df

st.write("フィルタリングされたデータ:", filtered_data)