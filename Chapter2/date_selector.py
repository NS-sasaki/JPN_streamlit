import streamlit as st
from datetime import date

# 日付入力フィールドを作成
selected_date = st.date_input('日付を選択してください', date.today())

# 選択された日付を表示
st.write(f"選択した日付: {selected_date}")