import streamlit as st
import pandas as pd

# サンプルデータ
data = {
    '年': [2018, 2019, 2020, 2021, 2022],
    '売上': [200, 250, 300, 350, 400],
    '地域': ['北', '南', '東', '西', '北']
}

# DataFrameを作成
df = pd.DataFrame(data)

# 年範囲でフィルタリング
year_range = st.slider("年の範囲を選択:", min_value=2018, max_value=2022, value=(2018, 2022))

# 選択された年範囲に基づいてフィルタを適用
filtered_df = df[(df['年'] >= year_range[0]) & (df['年'] <= year_range[1])]

# フィルタリングされたデータに基づいてメトリックを計算
total_sales = filtered_df['売上'].sum()
average_sales = filtered_df['売上'].mean()

# メトリックを表示
st.metric(label="売上の合計", value=f"¥{total_sales:,.2f}")
st.metric(label="売上の平均", value=f"¥{average_sales:,.2f}")

# フィルタリングされたデータを表示
st.write("フィルタリングされたデータ:")
st.dataframe(filtered_df)