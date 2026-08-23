import streamlit as st
from components.badges import badge_html
from components.icons import icon


def icon_header(icon_key, title, right_html=None):
    """Icon-in-circle + bold title, the header pattern every card section
    uses now instead of a bare heading - keeps every page's section
    headers looking like one design language instead of plain text."""
    right = f'<div style="margin-left:auto;">{right_html}</div>' if right_html else ""
    st.markdown(f"""
    <div class="ea-header-row">
        <div class="ea-icon-badge">{icon(icon_key, 'var(--color-primary)')}</div>
        <div class="ea-section" style="font-size:18px;">{title}</div>
        {right}
    </div>
    """, unsafe_allow_html=True)


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


def progress_bar_card(label, pct, right_label=None, tone="scale"):
    """Every progress bar in the app fills with the same teal, at a depth
    that scales with the value - strength/completeness reads through shade,
    not through switching to red/amber/green. The badge or text next to it
    still carries any pass/fail meaning, same as the design system's rule
    that colour is never the only signal."""
    if tone == "scale":
        if pct >= 75:
            fill = "var(--color-primary)"
        elif pct >= 45:
            fill = "rgba(14, 164, 175, 0.6)"
        else:
            fill = "rgba(14, 164, 175, 0.3)"
    else:
        fill = {
            "success": "var(--color-success)",
            "warning": "var(--color-warning)",
            "error": "var(--color-error)",
            "muted": "#D1D5DB",
        }.get(tone, "var(--color-primary)")
    right = right_label if right_label is not None else f"{pct}%"
    st.markdown(f"""
    <div style="margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;font-size:14px;font-weight:500;margin-bottom:4px;">
            <span>{label}</span><span style="color:#6B7280;">{right}</span>
        </div>
        <div class="ea-progress-track">
            <div class="ea-progress-fill" style="width:{pct}%;background:{fill};"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def message_banner(title, body, kind="info"):
    """Stands in for st.info/st.warning/st.error, which render in
    Streamlit's own fixed blue/amber/red and ignore the app's theme
    entirely - this keeps every inline message on the same teal palette
    as everything else, distinguished by icon rather than an off-brand
    hue."""
    styles = {
        "success": ("#E3F5F7", "#0B7A82", "check-circle"),
        "warning": ("#AFDDE5", "#0B7A82", "alert"),
        "error": ("#0EA4AF", "#FFFFFF", "alert"),
        "info": ("#E3F5F7", "#0B7A82", "bell"),
    }
    bg, text, icon_key = styles.get(kind, styles["info"])
    st.markdown(f"""
    <div style="background:{bg};color:{text};border-radius:var(--radius);padding:14px 16px;margin-bottom:12px;display:flex;gap:10px;align-items:flex-start;">
        <div style="flex-shrink:0;margin-top:1px;">{icon(icon_key, text)}</div>
        <div>
            <div style="font-weight:600;">{title}</div>
            <div style="font-size:14px;margin-top:2px;">{body}</div>
        </div>
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
