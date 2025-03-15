import streamlit as st

# メトリクスを表示
st.metric(label="気温", value="20 ℃", delta="1.2 ℃")
st.metric(label="湿度", value="45%", delta="-3%")