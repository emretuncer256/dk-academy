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
    st.title("Generation")

    user = User("Emre", 7, "Erkek", ["Bitkiler"])
    prompt = Prompt(user, "Matematik", "Zaman Ölçme")

    st.write(user)
    st.write(prompt)
    pb = PromptBuilder()

    if st.button("Eğitimi Üret"):

        pb.build(prompt)

        model = GeminiService(pb.system_instruction)
        content = model.generate_content(pb.prompt)
        content_folder = content.save()
        st.session_state["content"] = content
        st.write(content)
        for panel in content.panels:
            os.makedirs(
                os.path.join(content_folder, "images",
                             f"panel_{panel.panel_number}"))
            for i ,vp in enumerate(panel.visual_prompts):
                st.session_state["image_model"].generate_image(
                    vp,
                    os.path.join(content_folder, "images", f"panel_{panel.panel_number}", f"{i}.png")
                )
