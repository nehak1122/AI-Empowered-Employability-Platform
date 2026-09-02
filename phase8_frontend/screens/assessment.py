import streamlit as st
from components.badges import badge
from components.cards import icon_header, progress_bar_card, message_banner
from components.icons import icon
from components import charts
from data.dummy_data import ASSESSMENT_DOMAINS, ASSESSMENT_DIFFICULTIES, QUESTION_BANK


def render():
    if st.session_state.get("assessment_submitted"):
        _render_results()
    elif not st.session_state.get("assessment_domain") or not st.session_state.get("assessment_difficulty"):
        _render_domain_picker()
    else:
        _render_question_flow()


# ---------------------------------------------------------------- picker --

def _render_domain_picker():
    st.session_state.setdefault("_pick_domain", None)
    st.session_state.setdefault("_pick_difficulty", "easy")

    icon_header("skill_gap", "Select your domain")
    st.markdown(
        '<div class="ea-body" style="color:#6B7280;">Pick the track you want to be assessed on. '
        'This decides which questions you get for the rest of the assessment.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    cols = st.columns(len(ASSESSMENT_DOMAINS))
    for col, d in zip(cols, ASSESSMENT_DOMAINS):
        with col:
            selected = st.session_state._pick_domain == d["key"]
            border = "border-color:var(--color-primary);background:var(--color-accent-bg);" if selected else ""
            st.markdown(f"""
            <div class="ea-card" style="text-align:center;{border}min-height:170px;">
                <div class="ea-icon-badge" style="margin:0 auto 10px auto;">{icon(d['icon'], 'var(--color-primary)')}</div>
                <div class="ea-section" style="font-size:16px;">{d['name']}</div>
                <div class="ea-small" style="margin-top:6px;">{d['desc']}</div>
                <div class="ea-small" style="margin-top:8px;">{d['questions']} questions · ~{d['minutes']} min</div>
            </div>
            """, unsafe_allow_html=True)
            label = "✓ Selected" if selected else "Select"
            if st.button(label, key=f"pick-domain-{d['key']}", type="primary" if selected else "secondary", width="stretch"):
                st.session_state._pick_domain = d["key"]
                st.rerun()

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    icon_header("assessment", "Select difficulty")
    diff_cols = st.columns(len(ASSESSMENT_DIFFICULTIES))
    for col, level in zip(diff_cols, ASSESSMENT_DIFFICULTIES):
        with col:
            selected = st.session_state._pick_difficulty == level["key"]
            border = "border-color:var(--color-primary);background:var(--color-accent-bg);" if selected else ""
            st.markdown(f"""
            <div class="ea-card" style="{border}">
                <b>{level['name']}</b>
                <div class="ea-small" style="margin-top:2px;">{level['note']}</div>
            </div>
            """, unsafe_allow_html=True)
            label = "✓ Selected" if selected else "Select"
            if st.button(label, key=f"pick-diff-{level['key']}", type="primary" if selected else "secondary", width="stretch"):
                st.session_state._pick_difficulty = level["key"]
                st.rerun()

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    ready = st.session_state._pick_domain is not None
    if not ready:
        st.caption("Pick a domain above to continue.")
    if st.button("Start Assessment →", type="primary", width="stretch", disabled=not ready, key="start-assessment"):
        st.session_state.assessment_domain = st.session_state._pick_domain
        st.session_state.assessment_difficulty = st.session_state._pick_difficulty
        st.session_state.assessment_current_q = 0
        st.session_state.assessment_answers = {}
        st.rerun()


# ---------------------------------------------------------------- questions --

def _render_question_flow():
    domain_key = st.session_state.assessment_domain
    domain = next(d for d in ASSESSMENT_DOMAINS if d["key"] == domain_key)
    questions = QUESTION_BANK[domain_key]
    idx = st.session_state.assessment_current_q
    total = len(questions)
    q = questions[idx]
    answers = st.session_state.assessment_answers
    selected = answers.get(q["id"])

    st.markdown(f'<div class="ea-small" style="letter-spacing:.06em;text-transform:uppercase;">{domain["name"]} certification · {st.session_state.assessment_difficulty.title()}</div>', unsafe_allow_html=True)
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown('<div class="ea-heading">Assessment</div>', unsafe_allow_html=True)
    with top_r:
        st.markdown(f'<div style="text-align:right;padding-top:10px;color:#6B7280;">Question {idx + 1} of {total}</div>', unsafe_allow_html=True)
    st.progress((idx + 1) / total)

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
    if selected:
        st.markdown(
            f"<style>[class*=\"st-key-opt-{q['id']}-{selected}\"] {{ border-color: var(--color-primary) !important; "
            f"background: var(--color-accent-bg); }}</style>",
            unsafe_allow_html=True,
        )
    with st.container(border=True):
        st.markdown(f'<div class="ea-body" style="font-weight:600;font-size:18px;">{q["text"]}</div>', unsafe_allow_html=True)
        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

        for opt in q["options"]:
            is_selected = selected == opt["key"]
            css_key = f"opt-{q['id']}-{opt['key']}"
            with st.container(key=css_key):
                dot_class = "current" if is_selected else "pending"
                oc1, oc2 = st.columns([1, 12], vertical_alignment="center")
                with oc1:
                    st.markdown(f'<div class="ea-step-dot {dot_class}">{opt["key"]}</div>', unsafe_allow_html=True)
                with oc2:
                    if st.button(opt["text"], key=f"btn-{css_key}", width="stretch", disabled=selected is not None):
                        answers[q["id"]] = opt["key"]
                        st.rerun()

        if selected:
            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
            is_correct = selected == q["correct"]
            if is_correct:
                message_banner("Correct", q["explanations"][q["correct"]], kind="success")
            else:
                message_banner(f"Not quite - option {selected} is incorrect", q["explanations"][selected], kind="warning")
                message_banner(f"Why {q['correct']} is the right answer", q["explanations"][q["correct"]], kind="info")

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    nav1, nav2 = st.columns(2)
    with nav1:
        if st.button("← Previous", width="stretch", disabled=idx == 0, key="q-prev"):
            st.session_state.assessment_current_q -= 1
            st.rerun()
    with nav2:
        is_last = idx == total - 1
        label = "Finish assessment →" if is_last else "Next question →"
        if st.button(label, type="primary", width="stretch", disabled=selected is None, key="q-next"):
            if is_last:
                st.session_state.assessment_submitted = True
            else:
                st.session_state.assessment_current_q += 1
            st.rerun()

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
    if st.button("Exit to domain selection", key="switch-domain"):
        st.session_state.assessment_domain = None
        st.session_state.assessment_difficulty = None
        st.rerun()


# ---------------------------------------------------------------- results --

_LEVEL_COPY = [
    (80, "Excellent!", "You've demonstrated a strong grasp of the fundamentals."),
    (60, "Good job!", "Solid overall, with a couple of areas worth another look."),
    (0, "Keep practicing!", "The basics are there - a bit more practice will make a real difference."),
]


def _render_results():
    domain_key = st.session_state.assessment_domain
    domain = next(d for d in ASSESSMENT_DOMAINS if d["key"] == domain_key)
    questions = QUESTION_BANK[domain_key]
    answers = st.session_state.assessment_answers
    total = len(questions)
    correct_count = sum(1 for q in questions if answers.get(q["id"]) == q["correct"])
    overall_pct = round(correct_count / total * 100)
    verdict, verdict_sub = next((v, s) for t, v, s in _LEVEL_COPY if overall_pct >= t)

    categories = {}
    for q in questions:
        cat = q["category"]
        categories.setdefault(cat, {"correct": 0, "total": 0})
        categories[cat]["total"] += 1
        if answers.get(q["id"]) == q["correct"]:
            categories[cat]["correct"] += 1
    cat_scores = [
        {"name": c, "pct": round(v["correct"] / v["total"] * 100)}
        for c, v in categories.items()
    ]
    strengths = sorted([c for c in cat_scores if c["pct"] >= 70], key=lambda c: -c["pct"])
    improvements = sorted([c for c in cat_scores if c["pct"] < 70], key=lambda c: c["pct"])

    icon_header("check-circle", f"{domain['name']} · {st.session_state.assessment_difficulty.title()}")
    top_l, top_r = st.columns([2.4, 1])
    with top_l:
        st.markdown(f'<div class="ea-heading">Assessment completed - {verdict}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="ea-body" style="color:#6B7280;">{verdict_sub} Review your detailed breakdown below.</div>', unsafe_allow_html=True)
    with top_r:
        b1, b2 = st.columns(2)
        b1.button("Download report", key="dl-assessment-report")
        b2.button("Share result", type="primary", key="share-assessment-result")

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.2, 1.2])
    with c1:
        with st.container(border=True):
            st.markdown('<div class="ea-small" style="text-align:center;letter-spacing:.06em;text-transform:uppercase;">Overall score</div>', unsafe_allow_html=True)
            charts.score_ring(overall_pct, height=200)
            st.markdown(
                f'<div style="text-align:center;"><b>{correct_count}/{total} correct</b>'
                f'<div class="ea-small">Domain: {domain["name"]}</div></div>',
                unsafe_allow_html=True,
            )

    with c2:
        icon_header("trend", "Strengths")
        with st.container(border=True):
            if strengths:
                for s in strengths:
                    progress_bar_card(s["name"], s["pct"])
            else:
                st.caption("None of the categories cleared 70% this attempt - see improvement areas instead.")

    with c3:
        icon_header("alert", "Improvement areas")
        with st.container(border=True):
            if improvements:
                for w in improvements:
                    progress_bar_card(w["name"], w["pct"])
                weakest = improvements[0]
                weakest_q = next(q for q in questions if q["category"] == weakest["name"] and answers.get(q["id"]) != q["correct"])
                why = weakest_q["explanations"][weakest_q["correct"]].removeprefix("Correct. ")
                st.markdown(f"""
                <div class="ea-card" style="background:var(--color-accent-bg);border:none;margin-top:8px;">
                    <div class="ea-card-kicker">Recommended next step</div>
                    <div class="ea-body" style="font-size:14px;">Revisit <b>{weakest['name']}</b>. Key idea to review: {why}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.caption("No weak spots this attempt - every category cleared 70%.")

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3)
    with r1:
        with st.container(border=True):
            rc1, rc2 = st.columns([1, 5])
            rc1.markdown(f'<div class="ea-icon-badge">{icon("assessment", "var(--color-primary)")}</div>', unsafe_allow_html=True)
            rc2.markdown('<b>Review answers</b><br/><span class="ea-small">See detailed explanations.</span>', unsafe_allow_html=True)
            st.session_state.setdefault("_show_review", False)
            if st.button("Review answers", key="toggle-review", width="stretch"):
                st.session_state._show_review = not st.session_state._show_review
                st.rerun()
    with r2:
        with st.container(border=True):
            rc1, rc2 = st.columns([1, 5])
            rc1.markdown(f'<div class="ea-icon-badge">{icon("skill_gap", "var(--color-primary)")}</div>', unsafe_allow_html=True)
            rc2.markdown('<b>View skill gap</b><br/><span class="ea-small">Update your learning path.</span>', unsafe_allow_html=True)
            if st.button("View skill gap", key="goto-skillgap", width="stretch"):
                st.session_state.page = "skill_gap"
                st.rerun()
    with r3:
        with st.container(border=True):
            rc1, rc2 = st.columns([1, 5])
            rc1.markdown(f'<div class="ea-icon-badge">{icon("dashboard", "var(--color-primary)")}</div>', unsafe_allow_html=True)
            rc2.markdown('<b>Back to dashboard</b><br/><span class="ea-small">Return to home screen.</span>', unsafe_allow_html=True)
            if st.button("Back to dashboard", key="goto-dashboard", width="stretch"):
                st.session_state.page = "dashboard"
                st.rerun()

    if st.session_state.get("_show_review"):
        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
        icon_header("assessment", "Answer review")
        for i, q in enumerate(questions, start=1):
            sel = answers.get(q["id"])
            correct = sel == q["correct"]
            with st.expander(f"Q{i}. {q['text']}", expanded=False):
                st.markdown(f"Your answer: **{sel}** · Correct answer: **{q['correct']}**")
                if correct:
                    message_banner("Correct", q["explanations"][q["correct"]], kind="success")
                else:
                    message_banner(f"You chose {sel} - incorrect", q["explanations"][sel], kind="warning")
                    message_banner(f"Correct answer: {q['correct']}", q["explanations"][q["correct"]], kind="info")

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    if st.button("Retake this assessment", key="retake-assessment"):
        st.session_state.assessment_submitted = False
        st.session_state.assessment_domain = None
        st.session_state.assessment_difficulty = None
        st.session_state.assessment_current_q = 0
        st.session_state.assessment_answers = {}
        st.session_state._show_review = False
        st.rerun()
