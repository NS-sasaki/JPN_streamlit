import streamlit as st
import plotly.express as px
import pandas as pd

# サンプルデータ
data = {
    'x': list(range(100)),
    'y': [i**2 for i in range(100)]
}
df = pd.DataFrame(data)

# ユーザー入力用のスライダー
value_range = st.slider("値の範囲を選択してください:", 0, 100, (25, 75))

# スライダー入力に基づくデータのフィルタリング
filtered_df = df[(df['x'] >= value_range[0]) & (df['x'] <= value_range[1])]

# 動的グラフの作成
fig = px.line(filtered_df, x='x', y='y', title='動的グラフ: y = x^2')

# グラフの表示
st.plotly_chart(fig)