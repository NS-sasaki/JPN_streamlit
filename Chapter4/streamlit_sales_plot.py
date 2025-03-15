import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import japanize_matplotlib  # 日本語化ライブラリ

# サンプルデータ
data = {'年': [2018, 2019, 2020, 2021],
        '売上': [200, 250, 300, 350]}

# DataFrameを作成
df = pd.DataFrame(data)

# 折れ線グラフをプロット
plt.figure(figsize=(8, 4))
plt.plot(df['年'], df['売上'], marker='o')
plt.title('年間売上')
plt.xlabel('年')
plt.ylabel('売上')
plt.grid(True)

# x軸の目盛りをデータに含まれる年のみを目盛りとして表示するよう設定
plt.xticks(df['年'])

# Streamlitでプロットを表示
st.pyplot(plt)