import streamlit as st


def login():
    st.title("DK Akademi ile Maceraya Hazır Mısın?")
    with st.form("login_form"):
        st.header("Kullanıcı Girişi")
        st.text_input("İsim")
        st.number_input("Yaş", step=1, min_value=0)
        st.multiselect("Hangileri ilgini çekiyor?", ["uzay", "doğa", "tatil"])
        st.form_submit_button("Başla")
