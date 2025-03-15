import pandas as pd
import streamlit as st

# CSVファイルをDataFrameにロード
data = pd.read_csv('sales_data.csv')

# DataFrame全体をインタラクティブに表示
st.write("インタラクティブな売上データテーブル:")
st.dataframe(data)