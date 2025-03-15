import streamlit as st
import pandas as pd

# CSVファイルをDataFrameに読み込む
data = pd.read_csv('data.csv')

# DataFrameを作成
df = pd.DataFrame(data)

# StreamlitアプリでDataFrameを表示
st.dataframe(df)


