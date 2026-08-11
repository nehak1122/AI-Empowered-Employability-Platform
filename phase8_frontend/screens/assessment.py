import streamlit as st
from components.badges import badge
from data.dummy_data import ASSESSMENT_SECTIONS

QUESTION = {
    "domain_tags": ["Identity & access", "Medium", "Single choice"],
    "text": "A team needs an application running on EC2 to read objects from a single "
            "S3 bucket, with no long-lived credentials stored on the instance. What is the correct approach?",
    "options": [
        ("A", "Store an access key and secret in an environment variable on the instance"),
        ("B", "Attach an IAM role to the instance with a policy scoped to that bucket"),
        ("C", "Make the bucket public and restrict access by IP address"),
        ("D", "Create an IAM user per instance and rotate the keys weekly"),
    ],
}


def render():
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown('<div class="ea-heading">Cloud Computing — Technical</div>', unsafe_allow_html=True)
        st.markdown('<div class="ea-body" style="color:#6B7280;">Section 3 of 4 — your answers save as you go.</div>', unsafe_allow_html=True)
    with top_r:
        st.button("Submit section", type="primary", width="stretch")

    main, sidebar = st.columns([2.4, 1])

    with main:
        st.progress(0.40, text="Question 12 of 30 · 40% complete")
        with st.container(border=True):
            st.markdown(" ".join(f'<span class="ea-badge ea-badge-neutral">{t}</span>' for t in QUESTION["domain_tags"]), unsafe_allow_html=True)
            st.markdown(f'<div class="ea-body" style="margin-top:10px;font-weight:600;">{QUESTION["text"]}</div>', unsafe_allow_html=True)
            choice = st.radio(
                "options", [f"{k} · {v}" for k, v in QUESTION["options"]],
                index=1, label_visibility="collapsed",
            )
            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
            st.radio("How sure are you?", ["Guessing", "Fairly sure", "Certain"], index=1, horizontal=True)

            st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
            nav1, nav2, nav3 = st.columns([1, 1, 1])
            nav1.button("← Previous", width="stretch")
            nav2.markdown('<div style="text-align:center;color:#22C55E;padding-top:8px;">Saved</div>', unsafe_allow_html=True)
            nav3.button("Next question →", type="primary", width="stretch")

    with sidebar:
        st.markdown('<div class="ea-section">Your sections</div>', unsafe_allow_html=True)
        with st.container(border=True):
            for s in ASSESSMENT_SECTIONS:
                c1, c2 = st.columns([2, 1])
                c1.markdown(s["name"])
                with c2:
                    kind = "success" if s["status"] == "Done" else ("purple" if s["status"] == "In progress" else "neutral")
                    badge(s["score"], kind)

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        st.markdown('<div class="ea-section">Domain</div>', unsafe_allow_html=True)
        with st.container(border=True):
            st.radio("domain", ["Cloud Computing", "Cybersecurity"], index=0, label_visibility="collapsed")
            st.caption("Switching domain restarts this section.")
