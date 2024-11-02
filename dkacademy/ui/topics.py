import streamlit as st
import utils


def topics_pages():
    if not st.session_state["user"]:
        st.session_state["page"] = 0
        st.rerun()

    lesson = st.session_state["prompt"].lesson
    topics = next(ls["topics"] for ls in utils.load_lessons()["lessons"]
               if ls["name"] == lesson)

    st.title("Konular")

    for topic in topics:
        if st.button(topic):
            st.session_state["prompt"].topic = topic
            st.session_state["page"] = 4
            st.rerun()
