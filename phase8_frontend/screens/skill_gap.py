import streamlit as st
from components import charts
from components.badges import priority_badge_html
from components.cards import icon_header
from components.tables import responsive_table
from data.dummy_data import SKILL_GAP_ROWS, RADAR_ROLE


def render():
    st.markdown('<div class="ea-heading">Skill Gap Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="ea-body" style="color:#6B7280;">How you compare against 74 live job postings for Cloud Support Associate.</div>', unsafe_allow_html=True)
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    high = sum(1 for r in SKILL_GAP_ROWS if r["priority"] == "High")
    medium = sum(1 for r in SKILL_GAP_ROWS if r["priority"] == "Medium")
    met = sum(1 for r in SKILL_GAP_ROWS if r["priority"] == "Met")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="ea-card">
            <div class="ea-small">READY FOR</div>
            <div class="ea-section">Cloud Support Associate</div>
            <div class="ea-small">5 of 7 requirements met</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="ea-card" style="text-align:center;border-color:var(--color-primary);">
            <div class="ea-small">Must fix</div>
            <div class="ea-big-number" style="font-size:28px;color:var(--color-primary);">{high}</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="ea-card" style="text-align:center;">
            <div class="ea-small">Already met</div>
            <div class="ea-big-number" style="font-size:28px;color:var(--color-primary);">{met}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    left, right = st.columns([1, 1.3])
    with left:
        icon_header("skill_gap", "Your profile against the role")
        st.caption("The six things this role weighs most")
        with st.container(border=True):
            charts.radar(RADAR_ROLE["categories"], RADAR_ROLE["you"], RADAR_ROLE["role_requires"], "Role requires")
    with right:
        icon_header("trend", "What is needed against what you have")
        st.caption("Sorted by how much each gap is costing your score")
        with st.container(border=True):
            for row in sorted(SKILL_GAP_ROWS, key=lambda r: r["impact"]):
                pct = 100 if row["priority"] == "Met" else min(abs(row["impact"]) * 12, 100)
                st.markdown(f"""
                <div style="margin-bottom:12px;">
                    <div style="display:flex;justify-content:space-between;font-size:14px;">
                        <span>{row['skill']}</span>{priority_badge_html(row['priority'])}
                    </div>
                    <div class="ea-progress-track"><div class="ea-progress-fill" style="width:{pct}%;"></div></div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    icon_header("assessment", "Every gap, and what to do about it")
    st.caption("Based on job postings last refreshed on 28 July")

    headers = ["Skill", "Asked in", "Required", "You have", "Priority", "Suggested improvement"]
    rows = [
        [r["skill"], r["asked"], r["required"], r["have"], priority_badge_html(r["priority"]), r["action"]]
        for r in SKILL_GAP_ROWS
    ]

    def mobile_row(r_tuple):
        skill, asked, required, have, priority_html, action = r_tuple
        return f"""
        <div class="ea-card" style="margin-bottom:10px;">
            <div style="display:flex;justify-content:space-between;">
                <b>{skill}</b>{priority_html}
            </div>
            <div class="ea-small">Needed {required} · You have {have}</div>
            <div class="ea-body" style="margin-top:4px;">{action}</div>
        </div>
        """

    responsive_table(headers, rows, mobile_row)

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    st.markdown('<hr style="border:none;border-top:1px solid var(--color-border);margin:0 0 16px 0;">', unsafe_allow_html=True)
    st.markdown(
        '<div class="ea-small">Reviewed everything above? Turn it into a plan, '
        'or take a copy with you.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    b1, b2 = st.columns([1, 1])
    b1.button("Download plan", key="download-plan-bottom", width="stretch")
    b2.button("Build my roadmap →", type="primary", key="build-roadmap-bottom", width="stretch")
