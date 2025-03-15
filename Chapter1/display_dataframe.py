import streamlit as st
import pandas as pd

# シンプルなDataFrameを作成
data = pd.DataFrame({
    '列 1': [1, 2, 3],
    '列 2': ['A', 'B', 'C']
})

# DataFrameを表示
st.write(data)