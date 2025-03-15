import streamlit as st
import pandas as pd

# CSVファイルをDataFrameにロード
data = pd.read_csv('sales_data.csv')

# 静的なテーブルを表示
st.write("静的な売上データテーブル:")
st.table(data.head(10))