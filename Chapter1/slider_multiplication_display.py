import streamlit as st

# ユーザー入力用のスライダーを作成
number = st.slider("数値を選択してください", 1, 10)

# スライダーの値に基づいて計算を実行
dynamic_result = number * 10

# 動的な結果を表示
st.write(f"{number}に10を掛けた結果は:", dynamic_result)