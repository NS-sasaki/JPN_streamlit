import streamlit as st

# 乗数を初期化
if 'multiplier' not in st.session_state:
    st.session_state.multiplier = 3

# ユーザー入力用のスライダーを作成
base_number = st.slider("基数を選択してください", 1, 100)

# 基数と乗数を使って計算を実行
calculated_value = base_number * st.session_state.multiplier

# 動的な計算結果を表示
st.write(f"{base_number}に{st.session_state.multiplier}を掛けた結果は:", calculated_value)

# 乗数を倍にするボタン
if st.button("乗数を倍にする"):
    st.session_state.multiplier *= 2
    calculated_value = base_number * st.session_state.multiplier
    st.write(f"乗数を倍（{st.session_state.multiplier}）にした計算結果:", calculated_value)