import streamlit as st
from data.dummy_data import STUDENT
from utils.state import NAV_ITEMS, LIVE_SCREENS, go_to


def render_sidebar(current_page: str):
    with st.sidebar:
        st.markdown(
            '<div style="display:flex;align-items:center;gap:8px;padding:8px 4px 16px 4px;">'
            '<div style="width:28px;height:28px;border-radius:8px;background:#6C5CE7;'
            'display:flex;align-items:center;justify-content:center;font-weight:700;color:#fff;">E</div>'
            '<span class="ea-sidebar-wordmark-text" style="font-weight:600;color:#fff;">EmployaAI</span>'
            '</div>',
            unsafe_allow_html=True,
        )

        for group_label, items in NAV_ITEMS:
            st.markdown(f'<div class="ea-nav-group-label">{group_label}</div>', unsafe_allow_html=True)
            for key, label, count in items:
                active = key == current_page
                wrapper_class = "ea-nav-active" if active else ""
                st.markdown(f'<div class="{wrapper_class}">', unsafe_allow_html=True)
                display_label = f"{label}  ·  {count}" if count else label
                if st.button(display_label, key=f"nav-{key}", width="stretch"):
                    go_to(key)
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="flex-grow:1;"></div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style="display:flex;align-items:center;gap:8px;margin-top:24px;padding:8px 4px;border-top:1px solid rgba(255,255,255,.08);">
                <div style="width:32px;height:32px;border-radius:999px;background:#6C5CE7;
                display:flex;align-items:center;justify-content:center;font-weight:600;color:#fff;font-size:13px;">{STUDENT['initials']}</div>
                <div class="ea-sidebar-footer-text">
                    <div style="font-size:13px;font-weight:600;color:#fff;">{STUDENT['name']}</div>
                    <div style="font-size:12px;color:#9CA3AF;">{STUDENT['track']} · {STUDENT['semester']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


_ALL_MOBILE_BOTTOM_ITEMS = [
    ("dashboard", "Home"),
    ("score", "Score"),
    ("skill_gap", "Gaps"),
    ("roadmap", "Learn"),
    ("profile", "More"),
]
MOBILE_BOTTOM_ITEMS = [item for item in _ALL_MOBILE_BOTTOM_ITEMS if item[0] in LIVE_SCREENS]


def render_mobile_bottom_nav(current_page: str):
    with st.container(key="mobile-bottom-nav"):
        cols = st.columns(len(MOBILE_BOTTOM_ITEMS))
        for col, (key, label) in zip(cols, MOBILE_BOTTOM_ITEMS):
            with col:
                marker = "●  " if key == current_page else ""
                if st.button(f"{marker}{label}", key=f"mnav-{key}", width="stretch"):
                    go_to(key)
                    st.rerun()
