import plotly.express as px
import streamlit as st
import pandas as pd

# サンプルデータ
data = {
    '年': [2018, 2019, 2020, 2021],
    '売上': [200, 250, 300, 350]
}

# DataFrameを作成
df = pd.DataFrame(data)

# Plotlyを使用した折れ線グラフの作成
fig = px.line(df, x='年', y='売上')

# Plotlyグラフにラベルを追加する例
fig.update_layout(
    title='年間売上の推移',
    xaxis_title='年',
    yaxis_title='売上'
)

# x軸の目盛りを整数単位に設定
fig.update_xaxes(dtick="1")

st.plotly_chart(fig)