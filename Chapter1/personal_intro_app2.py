import streamlit as st
import pandas as pd

# アプリのメインタイトルを設定
st.title("私の個人紹介ページへようこそ")

# 簡単な紹介文を書く
st.write("こんにちは！私は[あなたの名前]です。自己紹介をさせていただきます。")

# 趣味のDataFrameを作成
hobbies = pd.DataFrame({
    '趣味': ['読書', '旅行', '料理', '写真'],
    '説明': [
        '本を通じて新しい世界を知る。',
        '新しい場所を訪れ、異なる文化を体験する。',
        'レシピを試す。',
        'レンズを通して瞬間を捉える。'
    ]
})

# 趣味のテーブルを表示
st.header("私のお気に入りの趣味")
st.table(hobbies)

# 画像を表示
st.header("私の干支")
st.image("path/to/your/image.jpg", caption="This image represents my Japanese zodiac animal")

# サイドバーにラジオボタンを追加
st.sidebar.title("連絡方法")
contact_method = st.sidebar.radio("好きな連絡方法:", ["メール", "電話", "SNS"])

# 選択した連絡方法を表示
st.write(f"あなたの好きな連絡方法は、 {contact_method}")

