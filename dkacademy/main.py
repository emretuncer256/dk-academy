import streamlit as st
from ui import login_page, interests_page, lessons_page, topics_pages, generation_page, content_page, learned_page
import utils
import os

os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'

if "page" not in st.session_state:
    st.session_state["page"] = 0

if "user" not in st.session_state:
    st.session_state["user"] = None

if "prompt" not in st.session_state:
    st.session_state["prompt"] = None

if "content" not in st.session_state:
    st.session_state["content"] = None

if "next_panel" not in st.session_state:
    st.session_state["next_panel"] = None

if "image_model" not in st.session_state:
    st.session_state["image_model"] = utils.load_model()

if "first_page_generated" not in st.session_state:
    st.session_state["first_page_generated"] = False

pages = {
    0: login_page,
    1: interests_page,
    2: lessons_page,
    3: topics_pages,
    4: generation_page,
    5: content_page,
    6: learned_page
}

pages[st.session_state["page"]]()

# TODO: Last page returns login page. Fix it
# TODO: Questions will be displayed
# TODO: The prompt will be improved
