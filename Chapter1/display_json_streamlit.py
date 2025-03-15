import streamlit as st

# シンプルなJSONオブジェクトを定義
json_data = {
    "名前": "佐藤　一郎",
    "年齢": 30,
    "市区町村": "大阪"
}

# JSONデータを表示
st.json(json_data)