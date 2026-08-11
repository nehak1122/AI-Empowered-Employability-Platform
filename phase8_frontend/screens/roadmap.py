import streamlit as st
from components.cards import progress_bar_card
from data.dummy_data import ROADMAP_PHASES, ROADMAP_TIMELINE, THIS_WEEK, RECOMMENDATIONS


def render():
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown('<div class="ea-heading">Your 12-week roadmap</div>', unsafe_allow_html=True)
        st.markdown('<div class="ea-body" style="color:#6B7280;">Six hours a week, in the order that actually makes sense to learn things.</div>', unsafe_allow_html=True)
    with top_r:
        st.markdown('<div class="ea-small" style="text-align:right;">Projected score</div>', unsafe_allow_html=True)
        st.markdown('<div class="ea-section" style="text-align:right;color:#6C5CE7;">74 → 88</div>', unsafe_allow_html=True)
        st.button("Download plan", type="primary", width="stretch")

    progress_bar_card("Overall progress", 22, right_label="Week 3 of 12 · 22% done")

    cols = st.columns(3)
    for col, phase in zip(cols, ROADMAP_PHASES):
        with col:
            border = "border-color:#6C5CE7;" if phase["status"] == "In progress" else ""
            st.markdown(f"""
            <div class="ea-card" style="{border}">
                <div style="display:flex;justify-content:space-between;">
                    <div class="ea-small">{phase['weeks']}</div>
                    <span class="ea-badge {'ea-badge-purple' if phase['status']=='In progress' else 'ea-badge-neutral'}">{phase['status']}</span>
                </div>
                <div class="ea-section" style="margin-top:4px;">{phase['title']}</div>
                <div class="ea-body" style="color:#6B7280;margin-top:4px;font-size:14px;">{phase['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
            progress_bar_card("", phase["progress"], right_label=f"{phase['progress']}%")

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    st.markdown('<div class="ea-section">Your twelve weeks</div>', unsafe_allow_html=True)
    st.caption("Nothing starts before the skill it builds on is done")
    total_weeks = 12
    for track in ROADMAP_TIMELINE:
        color = {"done": "#22C55E", "now": "#6C5CE7", "upcoming": "#E5E7EB"}[track["status"]]
        left_pct = (track["start_week"] - 1) / total_weeks * 100
        width_pct = (track["end_week"] - track["start_week"]) / total_weeks * 100
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
            <div style="width:140px;font-size:13px;">{track['track']}</div>
            <div style="flex:1;background:#F3F4F6;border-radius:6px;height:14px;position:relative;">
                <div style="position:absolute;left:{left_pct}%;width:{width_pct}%;background:{color};height:100%;border-radius:6px;"></div>
            </div>
            <div style="width:70px;font-size:12px;color:#6B7280;">W{track['start_week']}-{track['end_week']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    left, right = st.columns(2)
    with left:
        st.markdown('<div class="ea-section">What you are on this week</div>', unsafe_allow_html=True)
        for item in THIS_WEEK:
            if item["status"] == "done":
                st.markdown(f'<div class="ea-card" style="margin-bottom:8px;">✅ {item["title"]}</div>', unsafe_allow_html=True)
            elif item["status"] == "active":
                st.markdown(f"""
                <div class="ea-card" style="border-color:#6C5CE7;margin-bottom:8px;">
                    <b>{item['title']}</b><br/><span class="ea-small">{item['meta']}</span>
                </div>
                """, unsafe_allow_html=True)
                st.button("Resume lesson", type="primary", key="resume_lesson")
            else:
                st.markdown(f'<div class="ea-card" style="margin-bottom:8px;color:#9CA3AF;">{item["title"]}</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="ea-section">Courses that would help</div>', unsafe_allow_html=True)
        for c in RECOMMENDATIONS:
            st.markdown(f"""
            <div class="ea-card" style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <div><b>{c['title']}</b><br/><span class="ea-small">{c['meta']}</span></div>
                <span class="ea-badge ea-badge-purple">{c['tag']}</span>
            </div>
            """, unsafe_allow_html=True)
