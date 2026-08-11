import os
import sys

import streamlit as st

APP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, APP_DIR)

from utils.state import init_state
from components.navigation import render_sidebar, render_mobile_bottom_nav
from screens import login, dashboard, profile
# Assessment, Score, Skill Gap, Roadmap, Certifications, Career Suggestions,
# Analytics, Reports and Settings are already written (screens/*.py) but not
# wired in yet - that's next session's work, not today's. See progress.md.

st.set_page_config(page_title="EmployaAI", page_icon="🎓", layout="wide", initial_sidebar_state="expanded")

with open(os.path.join(APP_DIR, "assets", "styles.css")) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

init_state()

if not st.session_state.authenticated:
    login.render()
    st.stop()

page = st.session_state.page
render_sidebar(page)

SCREENS = {
    "dashboard": dashboard.render,
    "profile": profile.render,
}

SCREENS[page]()

render_mobile_bottom_nav(page)
