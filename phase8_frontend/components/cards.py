import streamlit as st
from components.badges import badge_html


def metric_card(label, value, delta=None, kicker=None):
    delta_html = ""
    if delta:
        delta_html = f'<div style="margin-top:6px;">{badge_html(delta, "success" if str(delta).startswith("+") else "neutral")}</div>'
    kicker_html = f'<div class="ea-card-kicker">{kicker}</div>' if kicker else ""
    st.markdown(f"""
    <div class="ea-card">
        {kicker_html}
        <div class="ea-small">{label}</div>
        <div class="ea-big-number" style="margin-top:4px;">{value}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)


def score_hero_card(score: int, band: str, vs_cohort: str, to_ready_points: int):
    st.markdown(f"""
    <div class="ea-card-hero">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div class="ea-small" style="color:rgba(255,255,255,.8);">Employability score</div>
            {badge_html(band, "neutral")}
        </div>
        <div class="ea-big-number" style="font-size:56px;margin-top:8px;">{score}</div>
        <div class="ea-small" style="color:rgba(255,255,255,.85);">out of 100</div>
        <div class="ea-small" style="color:rgba(255,255,255,.85);margin-top:10px;">
            vs batch average <b style="color:#fff;">{vs_cohort}</b><br/>
            to job-ready · <b style="color:#fff;">{to_ready_points} points</b>
        </div>
    </div>
    """, unsafe_allow_html=True)


def progress_bar_card(label, pct, right_label=None, tone="default"):
    tone_class = {"success": "success", "warning": "warning", "error": "error"}.get(tone, "")
    right = right_label if right_label is not None else f"{pct}%"
    st.markdown(f"""
    <div style="margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;font-size:14px;font-weight:500;margin-bottom:4px;">
            <span>{label}</span><span style="color:#6B7280;">{right}</span>
        </div>
        <div class="ea-progress-track">
            <div class="ea-progress-fill {tone_class}" style="width:{pct}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def message_banner(title, body, kind="info"):
    colors = {
        "success": ("#DCFCE7", "#15803D", "✓"),
        "warning": ("#FEF3C7", "#B45309", "!"),
        "error": ("#FEE2E2", "#B91C1C", "✕"),
        "info": ("#DBEAFE", "#1D4ED8", "i"),
    }
    bg, text, icon = colors.get(kind, colors["info"])
    st.markdown(f"""
    <div style="background:{bg};color:{text};border-radius:12px;padding:14px 16px;margin-bottom:12px;">
        <div style="font-weight:600;">{icon}  {title}</div>
        <div style="font-size:14px;margin-top:2px;">{body}</div>
    </div>
    """, unsafe_allow_html=True)


def section_header(title, subtitle=None, right_html=None):
    subtitle_html = f'<div class="ea-body" style="color:#6B7280;margin-top:2px;">{subtitle}</div>' if subtitle else ""
    left, right = st.columns([3, 1])
    with left:
        st.markdown(f'<div class="ea-heading">{title}</div>{subtitle_html}', unsafe_allow_html=True)
    with right:
        if right_html:
            st.markdown(f'<div style="text-align:right;padding-top:8px;">{right_html}</div>', unsafe_allow_html=True)
