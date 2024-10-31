import streamlit as st
from ui import login
from ui import interests
from ui import lessons
from ui import topics

if "page" not in st.session_state:
    st.session_state["page"] = 0

if "user" not in st.session_state:
    st.session_state["user"] = None

if "prompt" not in st.session_state:
    st.session_state["prompt"] = None

pages = {0: login, 1: interests, 2: lessons, 3: topics}

pages[st.session_state["page"]]()
