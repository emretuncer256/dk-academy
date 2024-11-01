import streamlit as st
from ui import login_page
from ui import interests_page
from ui import lessons_page
from ui import topics_pages

if "page" not in st.session_state:
    st.session_state["page"] = 0

if "user" not in st.session_state:
    st.session_state["user"] = None

if "prompt" not in st.session_state:
    st.session_state["prompt"] = None

pages = {0: login_page, 1: interests_page, 2: lessons_page, 3: topics_pages}

pages[st.session_state["page"]]()
