import streamlit as st
import pandas as pd

# サンプルDataFrame
data = {'名前': ['山田', '里崎', '阿部'], '年齢': [25, 30, 35]}
df = pd.DataFrame(data)

# 平均年齢を計算
average_age = df['年齢'].mean()

# 分析結果用のダウンロードボタンを作成
analysis_result = f"平均年齢は: {average_age}歳です。"
st.download_button(
    label="分析結果をダウンロード",
    data=analysis_result,
    file_name='analysis_result.txt',
    mime='text/plain'
)