import pandas as pd
import streamlit as st

# サンプルデータからDataFrameを作成
data = pd.DataFrame({
    'カテゴリ': ['フルーツ', '野菜', 'フルーツ', '野菜'],
    '項目': ['リンゴ', 'にんじん', 'バナナ', 'ブロッコリー']
})

# カテゴリフィルタ用のマルチセレクトウィジェットを作成
categories = st.multiselect('フィルタするカテゴリを選択してください', data['カテゴリ'].unique())

# 選択されたカテゴリに基づいてデータをフィルタリング
filtered_data = data[data['カテゴリ'].isin(categories)]

# フィルタリングされたデータを表示
st.write("フィルタリングされた項目:")
st.write(filtered_data)