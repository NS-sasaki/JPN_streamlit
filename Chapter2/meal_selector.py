import streamlit as st

# 食事の好み選択用のセレクトボックスを作成
meal = st.selectbox('食事を選択してください', ['朝食', '昼食', '夕食'])

# 選択された食事に応じてメニューの選択肢を変化させる
if meal == '朝食':
    menu_options = ['トースト', 'シリアル', '卵料理', '和食']
elif meal == '昼食':
    menu_options = ['パスタ', 'カレー', 'サンドイッチ', 'ラーメン']
elif meal == '夕食':
    menu_options = ['ステーキ', '寿司', '鍋料理', '中華']

# メニュー選択用のセレクトボックスを作成
menu = st.selectbox('メニューを選択してください', menu_options)

# 選択された食事とメニューを表示
st.write(f"あなたの好み: {meal} - {menu}")