import streamlit as st
import pandas as pd

# サンプルデータ
data = {'名前': ['山田', '里崎', '阿部'], '年齢': [25, 30, 35]}
df = pd.DataFrame(data)

# DataFrameをCSVに変換
csv = df.to_csv(index=False)

# ダウンロードボタンを作成
st.download_button(
    label="データをダウンロード",
    data=csv,
    file_name='sample_data.csv',
    mime='text/csv'
)