import streamlit as st
from models import Content
import json


def learned_page():
    # if not st.session_state["content"]:
    #     st.session_state["page"] = 0
    #     st.rerun()
    # content: Content = st.session_state["content"]
    with open(r"contents\20241101160027\content.json", "r") as f:
        content = Content.from_json(json.load(f))

    st.title("Neler Öğrendik?")

    for i, p in enumerate(content.panels, 1):
        st.success(f"{i} - {p.learned}", icon=":material/task_alt:")
    st.balloons()
