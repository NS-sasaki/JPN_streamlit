import streamlit as st

# ナビゲーション用のサイドバー
st.sidebar.title("タスクマネージャー")
option = st.sidebar.radio("オプションを選択", ["タスクを追加", "タスクを表示"])

# タスクを保存するためのセッションステートを初期化
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

if option == "タスクを追加":
    with st.form(key='task_form'):
        task_name = st.text_input("タスク名")
        task_description = st.text_area("タスクの説明")
        submitted = st.form_submit_button("タスクを追加")
      
        if submitted:
            st.session_state.tasks.append({"name": task_name, "description": task_description})
            st.success("タスクが正常に追加されました！")