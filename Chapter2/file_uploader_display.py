import streamlit as st
import pandas as pd

# ファイルアップローダーを作成
uploaded_file = st.file_uploader('ファイルをアップロードしてください', type=['csv', 'txt'])

# ファイルがアップロードされたか確認
if uploaded_file is not None:
    # ファイルをDataFrameに読み込む
    df = pd.read_csv(uploaded_file)
  
    # DataFrameを表示
    st.write("ファイルの内容:")
    st.dataframe(df)