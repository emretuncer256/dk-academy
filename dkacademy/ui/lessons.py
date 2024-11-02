import streamlit as st
import utils
import os


def lessons_page():
    if not st.session_state["user"]:
        st.session_state["page"] = 0
        st.rerun()

    lessons = utils.load_lessons()

    st.title("Dersler")

    cols = st.columns(3)

    for i, lesson in enumerate(lessons["lessons"]):
        col = cols[i % 3]
        with col:
            with st.container(border=True):
                if lesson["image"]:
                    st.image(os.path.join("assets", lesson["image"]),
                             use_column_width=True)
                if st.button(lesson["name"],
                             use_container_width=True,
                             type="primary"):
                    st.session_state["prompt"].lesson = lesson["name"]
                    st.session_state["page"] = 3
                    st.rerun()
