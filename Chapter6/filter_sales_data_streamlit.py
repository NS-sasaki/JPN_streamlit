import pandas as pd
import streamlit as st
import plotly.express as px

# --- ステップ1: CSVファイルを読み込む ---
data = pd.read_csv('sales_data.csv')

# --- ステップ2: '日付'列をdatetime形式に変換し、日付のみにする ---
data['日付'] = pd.to_datetime(data['日付']).dt.date

# --- ステップ3: ユニークなカテゴリを取得する ---
categories = data['カテゴリー'].unique()

# --- サイドバーコンテンツ ---
# --- ステップ4:サイドバーの作成 ---
st.sidebar.header("フィルター")

# --- ステップ5: カテゴリー選択のドロップダウンをサイドバーに配置し、データをフィルタリング ---
selected_category = st.sidebar.selectbox(
    "カテゴリーを選択:", 
    categories,
    help="売上データをフィルタリングするカテゴリーを選択してください。"
)
category_data = data[data['カテゴリー'] == selected_category]

# --- ステップ6: 日付範囲スライダーをサイドバーに配置 ---
min_date = data['日付'].min()
max_date = data['日付'].max()

start_date, end_date = st.sidebar.slider(
    "日付範囲を選択:",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    help="日付範囲を選択してデータをフィルタリングしてください。"
)
# --- ステップ7: 日付範囲でデータをフィルタリング ---
filtered_data = category_data[
    (category_data['日付'] >= start_date) & 
    (category_data['日付'] <= end_date)
]

# --- ステップ8: メトリクスをサイドバーに表示 ---
total_sales = filtered_data['売上'].sum()
average_price = filtered_data['価格'].mean()

st.sidebar.metric(label="総売上", value=f"¥{total_sales:,.2f}")
st.sidebar.metric(label="平均価格", value=f"¥{average_price:,.2f}")

# --- フィルタリングされたデータをCSV形式に変換 ---
csv_data = filtered_data.to_csv(index=False, encoding='utf-8-sig')

# --- ダウンロードボタン ---
st.sidebar.download_button(
    label="フィルタリングされたデータをCSVでダウンロード",
    data=csv_data,
    file_name='filtered_data.csv',
    mime='text/csv'
)

# --- メインコンテンツ ---

# --- ステップ9:メインコンテンツをグラフ用にカラムで分割 ---
col1, col2 = st.columns(2)

# --- ステップ10: 折れ線グラフを左側のカラムに表示 ---
with col1:
    st.subheader("売上トレンド")
    line_chart = px.line(
        filtered_data,
        x='日付',
        y='売上',
        title='売上の時系列変化（トレンド）',
        labels={'売上': '売上 (¥)', '日付': '日付'}
    )
    st.plotly_chart(line_chart)

# --- 棒グラフを右側のカラムに表示 ---
with col2:
    st.subheader("カテゴリー別売上")
    # 日付範囲でフィルタリング
    period_category_sales= data[
        (data['日付'] >= start_date) & 
        (data['日付'] <= end_date)
    ]
    # カテゴリーごとに売上を集計
    category_sales = period_category_sales.groupby('カテゴリー')['売上'].sum().reset_index()

    bar_chart = px.bar(
        category_sales,
        x='カテゴリー',
        y='売上',
        title='対象期間のカテゴリ別の売上',
        labels={'売上': '売上 (¥)', 'カテゴリー': 'カテゴリ'}
    )
    st.plotly_chart(bar_chart)