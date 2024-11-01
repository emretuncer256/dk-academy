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
    check_user_and_prompt()
    st.title("Generation")

    user = st.session_state["user"]
    prompt = st.session_state["prompt"]

    st.write(user)
    st.write(prompt)
    pb = PromptBuilder()
    
    if st.button("Başla", use_container_width=True):
        st.session_state["page"] = 5
        st.rerun()

    if st.button("Eğitimi Üret"):

        pb.build(prompt)

        model = GeminiService(pb.system_instruction)
        content = model.generate_content(pb.prompt)
        st.write(content)

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
