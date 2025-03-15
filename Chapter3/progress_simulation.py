import streamlit as st
import time  # 進捗をシミュレートするためにtimeをインポート

# 進捗バーを作成
progress_bar = st.progress(0)

# 長時間実行されるタスクをシミュレート
for percent_complete in range(101):
    # 何らかの計算やタスクを実行
    time.sleep(0.1)  # 時間の遅延をシミュレート

    # 進捗バーを更新
    progress_bar.progress(percent_complete)