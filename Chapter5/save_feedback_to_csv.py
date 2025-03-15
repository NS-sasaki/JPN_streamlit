import streamlit as st
import os
import pandas as pd

# --- ステップ1: ユーザー入力の収集 ---
name = st.text_input("あなたの名前を入力してください:")
feedback = st.text_area("あなたのフィードバックを入力してください:")

# --- ステップ2: データを保存する関数 ---
def save_to_csv(name, feedback):
    # データフレームの作成
    df = pd.DataFrame([[name, feedback]], columns=["名前", "フィードバック"])

    # CSVにデータを保存（ファイルが存在する場合は追加、存在しない場合は新規作成）
    if not os.path.isfile("user_feedback.csv"):
        df.to_csv("user_feedback.csv", mode='w', header=True, index=False)
    else:
        df.to_csv("user_feedback.csv", mode='a', header=False, index=False)

# --- ステップ3: 保存ボタンの追加 ---
if st.button("フィードバックを保存"):
    if name and feedback:  # 入力が空でないことを確認
        save_to_csv(name, feedback)
        st.success("フィードバックが保存されました！")
    else:
        st.error("保存する前に両方の欄を入力してください。")