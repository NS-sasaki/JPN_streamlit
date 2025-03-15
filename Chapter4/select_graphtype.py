# 1. ライブラリのインポート
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import japanize_matplotlib

# 2. サンプルデータの作成
# サンプルデータ
data = {'年': [2018, 2019, 2020, 2021],
        '売上': [200, 250, 300, 350]}

# DataFrameを作成
df = pd.DataFrame(data)

# 3. ユーザー入力ウィジェットの追加
# グラフタイプのユーザー入力
graph_type = st.radio("グラフの種類を選択:", ('折れ線', '棒'))

# データ範囲のユーザー入力
year_range = st.slider("年の範囲を選択:", min_value=2018, max_value=2021, value=(2018, 2021))

# 4. ユーザー入力に基づいてデータをフィルタリング
# 選択された年の範囲に基づいてデータをフィルタリング
filtered_data = df[(df['年'] >= year_range[0]) & (df['年'] <= year_range[1])]

# 5. グラフを動的にプロット
# グラフタイプに基づいて条件付きでプロット
plt.figure(figsize=(8, 4))

if graph_type == '折れ線':
    plt.plot(filtered_data['年'], filtered_data['売上'], marker='o')
    plt.title('年間売上（折れ線グラフ）')
else:
    plt.bar(filtered_data['年'], filtered_data['売上'], color='skyblue')
    plt.title('年間売上（棒グラフ）')

# ラベル、グリッドを追加し、表示
plt.xlabel('年')
plt.ylabel('売上')
plt.grid(True)

# x軸の目盛りをデータに含まれる年のみを目盛りとして表示するよう設定
plt.xticks(filtered_data['年'])

# Streamlitでプロットを表示
st.pyplot(plt)