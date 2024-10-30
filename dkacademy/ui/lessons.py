import streamlit as st


def lessons():
    if not st.session_state["user"]:
        st.session_state["page"] = 0
        st.rerun()
    st.title("Dersler")

    cols = st.columns(4)

    for i, col in enumerate(cols):
        with col:
            with st.container(border=True):
                st.image("math.webp", use_column_width=True)
                st.button(f"{i} Matematik",
                          use_container_width=True,
                          type="primary")
