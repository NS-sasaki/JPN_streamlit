import streamlit as st
from datetime import time

# 時刻入力フィールドを作成
selected_time = st.time_input('時刻を選択してください', time(12, 0))

# 選択された時刻を表示
st.write(f"選択した時刻: {selected_time}")