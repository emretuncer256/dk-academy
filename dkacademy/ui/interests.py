import streamlit as st
from utils import load_interests
from models.prompt import Prompt


def interests_page():
    interests = load_interests()
    if not st.session_state["user"]:
        st.session_state["page"] = 0
        st.rerun()

    st.title("İlgi Alanınız")

    cols = st.columns(3)
    for i, interest in enumerate(interests.values()):
        col = cols[i % 3]
        with col:
            st.image(interest["image"])
            interest["status"] = st.button(interest["name"],
                                           use_container_width=True)

    for i in interests.values():
        if i["status"]:
            st.session_state["user"].interests = [i["name"]]
            st.session_state["prompt"] = Prompt(st.session_state["user"])
            st.session_state["page"] = 2
            st.rerun()
