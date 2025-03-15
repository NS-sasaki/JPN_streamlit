import pandas as pd
import streamlit as st

# --- ステップ1: CSVファイルを読み込む ---
data = pd.read_csv('sales_data.csv')

# --- ステップ2: '日付'列をdatetime型に変換し、日付のみを抽出 ---
data['日付'] = pd.to_datetime(data['日付']).dt.date

# --- ステップ3: ユニークなカテゴリを取得 ---
categories = data['カテゴリー'].unique()

# --- ステップ4: カテゴリ選択のためのドロップダウンを作成 ---
selected_category = st.selectbox("カテゴリーを選択:", categories)

# --- ステップ5: 選択されたカテゴリに基づいてデータをフィルタリング ---
filtered_data = data[data['カテゴリー'] == selected_category]

# --- ステップ6: 日付範囲スライダーを作成 ---
min_date = filtered_data['日付'].min()
max_date = filtered_data['日付'].max()

start_date, end_date = st.slider(
    "日付範囲を選択:",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

# --- ステップ7: 選択された日付範囲に基づいてデータをフィルタリング ---
date_filtered_data = filtered_data[
    (filtered_data['日付'] >= start_date) & (filtered_data['日付'] <= end_date)
]

# --- ステップ8: フィルタリングされたデータを表示 ---
st.dataframe(date_filtered_data)

# --- ステップ9: メトリクスを計算 ---
total_sales = date_filtered_data['売上'].sum()
average_price = date_filtered_data['価格'].mean()

# --- ステップ10: メトリクスをカラムに表示 ---
col1, col2 = st.columns(2)

with col1:
    st.metric(label="総売上", value=f"¥{total_sales:,.2f}")

with col2:
    st.metric(label="平均価格", value=f"¥{average_price:,.2f}")