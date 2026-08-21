import streamlit as st
from components import charts
from components.cards import score_hero_card, progress_bar_card, icon_header
from components.icons import icon
from data.dummy_data import (
    STUDENT, SCORE, SCORE_HISTORY, SKILLS_OVERVIEW, QUICK_ACTIONS,
    RECENT_ACTIVITY, JOB_MATCHES,
)


def render():
    st.markdown(f'<div class="ea-heading">Good evening, {STUDENT["name"].split()[0]} 👋</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="ea-body" style="color:#6B7280;margin-top:4px;">'
        f'Great progress — your score went up {SCORE["points_this_week"]} points this week. '
        f'You are only 2 skills away from being ready for a Cloud Support Associate role.</div>',
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
    st.text_input("Search", placeholder="Search skills, roles, courses…", label_visibility="collapsed")

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    qa_cols = st.columns(len(QUICK_ACTIONS))
    for col, action in zip(qa_cols, QUICK_ACTIONS):
        with col:
            st.markdown(f"""
            <div class="ea-card" style="text-align:left;">
                <div class="ea-icon-badge" style="margin-bottom:8px;">{action['icon']}</div>
                <div class="ea-body" style="font-weight:600;">{action['label']}</div>
                <div class="ea-small">{action['hint']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1.1, 1, 1])
    with c1:
        score_hero_card(SCORE["overall"], SCORE["band"], f"+{SCORE['overall'] - SCORE['cohort_average']:.1f} above", SCORE["job_ready_threshold"] - SCORE["overall"])
    with c2:
        st.markdown(f"""
        <div class="ea-card">
            <div class="ea-card-kicker">Your profile</div>
            <div class="ea-big-number">{STUDENT['profile_completion']}%</div>
            <div class="ea-small">Resume uploaded · Done<br/>GitHub linked · Done<br/>Projects · 1 of 3<br/>Internship · Empty</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="ea-card" style="border-color:var(--color-primary);background:var(--color-accent-bg);">
            <div class="ea-card-kicker">⚡ Today's goal</div>
            <div class="ea-body" style="font-weight:600;">Start the Terraform module</div>
            <div class="ea-small">Worth around 7 points, ~3 weeks of work.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    left, right = st.columns([1.4, 1])
    with left:
        icon_header("analytics", "Score over time")
        st.caption("Every score you've had since February")
        with st.container(border=True):
            charts.line(SCORE_HISTORY["months"], SCORE_HISTORY["student"], SCORE_HISTORY["cohort"], SCORE_HISTORY["target"])
    with right:
        icon_header("skill_gap", "Skill overview")
        with st.container(border=True):
            for s in SKILLS_OVERVIEW:
                progress_bar_card(s["skill"], round(s["score"] / s["max"] * 100), right_label=s["level"])

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        icon_header("careers", "Job match")
        with st.container(border=True):
            for j in JOB_MATCHES:
                progress_bar_card(j["role"], j["match"])
    with c2:
        icon_header("bell", "Recent activity")
        with st.container(border=True):
            for a in RECENT_ACTIVITY:
                st.markdown(f'<div class="ea-body" style="margin-bottom:8px;">• {a["text"]}<br/><span class="ea-small">{a["when"]}</span></div>', unsafe_allow_html=True)

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    with st.container(key="dashboard-cta"):
        text_col, btn_col = st.columns([3, 1], vertical_alignment="center")
        with text_col:
            st.markdown(
                '<div class="ea-section" style="color:#fff;">Continue your assessment</div>'
                '<div class="ea-small">Technical section - 12 of 30 done. About 15 minutes left.</div>',
                unsafe_allow_html=True,
            )
        with btn_col:
            st.button("Continue assessment →", type="primary", key="continue-assessment-bottom", width="stretch")
