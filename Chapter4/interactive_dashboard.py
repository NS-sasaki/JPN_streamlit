import streamlit as st
import pandas as pd
import plotly.express as px

# サンプルデータ
data = {
    '年': [2018, 2019, 2020, 2021],
    '売上': [200, 250, 300, 350],
    '地域': ['北', '南', '東', '西']
}

# DataFrameを作成
df = pd.DataFrame(data)

# インタラクティブな棒グラフを作成
fig = px.bar(df, x='年', y='売上', color='地域', title='地域別年間売上')

# 2カラムのレイアウトを作成
col1, col2 = st.columns(2)

# カラム1にチャートを表示
with col1:
    st.plotly_chart(fig)

# カラム2にDataFrameを表示
with col2:
    st.dataframe(df)