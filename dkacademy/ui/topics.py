import streamlit as st


def topics():
    st.title("Topics")
    st.write(st.session_state["user"])
    st.write(st.session_state["prompt"])
