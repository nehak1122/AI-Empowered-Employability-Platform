import streamlit as st
from components.cards import progress_bar_card, icon_header
from components.icons import icon
from data.dummy_data import ROADMAP_PHASES, ROADMAP_TIMELINE, THIS_WEEK, RECOMMENDATIONS


def render():
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown('<div class="ea-heading">Your 12-week roadmap</div>', unsafe_allow_html=True)
        st.markdown('<div class="ea-body" style="color:#6B7280;">Six hours a week, in the order that actually makes sense to learn things.</div>', unsafe_allow_html=True)
    with top_r:
        st.markdown('<div class="ea-small" style="text-align:right;">Projected score</div>', unsafe_allow_html=True)
        st.markdown('<div class="ea-section" style="text-align:right;color:#0EA4AF;">74 → 88</div>', unsafe_allow_html=True)
        st.button("Download plan", type="primary", width="stretch")

    progress_bar_card("Overall progress", 22, right_label="Week 3 of 12 · 22% done")

    cols = st.columns(3)
    for i, (col, phase) in enumerate(zip(cols, ROADMAP_PHASES), start=1):
        with col:
            border = "border-color:var(--color-primary);" if phase["status"] == "In progress" else ""
            if phase["status"] == "In progress":
                dot_class, dot_content = "current", str(i)
            elif phase["progress"] >= 100:
                dot_class, dot_content = "done", "✓"
            else:
                dot_class, dot_content = "pending", str(i)
            st.markdown(f"""
            <div class="ea-card" style="{border}">
                <div style="display:flex;justify-content:space-between;align-items:center;">
                    <div style="display:flex;align-items:center;gap:8px;">
                        <div class="ea-step-dot {dot_class}">{dot_content}</div>
                        <div class="ea-small">{phase['weeks']}</div>
                    </div>
                    <span class="ea-badge {'ea-badge-purple' if phase['status']=='In progress' else 'ea-badge-neutral'}">{phase['status']}</span>
                </div>
                <div class="ea-section" style="margin-top:8px;">{phase['title']}</div>
                <div class="ea-body" style="color:#6B7280;margin-top:4px;font-size:14px;">{phase['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
            progress_bar_card("", phase["progress"], right_label=f"{phase['progress']}%")

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    icon_header("roadmap", "Your twelve weeks")
    st.caption("Nothing starts before the skill it builds on is done")
    with st.container(border=True):
        total_weeks = 12
        for track in ROADMAP_TIMELINE:
            color = {"done": "var(--color-primary-dark)", "now": "var(--color-primary)", "upcoming": "#E5E7EB"}[track["status"]]
            left_pct = (track["start_week"] - 1) / total_weeks * 100
            width_pct = (track["end_week"] - track["start_week"]) / total_weeks * 100
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
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
        icon_header("assessment", "What you are on this week")
        with st.container(border=True):
            for item in THIS_WEEK:
                if item["status"] == "done":
                    st.markdown(
                        f'<div style="margin-bottom:10px;display:flex;gap:8px;align-items:center;">'
                        f'<span style="color:var(--color-primary);">{icon("check-circle")}</span>{item["title"]}</div>',
                        unsafe_allow_html=True,
                    )
                elif item["status"] == "active":
                    st.markdown(f"""
                    <div class="ea-card" style="border-color:var(--color-primary);margin-bottom:10px;">
                        <b>{item['title']}</b><br/><span class="ea-small">{item['meta']}</span>
                    </div>
                    """, unsafe_allow_html=True)
                    st.button("Resume lesson", type="primary", key="resume_lesson")
                else:
                    st.markdown(f'<div style="margin-bottom:10px;color:#9CA3AF;">{item["title"]}</div>', unsafe_allow_html=True)

    with right:
        icon_header("book", "Courses that would help")
        with st.container(border=True):
            for c in RECOMMENDATIONS:
                st.markdown(f"""
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
                    <div><b>{c['title']}</b><br/><span class="ea-small">{c['meta']}</span></div>
                    <span class="ea-badge ea-badge-purple">{c['tag']}</span>
                </div>
                """, unsafe_allow_html=True)
