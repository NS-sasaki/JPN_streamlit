import streamlit as st
import pandas as pd

# 趣味のDataFrameを作成
hobbies = pd.DataFrame({
    '趣味': ['読書', '旅行', '料理', '写真'],
    '説明': [
        '本を通じて新しい世界を知る。',
        '新しい場所を訪れ、異なる文化を体験する。',
        'レシピを試す。',
        'レンズを通して瞬間を捉える。'
    ]
})

# 趣味を表形式で表示
st.header("私のお気に入りの趣味")
st.table(hobbies)