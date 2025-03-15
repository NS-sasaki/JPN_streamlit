import streamlit as st
import pandas as pd
import time

# --- ステップ1: サンプルデータの準備 ---
data = {
    '年': [2018, 2019, 2020, 2021, 2022],
    '売上': [200, 250, 300, 350, 400],
    '地域': ['北', '南', '東', '西', '北']
}

# DataFrameを作成
df = pd.DataFrame(data)
# --- ステップ2: データの読み込みのキャッシングの実装 ---

# データの読み込み関数をキャッシュ
@st.cache_data
def load_data():
    # 時間のかかる操作をシミュレート
    time.sleep(2)  # データ処理をシミュレートするために2秒の遅延を追加
    return df.copy()

# --- ステップ3: キャッシングをテストするためのボタンの追加 ---

# データを読み込むボタン
if st.button("データを読み込む"):
    cached_data = load_data()  # キャッシュされたデータをロード

    # キャッシュされたデータを表示
    st.write("キャッシュされたデータ:")
    st.dataframe(cached_data)