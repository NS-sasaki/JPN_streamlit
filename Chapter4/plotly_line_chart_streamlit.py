import plotly.express as px
import streamlit as st
import pandas as pd

data = {
    '年': [2018, 2019, 2020, 2021, 2022],
    '売上': [200, 250, 300, 350, 400],
    '地域': ['北', '南', '東', '西', '北']
}

# DataFrameを作成
df = pd.DataFrame(data)

# Plotlyを使用した折れ線グラフの例
fig = px.line(df, x='年', y='売上', title='年間売上の推移')

# x軸の目盛りを整数単位に設定
fig.update_xaxes(dtick="1")

st.plotly_chart(fig)