import streamlit as st
from datetime import date

# 日付範囲を選択するための日付入力を作成
date_range = st.date_input('日付の範囲を選択してください', [date.today(), date.today()])

# 範囲が選択されていることを確認
if len(date_range) == 2:
    start_date, end_date = date_range
    st.write(f"選択した日付の範囲: {start_date} から {end_date} まで")
else:
    st.error("開始日と終了日を選択してください。")