import streamlit as st

# 画像表示用のチェックボックスを作成
show_image = st.checkbox('画像を表示')

# 条件付きで画像を表示
if show_image:
    st.image('path/to/image.jpg', caption='Sample Image')

# チャート表示用の別のチェックボックスを作成
show_chart = st.checkbox('チャートを表示')

# 条件付きでチャートを表示
if show_chart:
    st.line_chart([1, 2, 3, 4, 5])