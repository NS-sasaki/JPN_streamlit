import streamlit as st

# ネストされたJSONオブジェクトを定義
nested_json_data = {
    "ユーザー": {
        "名前": "小田　ルリ子",
        "年齢": 28,
        "住所": {
            "番地": "123 令和町",
            "市区町村": "名古屋",
            "都道府県": "愛知"
        }
    }
}

# ネストされたJSONデータを表示
st.json(nested_json_data)