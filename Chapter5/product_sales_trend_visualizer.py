import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# サンプルデータ
data = {
    '製品': ['A', 'B', 'C', 'A', 'B', 'C'],
    '売上': [100, 150, 200, 130, 170, 210],
    '月': ['1月', '1月', '1月', '2月', '2月', '2月']
}
df = pd.DataFrame(data)

# 製品を絞り込むためのユーザー入力
product_filter = st.text_input("絞り込む製品名を入力してください:")

# ユーザー入力に基づくデータのフィルタリング
if product_filter:
    filtered_data = df[df['製品'] == product_filter]
else:
    filtered_data = df

st.write("フィルタリングされたデータ:", filtered_data)

# 月ごとの合計売上を計算
monthly_sales = filtered_data.groupby('月')['売上'].sum()

# グラフのプロット
fig, ax = plt.subplots()
ax.plot(monthly_sales.index, monthly_sales.values, marker='o')
ax.set_title(f"製品{product_filter}の月別合計売上トレンド")
ax.set_xlabel("月")
ax.set_ylabel("合計売上")

# グラフの表示
st.pyplot(fig)
