import streamlit as st
import pandas as pd

# サンプルDataFrame
data = {'名前': ['山田', '里崎', '阿部'], '年齢': [25, 30, 35]}
df = pd.DataFrame(data)

# フィルタリングされたデータの例
filtered_df = df[df['年齢'] > 28]

# フィルタリングされたDataFrameをCSVに変換
filtered_csv = filtered_df.to_csv(index=False)

# フィルタリングされたデータ用のダウンロードボタンを作成
st.download_button(
    label="フィルタリングされたデータをダウンロード",
    data=filtered_csv,
    file_name='filtered_data.csv',
    mime='text/csv'
)