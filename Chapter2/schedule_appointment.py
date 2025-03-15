import streamlit as st
from datetime import date, time

# スケジューラのタイトルを追加
st.title("スケジューラー")

# 予定の日時入力を作成
appointment_date = st.date_input('予定日を選択してください', date.today())
appointment_time = st.time_input('予定時刻を選択してください', time(9, 0))

# 登録ボタンを追加
if st.button("登録"):
    # 登録された予定を表示
    st.success(f"あなたの予定は: **{appointment_date}** の **{appointment_time}** です。")