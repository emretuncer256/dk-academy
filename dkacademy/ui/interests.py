import streamlit as st

interests = str
interests_values = {
    interests : None,    
}

def interests():
    st.title("İlgi Alanlarınız")
    with st.form("interests_form"):
        interests_values["interests"] = st.text_input(label="İlgi Alanınızı Yazın", value=str, max_chars=20)

        submit_button = st.form_submit_button("Kaydet")