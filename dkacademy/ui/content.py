import streamlit as st
from models.content import Content, Panel
import os


def check_content():
    if not st.session_state["content"]:
        st.session_state["page"] = 0
        st.rerun()


def content_page():
    next_panel: int = st.session_state["next_panel"]
    content: Content = st.session_state["content"]
    content_folder: str = content.content_folder
    panel: Panel = content.panels[next_panel]

    images_path = os.path.join(content_folder, "images")

    panel_path = os.path.join(images_path, f"panel_{panel.panel_number}")
    images = [
        os.path.join(panel_path, f"{i}.png")
        for i in range(len(panel.visual_prompts))
    ]

    st.title(f"{content.title} - {next_panel}")

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

    with st.spinner("Sonraki sayfa oluşturuluyor..."):
        next_panel += 1
        for i, vp in content.panels[next_panel].visual_prompts:
            st.session_state["image_model"].generate_image(
                vp, os.path.join(images_path, f"panel_{next_panel}",
                                 f"{i}.png"))
    if st.button("İlerle"):
        st.session_state["next_panel"] = next_panel
        st.rerun()
