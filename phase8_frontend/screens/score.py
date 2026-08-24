import streamlit as st
from components import charts
from components.cards import score_hero_card, icon_header
from data.dummy_data import SCORE, SCORE_BREAKDOWN, SCORE_DRIVERS


def render():
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown('<div class="ea-heading">Employability Score</div>', unsafe_allow_html=True)
        st.markdown('<div class="ea-body" style="color:#6B7280;">Updated today at 4:12 PM — here is exactly how we got to it.</div>', unsafe_allow_html=True)
    with top_r:
        st.button("Recalculate", width="stretch")

    left, right = st.columns([1, 1.6])
    with left:
        score_hero_card(SCORE["overall"], f"{SCORE['band']} · Near-ready", f"+{SCORE['overall']-SCORE['cohort_average']:.1f}", SCORE["job_ready_threshold"] - SCORE["overall"])
        st.markdown(f"""
        <div class="ea-card" style="margin-top:16px;">
            <div style="display:flex;justify-content:space-between;align-items:center;font-size:14px;margin-bottom:6px;"><span>Cohort average</span><b>{SCORE['cohort_average']}</b></div>
            <div style="display:flex;justify-content:space-between;align-items:center;font-size:14px;margin-bottom:6px;"><span>Job-ready threshold</span><b>{SCORE['job_ready_threshold']}</b></div>
            <div style="display:flex;justify-content:space-between;align-items:center;font-size:14px;"><span>Your percentile</span><b>{SCORE['percentile']}th of {SCORE['cohort_size']}</b></div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        icon_header("analytics", "What makes up your score")
        st.caption("The bar is you, the line marks the batch average")
        with st.container(border=True):
            charts.bar([s["label"] for s in SCORE_BREAKDOWN], [s["value"] for s in SCORE_BREAKDOWN], warn_below=55)

        st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
        icon_header("trend", "Why you got this score")
        st.caption("What pushed it up and what pulled it down, starting from a baseline of 55")
        with st.container(border=True):
            for d in SCORE_DRIVERS:
                color = "var(--color-primary)" if d["impact"] > 0 else "#94A3B8"
                sign = "+" if d["impact"] > 0 else ""
                width = min(abs(d["impact"]) * 8, 100)
                st.markdown(f"""
                <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
                    <div style="width:150px;font-size:13px;">{d['label']}</div>
                    <div style="flex:1;background:#F3F4F6;border-radius:6px;height:10px;">
                        <div style="width:{width}%;background:{color};height:100%;border-radius:6px;"></div>
                    </div>
                    <div style="width:44px;text-align:right;font-size:13px;font-weight:600;color:{color};">{sign}{d['impact']}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    for col, (label, value, hint) in zip(
        [m1, m2, m3, m4],
        [
            ("Readiness verdict", "Near-ready", "One certification away from the top band"),
            ("Gaps open", "7 · 2 high", "Down from 9 last month"),
            ("Roles you qualify for", "3 of 9", "In the Cloud track"),
            ("Projected after roadmap", "88 (+14)", "If the 12-week plan is completed"),
        ],
    ):
        with col:
            st.markdown(f"""
            <div class="ea-card">
                <div class="ea-small">{label}</div>
                <div class="ea-section" style="margin-top:4px;">{value}</div>
                <div class="ea-small" style="margin-top:4px;">{hint}</div>
            </div>
            """, unsafe_allow_html=True)
