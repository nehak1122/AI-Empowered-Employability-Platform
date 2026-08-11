import streamlit as st

# Screens actually wired into the running app today. Nav only ever shows
# entries for screens in this set - no dead links, no "coming soon" pages.
# skill_gap.py, roadmap.py, certifications.py, careers.py, analytics.py,
# reports.py, assessment.py and score.py already exist and work (see
# progress.md) but aren't switched on here yet - that's the next session's
# work, not today's.
LIVE_SCREENS = {"dashboard", "profile"}

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


def go_to(page: str):
    st.session_state.page = page


def logout():
    st.session_state.authenticated = False
    st.session_state.page = "dashboard"
