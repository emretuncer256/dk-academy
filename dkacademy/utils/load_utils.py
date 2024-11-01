import streamlit as st
import json
import os


@st.cache_data
def load_interests() -> dict:
    try:
        with open(os.getenv("INTERESTS_PATH"), "r", encoding="utf-8") as file:
            interests: dict = json.load(file)
    except FileNotFoundError:
        st.error("The file interests.json was not found.")
        interests = {}
    except json.JSONDecodeError:
        st.error("Error decoding the JSON file.")
        interests = {}
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        interests = {}
    return interests


@st.cache_data
def load_lessons():
    try:
        with open(os.getenv("LESSONS_PATH"), "r", encoding="utf-8") as file:
            lessons: dict = json.load(file)
    except FileNotFoundError:
        st.error("The file lessons.json was not found.")
        lessons = {}
    except json.JSONDecodeError:
        st.error("Error decoding the JSON file.")
        lessons = {}
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        lessons = {}
    return lessons


@st.cache_data
def load_system_instruction():
    try:
        with open(os.getenv("SYSTEM_INSTRUCTION_PATH"), "r",
                  encoding="utf-8") as file:
            instruction: str = file.read()
    except FileNotFoundError:
        st.error("The file system_instruction.txt was not found.")
        instruction = None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        instruction = None
    return instruction
