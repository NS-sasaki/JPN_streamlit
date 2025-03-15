import pandas as pd
import streamlit as st

# CSVファイルをDataFrameにロード
data = pd.read_csv('sales_data.csv')

# データからユニークなカテゴリを取得
categories = data['カテゴリー'].unique()

# カテゴリ選択のためのドロップダウンを作成
selected_category = st.selectbox("カテゴリーを選択:", categories)

# 選択されたカテゴリに基づいてデータをフィルタリング
filtered_data = data[data['カテゴリー'] == selected_category]

# フィルタリングされたデータを表示
st.write(f"{selected_category}のデータ:")
st.dataframe(filtered_data)

