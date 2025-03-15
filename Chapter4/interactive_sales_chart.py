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

# インタラクティブな折れ線グラフを作成
fig = px.line(df, x='年', y='売上', title='年間売上')

# x軸の目盛りを整数単位に設定
fig.update_xaxes(dtick="1")

# StreamlitでPlotlyチャートを表示
st.plotly_chart(fig)