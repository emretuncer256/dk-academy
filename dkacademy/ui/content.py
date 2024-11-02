import streamlit as st
from models.content import Content, Panel, Question
import os


def check_content():
    if not st.session_state["content"]:
        st.session_state["page"] = 0
        st.rerun()


def content_page():
    check_content()
    st.set_page_config(layout="wide")
    finished: bool = False
    next_panel: int = st.session_state["next_panel"]
    content: Content = st.session_state["content"]
    content_folder: str = content.content_folder
    panel: Panel = content.panels[next_panel - 1]

    images_path = os.path.join(content_folder, "images")

    panel_path = os.path.join(images_path, f"panel_{panel.panel_number}")
    images = [
        os.path.join(panel_path, f"{i}.png")
        for i in range(len(panel.visual_prompts))
    ]

    add_question(panel.question)

    st.title(f"{content.title} - {next_panel}")

    with st.container(border=True):
        cols = st.columns(2)
        with cols[0]:
            st.image(images[0])
        with cols[1]:
            st.image(images[1])

    st.write(panel.story)

    # Next Panel Generation
    if content.panels[-1].panel_number == panel.panel_number:
        st.session_state["page"] = 0
        st.rerun()

    if next_panel != content.panels[-1].panel_number:
        next_panel += 1
        with st.spinner("Sonraki sayfa oluşturuluyor..."):
            for i, vp in enumerate(content.panels[next_panel -
                                                  1].visual_prompts):
                st.session_state["image_model"].generate_image(
                    vp,
                    os.path.join(images_path, f"panel_{next_panel}",
                                 f"{i}.png"))
    else:
        finished = True
    if st.button("İlerle", on_click=go_next, args=(next_panel, finished)):
        st.rerun()


def go_next(next_panel, finished):
    if finished:
        st.session_state["page"] = 6
    else:
        st.session_state["next_panel"] = next_panel


def add_question(question: Question):
    st.sidebar.title("Soru")
    st.sidebar.header(question.question)
    for a in question.answers:
        answer = st.button(a)
        if answer and a == question.correct_answer:
            st.sidebar.success("Tebrikler! Doğru Cevapladın.")
        else:
            st.sidebar.error("Yanlış Cevap.", icon=":material/error:")
            st.sidebar.info(question.explanation, icon=":material/info:")
