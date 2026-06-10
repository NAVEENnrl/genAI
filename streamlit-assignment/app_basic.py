import streamlit as st

st.title("Welcome to Streamlit!")
name=st.text_input("Enter Yor Name")

if st.button("Greet Me"):
    st.write("hello, ",name)