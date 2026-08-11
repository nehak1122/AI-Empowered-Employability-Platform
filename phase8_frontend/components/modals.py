import streamlit as st


def confirm_dialog(title: str, body: str, confirm_label: str, on_confirm=None):
    @st.dialog(title)
    def _inner():
        st.write(body)
        c1, c2 = st.columns(2)
        if c1.button("Keep going", width="stretch"):
            st.rerun()
        if c2.button(confirm_label, type="primary", width="stretch"):
            if on_confirm:
                on_confirm()
            st.rerun()
    _inner()


def success_dialog(title: str, body: str, action_label: str):
    @st.dialog(title)
    def _inner():
        st.markdown(f"### ✅ {title}")
        st.write(body)
        if st.button(action_label, type="primary", width="stretch"):
            st.rerun()
    _inner()
