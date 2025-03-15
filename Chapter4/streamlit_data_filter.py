import streamlit as st
import pandas as pd

# サンプルデータ
data = {
    '年': [2018, 2019, 2020, 2021],
    '売上': [200, 250, 300, 350],
    '地域': ['北', '南', '東', '西']
}

# DataFrameを作成
df = pd.DataFrame(data)

# 年フィルターのユーザー入力
year_filter = st.multiselect("年を選択してください:", options=df['年'].unique(), default=df['年'].unique())

# 地域フィルターのユーザー入力
region_filter = st.multiselect("地域を選択してください:", options=df['地域'].unique(), default=df['地域'].unique())

# ユーザー入力に基づいてデータをフィルタリング
filtered_data = df[(df['年'].isin(year_filter)) & (df['地域'].isin(region_filter))]

# フィルタリングされたデータをStreamlitアプリで表示
st.dataframe(filtered_data)