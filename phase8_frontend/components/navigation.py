import streamlit as st
from data.dummy_data import STUDENT
from utils.state import NAV_ITEMS, LIVE_SCREENS, go_to
from components.icons import icon


def render_sidebar(current_page: str):
    with st.sidebar:
        st.markdown(
            '<div style="display:flex;align-items:center;gap:8px;padding:8px 4px 16px 4px;">'
            '<div style="width:28px;height:28px;border-radius:8px;background:#0EA4AF;'
            'display:flex;align-items:center;justify-content:center;font-weight:700;color:#fff;">E</div>'
            '<span class="ea-sidebar-wordmark-text" style="font-weight:600;color:var(--color-text-primary);">EmployaAI</span>'
            '</div>',
            unsafe_allow_html=True,
        )

        # st.container(key=...) is the only reliable way to get a real
        # wrapping element around icon+button in Streamlit - raw <div> tags
        # opened/closed across separate st.markdown calls each land in
        # their own isolated container and never actually nest.
        st.markdown(
            f"<style>.st-key-nav-row-{current_page} {{ background: var(--color-accent-bg); "
            f"border-radius: 8px; border-left: 3px solid var(--color-primary); }} "
            f".st-key-nav-row-{current_page} .stButton > button "
            f"{{ color: var(--color-primary-dark) !important; font-weight: 600 !important; }}</style>",
            unsafe_allow_html=True,
        )

        for group_label, items in NAV_ITEMS:
            st.markdown(f'<div class="ea-nav-group-label">{group_label}</div>', unsafe_allow_html=True)
            for key, label, count in items:
                active = key == current_page
                icon_color = "#0EA4AF" if active else "#9CA3AF"
                with st.container(key=f"nav-row-{key}"):
                    icon_col, btn_col = st.columns([1, 6], gap="small")
                    with icon_col:
                        st.markdown(f'<div class="ea-nav-icon">{icon(key, icon_color)}</div>', unsafe_allow_html=True)
                    with btn_col:
                        display_label = f"{label}  ·  {count}" if count else label
                        if st.button(display_label, key=f"nav-{key}", width="stretch"):
                            go_to(key)
                            st.rerun()

        st.markdown('<div style="flex-grow:1;"></div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style="display:flex;align-items:center;gap:8px;margin-top:24px;padding:8px 4px;border-top:1px solid var(--color-border);">
                <div style="width:32px;height:32px;border-radius:999px;background:#0EA4AF;
                display:flex;align-items:center;justify-content:center;font-weight:600;color:#fff;font-size:13px;">{STUDENT['initials']}</div>
                <div class="ea-sidebar-footer-text">
                    <div style="font-size:13px;font-weight:600;color:var(--color-text-primary);">{STUDENT['name']}</div>
                    <div style="font-size:12px;color:var(--color-text-secondary);">{STUDENT['track']} · {STUDENT['semester']}</div>
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
                active = key == current_page
                color = "#0EA4AF" if active else "#9CA3AF"
                st.markdown(
                    f'<div style="text-align:center;color:{color};">{icon(key, color)}</div>',
                    unsafe_allow_html=True,
                )
                if st.button(label, key=f"mnav-{key}", width="stretch"):
                    go_to(key)
                    st.rerun()
