import streamlit as st
from models import Content
import json


def learned_page():
    if not st.session_state["content"]:
        st.session_state["page"] = 0
        st.rerun()
    content: Content = st.session_state["content"]

    st.title("Neler Öğrendik?")

    for i, p in enumerate(content.panels, 1):
        st.success(f"{i} - {p.learned}", icon=":material/task_alt:")
    st.balloons()
