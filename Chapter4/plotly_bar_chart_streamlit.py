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

# Plotlyを使用した棒グラフの例
fig = px.bar(df, x='地域', y='売上', title='地域別売上')


st.plotly_chart(fig)