import streamlit as st


def login():
    st.title("Welcome to DK Academy")
    with st.form("login_form"):
        st.header("Login")
        st.text_input("Name")
        st.number_input("Year", step=1, min_value=0)
        st.form_submit_button()
