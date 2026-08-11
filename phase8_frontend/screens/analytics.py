import streamlit as st
from components import charts
from data.dummy_data import (
    ANALYTICS_SUMMARY, SECTION_PERFORMANCE, HOURS_LOGGED,
    SKILL_PRACTICE_HEATMAP, ATTEMPT_HISTORY,
)


def render():
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown('<div class="ea-heading">Analytics</div>', unsafe_allow_html=True)
        st.markdown('<div class="ea-body" style="color:#6B7280;">How far you have come since February, and how that compares with the rest of your batch.</div>', unsafe_allow_html=True)
    with top_r:
        st.selectbox("range", ["Last 6 months", "Last 3 months", "Last year"], label_visibility="collapsed")

    cols = st.columns(4)
    for col, s in zip(cols, ANALYTICS_SUMMARY):
        with col:
            delta_html = f'<span class="ea-badge ea-badge-success">{s["delta"]}</span>' if s["delta"] else ""
            st.markdown(f"""
            <div class="ea-card">
                <div class="ea-small">{s['label']}</div>
                <div class="ea-big-number" style="font-size:28px;">{s['value']}</div>
                {delta_html}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    left, right = st.columns(2)
    with left:
        st.markdown('<div class="ea-section">How your score has moved</div>', unsafe_allow_html=True)
        st.caption("You, the batch average, and the line you need to cross")
        from data.dummy_data import SCORE_HISTORY
        charts.line(SCORE_HISTORY["months"], SCORE_HISTORY["student"], SCORE_HISTORY["cohort"], SCORE_HISTORY["target"])
    with right:
        st.markdown('<div class="ea-section">How you did in each section</div>', unsafe_allow_html=True)
        st.caption("Your most recent attempt at each one")
        charts.bar([s["section"] for s in SECTION_PERFORMANCE], [s["score"] for s in SECTION_PERFORMANCE], warn_below=55)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.4, 1])
    with c1:
        st.markdown('<div class="ea-section">Hours you have put in</div>', unsafe_allow_html=True)
        st.caption("Against your target of six hours a week")
        for h in HOURS_LOGGED:
            pct = min(round(h["hours"] / h["target"] * 100), 100)
            tone = "success" if h["met"] else "warning"
            from components.cards import progress_bar_card
            progress_bar_card(h["month"], pct, right_label=f'{h["hours"]} hrs', tone=tone)
        st.warning("July was six hours short. Two extra sessions this week and you're back on track.")

    with c2:
        st.markdown('<div class="ea-section">Which skills you have practised</div>', unsafe_allow_html=True)
        st.caption("Darker means more practice that month")
        charts.heatmap(SKILL_PRACTICE_HEATMAP["skills"], SKILL_PRACTICE_HEATMAP["months"], SKILL_PRACTICE_HEATMAP["matrix"])

    with c3:
        st.markdown('<div class="ea-section">Everything you have taken</div>', unsafe_allow_html=True)
        for a in ATTEMPT_HISTORY:
            kind = "success" if a["kind"] == "success" else "warning"
            st.markdown(f"""
            <div class="ea-card" style="padding:10px 12px;margin-bottom:6px;display:flex;justify-content:space-between;align-items:center;">
                <div><b style="font-size:13px;">{a['name']}</b><br/><span class="ea-small">{a['when']}</span></div>
                <span class="ea-badge {'ea-badge-success' if kind=='success' else 'ea-badge-warning'}">{a['score']}</span>
            </div>
            """, unsafe_allow_html=True)
