import streamlit as st
from components.cards import progress_bar_card, icon_header, message_banner
from components.badges import badge
from data.dummy_data import CAREER_MATCHES, FIT_BREAKDOWN, ROLE_REQUIREMENTS


def render():
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown('<div class="ea-heading">Where you can apply</div>', unsafe_allow_html=True)
        st.markdown('<div class="ea-body" style="color:#6B7280;">Nine Cloud roles looked at. These three are realistic for you right now.</div>', unsafe_allow_html=True)
    with top_r:
        st.button("Compare roles", width="stretch")

    cols = st.columns(3)
    for col, role in zip(cols, CAREER_MATCHES):
        with col:
            hero = role["status"] == "Ready now"
            status_kind = {"Ready now": "success", "2 gaps away": "warning", "Stretch": "neutral"}[role["status"]]
            border = "border-color:#0EA4AF;" if hero else ""
            skills_html = " ".join(f'<span class="ea-badge ea-badge-success">{s} ✓</span>' for s in role["skills_ok"])
            skills_html += " " + " ".join(f'<span class="ea-badge ea-badge-error">{s}</span>' for s in role["skills_gap"])
            st.markdown(f"""
            <div class="ea-card" style="{border}">
                <span class="ea-badge {'ea-badge-success' if status_kind=='success' else ('ea-badge-warning' if status_kind=='warning' else 'ea-badge-neutral')}">{role['status']}</span>
                <div style="display:flex;justify-content:space-between;align-items:center;gap:10px;margin-top:6px;">
                    <div class="ea-section" style="min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">{role['role']}</div>
                    <div class="ea-big-number" style="font-size:24px;color:#0EA4AF;flex-shrink:0;">{role['match']}%</div>
                </div>
                <div style="margin-top:6px;">{skills_html}</div>
                <div class="ea-small" style="margin-top:8px;">Expected salary <b>{role['salary']}</b></div>
                <div class="ea-small">Hiring for it: {role['hiring']} · {role['openings']} openings</div>
            </div>
            """, unsafe_allow_html=True)
            st.button("Apply" if hero else "See what's missing", type="primary" if hero else "secondary", key=f"role-{role['role']}", width="stretch")

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    left, right = st.columns(2)
    with left:
        icon_header("skill_gap", "Fit breakdown")
        st.caption("Cloud Support Associate - your best match")
        with st.container(border=True):
            for f in FIT_BREAKDOWN:
                progress_bar_card(f["label"], f["value"])
            message_banner("Good news", "Your skills already clear the bar here. It's only the certification column holding the number down.", kind="success")

    with right:
        icon_header("assessment", "What this role asks for")
        st.caption("Taken from 74 live postings for this job title")
        with st.container(border=True):
            for req in ROLE_REQUIREMENTS:
                kind = {"Met": "success", "Partial": "warning", "Gap": "error"}[req["status"]]
                c1, c2 = st.columns([3, 1])
                c1.markdown(f'{req["item"]}<br/><span class="ea-small">Asked for in {req["asked"]}</span>', unsafe_allow_html=True)
                with c2:
                    badge(req["status"], kind)
