import streamlit as st
from components.cards import icon_header
from components.icons import icon
from data.dummy_data import REPORT_CONTENTS, REPORT_HISTORY


def render():
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown('<div class="ea-heading">Reports</div>', unsafe_allow_html=True)
        st.markdown('<div class="ea-body" style="color:#6B7280;">Turn all of this into something you can send to a recruiter or your placement cell.</div>', unsafe_allow_html=True)
    with top_r:
        st.button("Generate new report", type="primary", width="stretch")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="ea-card">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:8px;">
                <div class="ea-header-row" style="margin-bottom:0;">
                    <div class="ea-icon-badge">{icon('reports', 'var(--color-primary)')}</div>
                    <div class="ea-section" style="font-size:18px;">The full report</div>
                </div>
                <span class="ea-badge ea-badge-purple" style="flex-shrink:0;">Recommended</span>
            </div>
            <div class="ea-small" style="margin-top:6px;">Your score, the skills you're missing, your plan and the roles you're closest to.</div>
            <div class="ea-card" style="margin-top:10px;background:#F8FAFC;">
                <b>Eight pages, ready to send</b><br/>
                <span class="ea-small">PDF · A4 · 1.2 MB</span><br/>
                <span class="ea-small">Last generated today, 4:14 PM</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Download PDF", type="primary", key="dl-full", width="stretch")
        b1, b2, b3 = st.columns(3)
        b1.button("Export", key="exp")
        b2.button("Share", key="shr")
        b3.button("Print", key="prt")

    with c2:
        st.markdown(f"""
        <div class="ea-card">
            <div class="ea-header-row">
                <div class="ea-icon-badge">{icon('trend', 'var(--color-primary)')}</div>
                <div class="ea-section" style="font-size:18px;">Progress summary</div>
            </div>
            <div class="ea-small" style="margin-top:6px;">Six months of progress on three pages. Handy for a mentor or a review meeting.</div>
            <div class="ea-small" style="margin-top:10px;">Format &nbsp; PDF · A4<br/>Period &nbsp; Feb - Jul 2026</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Download progress report", key="dl-progress", width="stretch")

    with c3:
        st.markdown(f"""
        <div class="ea-card">
            <div class="ea-header-row">
                <div class="ea-icon-badge">{icon('link', 'var(--color-primary)')}</div>
                <div class="ea-section" style="font-size:18px;">Send someone a link</div>
            </div>
            <div class="ea-small" style="margin-top:6px;">A page anyone can view but nobody can edit. You choose what's on it.</div>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("link", value="employa.ai/r/aarav-d-9f2c", label_visibility="collapsed")
        st.checkbox("Hide salary expectations", value=True)
        st.checkbox("Show assessment scores", value=False)
        st.button("Manage sharing", key="manage-sharing", width="stretch")

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    left, right = st.columns([1.6, 1])
    with left:
        icon_header("reports", "Reports you have made before")
        for r in REPORT_HISTORY:
            st.markdown(f"""
            <div class="ea-card" style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <div>
                    <b>{r['name']}</b><br/>
                    <span class="ea-small">{r['when']} · score {r['score']} · {r['size']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with right:
        icon_header("settings", "What goes in it")
        st.caption("Untick anything you'd rather keep to yourself")
        for item in REPORT_CONTENTS:
            st.checkbox(item["item"], value=item["included"], key=f"inc-{item['item']}")
        st.caption("Recruiters only see your score and skills. Your answers and batch position stay private unless you tick them on.")
