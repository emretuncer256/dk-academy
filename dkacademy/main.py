import streamlit as st
from ui import login
from ui import interests

if "page" not in st.session_state:
    st.session_state["page"] = 0

if "user" not in st.session_state:
    st.session_state["user"] = None

pages = {0: login, 1: interests}

pages[st.session_state["page"]]()
