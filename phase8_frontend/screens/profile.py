import streamlit as st
from components.badges import badge
from components.cards import section_header
from data.dummy_data import (
    STUDENT, PROFILE_STEPS, EDUCATION, SKILLS, CERTIFICATIONS_HELD, PROJECTS, RESUME,
)


def render():
    st.markdown('<div class="ea-heading">Student Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="ea-body" style="color:#6B7280;">All of this feeds into your score. Three sections still need a bit of attention.</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    hc1, hc2 = st.columns([3, 1])
    with hc1:
        st.markdown(f"""
        <div class="ea-card" style="display:flex;gap:16px;align-items:center;">
            <div style="width:56px;height:56px;border-radius:999px;background:#0EA4AF;color:#fff;
            display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18px;">{STUDENT['initials']}</div>
            <div>
                <div class="ea-section">{STUDENT['name']}</div>
                <div class="ea-small">{STUDENT['degree']} · {STUDENT['semester']} · CGPA {STUDENT['cgpa']} · {STUDENT['enrolment_id']}</div>
                <div class="ea-small">{STUDENT['github']} &nbsp;·&nbsp; {STUDENT['linkedin']} &nbsp;·&nbsp; {STUDENT['languages']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with hc2:
        st.markdown(f"""
        <div class="ea-card" style="text-align:center;">
            <div class="ea-small">Profile completion</div>
            <div class="ea-big-number" style="font-size:28px;">{STUDENT['profile_completion']}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    step_html = ""
    for i, step in enumerate(PROFILE_STEPS, start=1):
        if step["status"] == "done":
            marker = f'<div style="width:22px;height:22px;border-radius:999px;background:#22C55E;color:#fff;font-size:12px;display:flex;align-items:center;justify-content:center;">✓</div>'
        elif step["status"] == "current":
            marker = f'<div style="width:22px;height:22px;border-radius:999px;background:#0EA4AF;color:#fff;font-size:12px;display:flex;align-items:center;justify-content:center;">{i}</div>'
        else:
            marker = f'<div style="width:22px;height:22px;border-radius:999px;background:#E5E7EB;color:#6B7280;font-size:12px;display:flex;align-items:center;justify-content:center;">{i}</div>'
        label_color = "#111827" if step["status"] != "pending" else "#9CA3AF"
        step_html += f'<div style="display:flex;flex-direction:column;align-items:center;gap:4px;min-width:90px;">{marker}<span style="font-size:12px;color:{label_color};text-align:center;">{step["label"]}</span></div>'
        if i < len(PROFILE_STEPS):
            step_html += '<div style="flex:1;height:2px;background:#E5E7EB;margin-top:11px;"></div>'
    st.markdown(f'<div class="ea-card" style="display:flex;align-items:flex-start;gap:4px;">{step_html}</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="ea-section">Personal information</div>', unsafe_allow_html=True)
        with st.container(border=True):
            f1, f2 = st.columns(2)
            f1.text_input("Full name", value=STUDENT["name"])
            f2.text_input("Enrolment ID", value=STUDENT["enrolment_id"])
            f3, f4 = st.columns(2)
            f3.text_input("Email", value=STUDENT["email"])
            f4.text_input("Phone", value=STUDENT["phone"])

        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        st.markdown('<div class="ea-section">Education</div>', unsafe_allow_html=True)
        with st.container(border=True):
            for edu in EDUCATION:
                e1, e2 = st.columns([3, 1])
                e1.markdown(f'<b>{edu["level"]}</b><br/><span class="ea-small">{edu["meta"]}</span>', unsafe_allow_html=True)
                e2.markdown(f'<div style="text-align:right;padding-top:6px;font-weight:600;">{edu["score"]}</div>', unsafe_allow_html=True)

        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        st.markdown('<div class="ea-section">Projects <span style="font-weight:400;">(1 of 3)</span></div>', unsafe_allow_html=True)
        with st.container(border=True):
            for p in PROJECTS:
                st.markdown(f'<b>{p["title"]}</b> <span class="ea-small">· {p["meta"]}</span>', unsafe_allow_html=True)
                st.markdown(f'<div class="ea-body">{p["desc"]}</div>', unsafe_allow_html=True)
                st.markdown(" ".join(f'<span class="ea-badge ea-badge-neutral">{t}</span>' for t in p["tags"]), unsafe_allow_html=True)
            st.button("+ Add a project", width="stretch")

    with c2:
        st.markdown('<div class="ea-section">Skills</div>', unsafe_allow_html=True)
        with st.container(border=True):
            tag_html = ""
            for s in SKILLS:
                kind = "ea-badge-error" if s.get("warning") else "ea-badge-purple"
                tag_html += f'<span class="ea-badge {kind}" style="margin:3px;">{s["name"]} {s["level"]}</span> '
            st.markdown(tag_html, unsafe_allow_html=True)
            st.button("+ Add skill", key="add_skill")

        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        st.markdown('<div class="ea-section">Certifications <span style="font-weight:400;">(2 held)</span></div>', unsafe_allow_html=True)
        with st.container(border=True):
            for c in CERTIFICATIONS_HELD:
                cc1, cc2 = st.columns([3, 1])
                cc1.markdown(f'<b>{c["badge"]}</b> &nbsp; {c["name"]}<br/><span class="ea-small">{c["meta"]}</span>', unsafe_allow_html=True)
                with cc2:
                    badge(c["status"], "success")

        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        st.markdown('<div class="ea-section">Resume</div>', unsafe_allow_html=True)
        with st.container(border=True):
            rc1, rc2 = st.columns([3, 1])
            rc1.markdown(f'📄 <b>{RESUME["filename"]}</b><br/><span class="ea-small">{RESUME["meta"]}</span>', unsafe_allow_html=True)
            with rc2:
                badge(f"Score {RESUME['score']}", "warning")

        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        st.markdown('<div class="ea-section">Internships</div>', unsafe_allow_html=True)
        with st.container(border=True):
            badge("Empty", "error")
            st.caption("Even a two-week stint counts. 41 of the 74 postings we track ask for one.")
            st.button("Add internship", type="primary", width="stretch")

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    st.markdown('<hr style="border:none;border-top:1px solid var(--color-border);margin:0 0 16px 0;">', unsafe_allow_html=True)
    save_l, save_r = st.columns([3, 1])
    with save_l:
        st.caption("Changes save to your profile and feed straight into your employability score.")
    with save_r:
        st.button("Save changes", type="primary", key="save-changes-bottom", width="stretch")
