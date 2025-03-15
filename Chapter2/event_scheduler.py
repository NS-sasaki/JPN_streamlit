import streamlit as st
from datetime import date, time

# 日付と時刻の入力を作成
event_date = st.date_input('イベントの日付を選択してください', date.today())
event_time = st.time_input('イベントの時刻を選択してください', time(14, 30))

# 選択された日付と時刻を表示
st.write(f"イベントは {event_date} の {event_time} に予定されています。")