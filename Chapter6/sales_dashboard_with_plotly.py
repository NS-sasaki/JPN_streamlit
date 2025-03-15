import pandas as pd
import streamlit as st
import plotly.express as px

# --- ステップ1: CSVファイルを読み込む ---
data = pd.read_csv('sales_data.csv')

# --- ステップ2: '日付'列をdatetime形式に変換し、日付のみにする ---
data['日付'] = pd.to_datetime(data['日付']).dt.date

# --- ステップ3: ユニークなカテゴリを取得する ---
categories = data['カテゴリー'].unique()

# --- ステップ4: カテゴリ選択のためのドロップダウンを作成 ---
selected_category = st.selectbox("カテゴリーを選択:", categories)

# --- ステップ5: 日付範囲スライダーを作成 ---
min_date = data['日付'].min()  # datetime.date 型になる
max_date = data['日付'].max()  # datetime.date 型になる

start_date, end_date = st.slider(
    "日付範囲を選択:",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

# --- ステップ6: 選択されたカテゴリに基づいてデータをフィルタリング ---
filtered_data = data[data['カテゴリー'] == selected_category]

# --- ステップ7: 選択された日付範囲に基づいてデータをフィルタリング ---
date_filtered_data = filtered_data[
    (filtered_data['日付'] >= start_date) & 
    (filtered_data['日付'] <= end_date)
]

# --- ステップ8: フィルタリングされたデータを表示 ---
st.dataframe(date_filtered_data)

# --- ステップ9: メトリクスを計算する ---
total_sales = date_filtered_data['売上'].sum()
average_price = date_filtered_data['価格'].mean()

# --- ステップ10: メトリクスをカラムに表示する ---
col1, col2 = st.columns(2)

with col1:
    st.metric(label="総売上", value=f"¥{total_sales:,.2f}")
with col2:
    st.metric(label="平均価格", value=f"¥{average_price:,.2f}")

# --- ステップ11: カラムにグラフを表示する ---
col1, col2 = st.columns(2)

with col1:
    # --- 売上トレンド用の折れ線グラフ ---
    line_chart = px.line(
        date_filtered_data,
        x='日付',
        y='売上',
        title='売上の時系列変化（トレンド）',
        labels={'売上': '売上 (¥)', '日付': '日付'}
    )
    st.plotly_chart(line_chart)

with col2:
    # --- カテゴリ別売上用の棒グラフ ---
    # 日付範囲でフィルタリング
    period_category_sales = data[
        (data['日付'] >= start_date) & 
        (data['日付'] <= end_date)
    ]
    # カテゴリーごとに売上を集計
    category_sales = period_category_sales.groupby('カテゴリー')['売上'].sum().reset_index()

    bar_chart = px.bar(
        category_sales,
        x='カテゴリー',
        y='売上',
        title='カテゴリ別の売上',
        labels={'売上': '売上 (¥)', 'カテゴリー': 'カテゴリ'}
    )
    st.plotly_chart(bar_chart)