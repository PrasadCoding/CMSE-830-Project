import streamlit as st

st.title('Hello World')

st.write('Hello world!')
st.markdown("<h1 style='text-align: left; color: red;'>Some title</h1>", unsafe_allow_html=True)
st.sidebar.success("Select a page")
