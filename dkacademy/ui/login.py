import streamlit as st
from models import User


def login():
    st.title("DK Akademi ile Maceraya Hazır Mısın?")
    with st.form(key="user_info_form"):
        st.header("Kullanıcı Girişi")
        name = st.text_input("İsim")
        age = st.number_input("Yaş", step=1, min_value=0)
        gender = st.radio("Cinsiyet", ["Erkek", "Kız"], index=None, horizontal=True)

        submit_button = st.form_submit_button(label="Başla")
        if submit_button:
            if not name or not age:
                st.warning("Lütfen tüm bilgileri giriniz!")
            else:
                st.session_state["user"] = User(name, age, gender)
                st.session_state["page"] = 1
                st.rerun()
