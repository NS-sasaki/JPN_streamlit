import streamlit as st
import pandas as pd

# ファイルアップローダーを作成
uploaded_file = st.file_uploader('CSVファイルをアップロードしてください', type='csv')

# アップロードされたファイルを処理
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("ファイルの内容:")
    st.dataframe(df)
  
    # 特定の列の合計を計算して表示
    column_to_sum = st.selectbox('合計を計算する列を選択してください', df.columns)
    column_sum = df[column_to_sum].sum()
    st.write(f"{column_to_sum} の合計: {column_sum}")