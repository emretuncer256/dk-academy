import streamlit as st
import json
import os


@st.cache_data
def load_interests() -> dict:
    try:
        with open(os.getenv("INTERESTS_PATH"), "r") as file:
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
def load_lectures():
    try:
        with open(os.getenv("LECTURES_PATH"), "r") as file:
            lectures: dict = json.load(file)
    except FileNotFoundError:
        st.error("The file interests.json was not found.")
        lectures = {}
    except json.JSONDecodeError:
        st.error("Error decoding the JSON file.")
        lectures = {}
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        lectures = {}
    return lectures
