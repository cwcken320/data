import streamlit as st

st.title("我的第一個 App")
st.write("Streamlit 測試成功！")

name = st.text_input("你叫咩名？")
if name:
    st.success(f"你好，{name}！")
