import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import japanize_matplotlib

# サンプルデータ
data = {'年': [2018, 2019, 2020, 2021],
        '売上': [200, 250, 300, 350]}

# DataFrameを作成
df = pd.DataFrame(data)

# 棒グラフをプロット
plt.figure(figsize=(8, 4))
plt.bar(df['年'], df['売上'], color='skyblue')
plt.title('年間売上')
plt.xlabel('年')
plt.ylabel('売上')
plt.grid(axis='y')

# Streamlitでプロットを表示
st.pyplot(plt)