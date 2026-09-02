import streamlit as st

# Screens actually wired into the running app. Nav only ever shows entries
# for screens in this set - no dead links, no "coming soon" pages.
LIVE_SCREENS = {
    "dashboard", "profile", "assessment", "score", "skill_gap", "roadmap",
    "certifications", "careers", "analytics", "reports", "settings",
}

_ALL_NAV_ITEMS = [
    ("MAIN", [
        ("dashboard", "Dashboard", None),
        ("profile", "Profile", "74%"),
        ("assessment", "Assessment", None),
    ]),
    ("INSIGHTS", [
        ("score", "Employability Score", None),
        ("skill_gap", "Skill Gap", "7"),
        ("roadmap", "Learning Roadmap", None),
        ("certifications", "Certifications", None),
        ("careers", "Career Suggestions", None),
    ]),
    ("OUTPUT", [
        ("analytics", "Analytics", None),
        ("reports", "Reports", None),
        ("settings", "Settings", None),
    ]),
]

NAV_ITEMS = [
    (group, [item for item in items if item[0] in LIVE_SCREENS])
    for group, items in _ALL_NAV_ITEMS
]
NAV_ITEMS = [(group, items) for group, items in NAV_ITEMS if items]


def init_state():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "page" not in st.session_state:
        st.session_state.page = "dashboard"
    reset_assessment_state()


def reset_assessment_state():
    if "assessment_domain" not in st.session_state:
        st.session_state.assessment_domain = None
    if "assessment_difficulty" not in st.session_state:
        st.session_state.assessment_difficulty = None
    if "assessment_submitted" not in st.session_state:
        st.session_state.assessment_submitted = False
    if "assessment_current_q" not in st.session_state:
        st.session_state.assessment_current_q = 0
    if "assessment_answers" not in st.session_state:
        st.session_state.assessment_answers = {}


def go_to(page: str):
    st.session_state.page = page


def logout():
    st.session_state.authenticated = False
    st.session_state.page = "dashboard"
    st.session_state.assessment_domain = None
    st.session_state.assessment_difficulty = None
    st.session_state.assessment_submitted = False
    st.session_state.assessment_current_q = 0
    st.session_state.assessment_answers = {}
