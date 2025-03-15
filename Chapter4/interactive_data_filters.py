import streamlit as st
import pandas as pd

# サンプルデータ
data = {
    '年': [2018, 2019, 2020, 2021, 2022],
    '売上': [200, 250, 300, 350, 400],
    '地域': ['北', '南', '東', '西', '北']
}

# DataFrameを作成
df = pd.DataFrame(data)

# 年フィルターのユーザー入力
year_filter = st.multiselect("年を選択してください:", options=df['年'].unique(), default=df['年'].unique())

# 地域フィルターのユーザー入力
region_filter = st.multiselect("地域を選択してください:", options=df['地域'].unique(), default=df['地域'].unique())