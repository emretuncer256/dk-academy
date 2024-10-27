import streamlit as st

form_values = {
    "isim" : None,
    "yaş" : None,
    "ilgi_alanları" : None, 
}

def login():
    st.title("DK Akademi ile Maceraya Hazır Mısın?")
    with st.form(key="user_info_form"):
        st.header("Kullanıcı Girişi")
        form_values["isim"] = st.text_input("İsim")
        form_values["yaş"] = st.number_input("Yaş", step=1, min_value=0)
        form_values["ilgi_alanları"] = st.multiselect("Hangileri ilgini çekiyor?", ["uzay", "doğa", "tatil"])

        submit_button = st.form_submit_button(label="Başla")
        if not all(form_values.values()):
            st.warning("Lütfen tüm bilgileri giriniz!")
        else:
            st.balloons()
            st.write("### Info")
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")