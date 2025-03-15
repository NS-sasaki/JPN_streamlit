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

# インタラクティブな棒グラフを作成
fig = px.bar(df, x='年', y='売上', title='年間売上')

# チャートをカスタマイズ
fig.update_traces(marker=dict(color='royalblue'))
fig.update_layout(title='Plotlyによる年間売上',
                  xaxis_title='年',
                  yaxis_title='売上')

# x軸の目盛り間隔を1に設定
fig.update_xaxes(dtick="1")

# StreamlitでカスタマイズされたPlotlyチャートを表示
st.plotly_chart(fig)