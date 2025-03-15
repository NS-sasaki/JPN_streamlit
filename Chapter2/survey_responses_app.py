import streamlit as st

# 名前用のテキスト入力
name = st.text_input("名前を入力してください")

# 年齢グループ選択用のラジオボタン
age_group = st.radio("年齢層を選択してください", ["18歳未満", "18-24歳", "25-34歳", "35-44歳", "45歳以上"])

# 興味選択用のチェックボックス
interests = st.multiselect("興味があるもの選択してください", ["テクノロジー", "スポーツ", "音楽", "アート", "旅行"])

# 満足度評価用のスライダー
satisfaction = st.slider("私たちのサービスにどの程度満足していますか？", min_value=1, max_value=10, value=5)

# 回答を表示
st.write("## あなたの回答")
st.write(f"名前: {name}")
st.write(f"年齢層: {age_group}")
st.write(f"興味: {', '.join(interests)}")
st.write(f"満足度評価: {satisfaction}")

# ダウンロード用に回答を準備
responses = f"名前: {name}\n年齢層: {age_group}\n興味: {', '.join(interests)}\n満足度評価: {satisfaction}"

# 回答をダウンロードするためのダウンロードボタンを作成
st.download_button(
    label="回答をダウンロード",
    data=responses,
    file_name='survey_responses.txt',
    mime='text/plain'
)