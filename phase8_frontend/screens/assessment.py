import streamlit as st
from components.badges import badge
from components.cards import progress_bar_card
from components import charts
from data.dummy_data import ASSESSMENT_SECTIONS, ASSESSMENT_DOMAINS, ASSESSMENT_RESULT

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
    if st.session_state.get("assessment_submitted"):
        _render_results()
    elif not st.session_state.get("assessment_domain"):
        _render_domain_picker()
    else:
        _render_question_flow()


def _step_tracker():
    """Numbered stepper across the top - which section is done, current, or locked."""
    step_html = ""
    total = len(ASSESSMENT_SECTIONS)
    for i, s in enumerate(ASSESSMENT_SECTIONS, start=1):
        if s["status"] == "Done":
            marker = f'<div class="ea-step-dot done">✓</div>'
        elif s["status"] == "In progress":
            marker = f'<div class="ea-step-dot current">{i}</div>'
        else:
            marker = f'<div class="ea-step-dot pending">{i}</div>'
        label_color = "var(--color-text-primary)" if s["status"] != "Locked" else "#9CA3AF"
        step_html += (
            f'<div style="display:flex;flex-direction:column;align-items:center;gap:4px;min-width:110px;">'
            f'{marker}<span style="font-size:12px;color:{label_color};text-align:center;font-weight:600;">{s["name"]}</span>'
            f'<span style="font-size:11px;color:#9CA3AF;">{s["score"]}</span></div>'
        )
        if i < total:
            line_color = "var(--color-success)" if s["status"] == "Done" else "var(--color-border)"
            step_html += f'<div style="flex:1;height:2px;background:{line_color};margin-top:15px;"></div>'
    st.markdown(f'<div class="ea-card" style="display:flex;align-items:flex-start;gap:4px;">{step_html}</div>', unsafe_allow_html=True)


def _render_domain_picker():
    st.markdown('<div class="ea-heading">Choose your domain</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="ea-body" style="color:#6B7280;">Pick the track you want to be assessed on. '
        'This decides which questions you get for the rest of the assessment - you can switch later, '
        'but that restarts the section you are on.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    cols = st.columns(len(ASSESSMENT_DOMAINS))
    for col, d in zip(cols, ASSESSMENT_DOMAINS):
        with col:
            st.markdown(f"""
            <div class="ea-card" style="min-height:140px;">
                <div class="ea-section">{d['name']}</div>
                <div class="ea-body" style="color:#6B7280;margin-top:6px;font-size:14px;">{d['desc']}</div>
                <div class="ea-small" style="margin-top:10px;">{d['questions']} questions · ~{d['minutes']} min</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Start {d['name']} →", type="primary", key=f"start-{d['key']}", width="stretch"):
                st.session_state.assessment_domain = d["key"]
                st.rerun()


def _render_question_flow():
    domain_name = next(d["name"] for d in ASSESSMENT_DOMAINS if d["key"] == st.session_state.assessment_domain)
    st.markdown(f"""
    <div class="ea-card" style="background:var(--color-secondary);border:none;">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
            <div>
                <div class="ea-section" style="color:var(--color-text-primary);">{domain_name} — Technical assessment</div>
                <div class="ea-body" style="color:var(--color-text-primary);margin-top:4px;">
                    30 questions, single choice. Answer each one and move on — your progress saves automatically,
                    so you can leave and pick up right where you left off.
                </div>
            </div>
            <span class="ea-badge ea-badge-neutral">Section 3 of 4</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    _step_tracker()
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    main, sidebar = st.columns([2.4, 1])

    with main:
        st.progress(0.40, text="Question 12 of 30 · 40% complete")
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(" ".join(f'<span class="ea-badge ea-badge-neutral">{t}</span>' for t in QUESTION["domain_tags"]), unsafe_allow_html=True)
            st.markdown(f'<div class="ea-body" style="margin-top:10px;font-weight:600;">{QUESTION["text"]}</div>', unsafe_allow_html=True)
            st.radio(
                "options", [f"{k} · {v}" for k, v in QUESTION["options"]],
                index=1, label_visibility="collapsed",
            )
            st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
            st.radio("How sure are you?", ["Guessing", "Fairly sure", "Certain"], index=1, horizontal=True)

            st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
            nav1, nav2, nav3 = st.columns([1, 1, 1])
            nav1.button("← Previous", width="stretch")
            nav2.markdown('<div style="text-align:center;color:#22C55E;padding-top:8px;">Saved</div>', unsafe_allow_html=True)
            nav3.button("Next question →", type="primary", width="stretch")

        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        st.markdown(
            '<div class="ea-small">This is a preview build, so the button below is left enabled — in the '
            'real assessment it stays locked until all 30 questions in this section are answered.</div>',
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("Submit section →", type="primary", width="stretch", key="submit-section-bottom"):
            st.session_state.assessment_submitted = True
            st.rerun()

    with sidebar:
        st.markdown('<div class="ea-section">Your sections</div>', unsafe_allow_html=True)
        with st.container(border=True):
            for s in ASSESSMENT_SECTIONS:
                c1, c2 = st.columns([2, 1])
                c1.markdown(s["name"])
                with c2:
                    kind = "success" if s["status"] == "Done" else ("purple" if s["status"] == "In progress" else "neutral")
                    badge(s["score"], kind)

        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        st.markdown('<div class="ea-section">Domain</div>', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(f'<b>{domain_name}</b>', unsafe_allow_html=True)
            st.caption("Switching domain restarts this section.")
            if st.button("Switch domain", key="switch-domain", width="stretch"):
                st.session_state.assessment_domain = None
                st.rerun()


def _render_results():
    st.markdown('<div class="ea-heading">Section results</div>', unsafe_allow_html=True)
    st.markdown('<div class="ea-body" style="color:#6B7280;">Here is how the Communication section went, and what it means for your score.</div>', unsafe_allow_html=True)
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    left, right = st.columns([1, 1.6])
    with left:
        st.markdown(f"""
        <div class="ea-card-hero">
            <div class="ea-small">Overall in this section</div>
            <div class="ea-big-number" style="font-size:56px;margin-top:8px;">{ASSESSMENT_RESULT['overall']}</div>
            <div class="ea-small">out of 100</div>
            <div style="margin-top:10px;"><span class="ea-badge ea-badge-neutral">{ASSESSMENT_RESULT['band']}</span></div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="ea-section">How each section scored</div>', unsafe_allow_html=True)
        charts.bar([s["name"] for s in ASSESSMENT_RESULT["sections"]], [s["score"] for s in ASSESSMENT_RESULT["sections"]], warn_below=60)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="ea-section">Strengths</div>', unsafe_allow_html=True)
        with st.container(border=True):
            for s in ASSESSMENT_RESULT["strengths"]:
                st.markdown(f'<div class="ea-body" style="margin-bottom:8px;">✅ {s}</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="ea-section">Where you lost points</div>', unsafe_allow_html=True)
        with st.container(border=True):
            for w in ASSESSMENT_RESULT["weaknesses"]:
                st.markdown(f'<div class="ea-body" style="margin-bottom:8px;">⚠️ {w}</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="ea-card" style="background:var(--color-secondary);border:none;">
        <div class="ea-card-kicker">What this means</div>
        <div class="ea-body" style="color:var(--color-text-primary);">{ASSESSMENT_RESULT['insight']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    b1, b2 = st.columns(2)
    if b1.button("Back to assessment", width="stretch", key="results-back"):
        st.session_state.assessment_submitted = False
        st.rerun()
    b2.button("See full skill gap →", type="primary", width="stretch", key="results-skillgap")
