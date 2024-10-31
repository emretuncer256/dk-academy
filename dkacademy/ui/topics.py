import streamlit as st
import utils


def topics():
    if not st.session_state["user"]:
        st.session_state["page"] = 0
        st.rerun()

    lesson = st.session_state["prompt"].lesson
    tps = next(ls["topics"] for ls in utils.load_lessons()["lessons"]
               if ls["name"] == lesson)

    st.title("Topics")

    for tp in tps:
        if st.button(tp):
            st.session_state["prompt"].topic = tp
            st.session_state["page"] = 4
            st.rerun()
