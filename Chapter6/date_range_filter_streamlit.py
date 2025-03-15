import pandas as pd
import streamlit as st
import datetime

# CSVファイルをDataFrameにロード
data = pd.read_csv('sales_data.csv')

# '日付'列をdatetime型に変換し、日付のみを抽出
data['日付'] = pd.to_datetime(data['日付']).dt.date

# データからユニークなカテゴリを取得
categories = data['カテゴリー'].unique()

# カテゴリ選択のためのドロップダウンを作成
selected_category = st.selectbox("カテゴリを選択:", categories)

# 選択されたカテゴリに基づいてデータをフィルタリング
filtered_data = data[data['カテゴリー'] == selected_category]

# 最小および最大の日付を取得
min_date = filtered_data['日付'].min()
max_date = filtered_data['日付'].max()

# 日付範囲スライダーを作成
start_date, end_date = st.slider(
    "日付範囲を選択:",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

# 選択された日付範囲に基づいてデータをフィルタリング
date_filtered_data = filtered_data[
    (filtered_data['日付'] >= start_date) & (filtered_data['日付'] <= end_date)
]

# フィルタリングされたデータを表示
st.dataframe(date_filtered_data)