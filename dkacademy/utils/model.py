from services.image_generation import SDXLGenerator
import streamlit as st


@st.cache_resource
def load_model() -> SDXLGenerator:
    return SDXLGenerator()
