import streamlit as st
import pandas as pd

# サンプルDataFrameを作成
data = pd.DataFrame({
    '名前': ['山田', '里崎', '阿部'],
    '年齢': [25, 30, 35],
    '職業': ['エンジニア', '医者', 'アーティスト']
})

# カスタムの幅と高さでDataFrameを表示
st.dataframe(data, width=500, height=300)