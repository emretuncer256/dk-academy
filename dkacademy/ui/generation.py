import streamlit as st
from models import Prompt, User
from services.prompt_generation import PromptBuilder
from services.content_generation import GeminiService
import os


def check_user_and_prompt():
    if not st.session_state["user"] or not st.session_state["prompt"]:
        st.session_state["page"] = 0
        st.rerun()


def generation_page():
    generated: bool = False
    check_user_and_prompt()
    st.title("Öğrenmeye Hazırlan!")

    prompt = st.session_state["prompt"]

    pb = PromptBuilder()

    if st.button("Başla",
                 use_container_width=True,
                 type="primary",
                 disabled=generated):
        st.session_state["page"] = 5
        st.rerun()

    if st.button("Eğitimi Üret", use_container_width=True):

        pb.build(prompt)

        with st.spinner("Hikaye üretiliyor..."):
            model = GeminiService(pb.system_instruction)
            content = model.generate_content(pb.prompt)
            st.text("Hikaye üretildi")

        content.save()
        st.session_state["content"] = content
        st.session_state["next_panel"] = 1
        st.session_state["content_folder"] = content.content_folder

        for panel in content.panels:
            os.makedirs(
                os.path.join(content.content_folder, "images",
                             f"panel_{panel.panel_number}"))
        with st.spinner("İlk sayfa hazırlanıyor..."):
            for i, vp in enumerate(content.panels[0].visual_prompts):
                st.session_state["image_model"].generate_image(
                    vp,
                    os.path.join(content.content_folder, "images", "panel_1",
                                 f"{i}.png"))
            generated = True
