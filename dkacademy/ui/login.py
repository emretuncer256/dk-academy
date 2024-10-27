import streamlit as st


def login():
    st.title("DK Akademi ile Maceraya Hazır Mısın?")
    with st.form("login_form"):
        st.header("Kullanıcı Girişi")
        isim = st.text_input("İsim")
        yaş = st.number_input("Yaş", step=1, min_value=0)
        ilgi_alanları = st.multiselect("Hangileri ilgini çekiyor?", ["uzay", "doğa", "tatil"])
        submit_button = st.form_submit_button("Başla")
