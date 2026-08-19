import streamlit as st
from data.dummy_data import STUDENT
from utils.state import logout


def render():
    st.markdown('<div class="ea-heading">Settings</div>', unsafe_allow_html=True)
    st.markdown('<div class="ea-body" style="color:#6B7280;">Account and notification preferences.</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="ea-section">Account</div>', unsafe_allow_html=True)
        st.text_input("Email", value=STUDENT["email"])
        st.text_input("Phone", value=STUDENT["phone"])

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="ea-section">Notifications</div>', unsafe_allow_html=True)
        st.checkbox("Weekly score summary email", value=True)
        st.checkbox("Reminders before an assessment opens", value=True)
        st.checkbox("New job matches", value=False)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    if st.button("Sign out", type="secondary"):
        logout()
        st.rerun()
