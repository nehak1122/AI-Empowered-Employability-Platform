import streamlit as st
from components import charts
from data.dummy_data import CERT_RECOMMENDATIONS, CERT_TABLE
from components.tables import responsive_table


def render():
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown('<div class="ea-heading">Certification Recommendations</div>', unsafe_allow_html=True)
        st.markdown('<div class="ea-body" style="color:#6B7280;">58 certifications, ranked by how much each one closes per hour you would put in.</div>', unsafe_allow_html=True)
    with top_r:
        st.button("Compare", width="stretch")

    cols = st.columns(3)
    for col, c in zip(cols, CERT_RECOMMENDATIONS):
        with col:
            hero = c["rank"] == 1
            card_class = "ea-card-hero" if hero else "ea-card"
            text_color = "" if hero else ""
            rating = f' · ⭐ {c["rating"]}' if c["rating"] else ""
            st.markdown(f"""
            <div class="{card_class}">
                <div style="display:flex;justify-content:space-between;">
                    <div class="ea-small">{c['provider']} · RANK {c['rank']}</div>
                    <span class="ea-badge {'ea-badge-neutral' if hero else 'ea-badge-purple'}">Match {c['match']}</span>
                </div>
                <div class="ea-section" style="margin-top:6px;">{c['name']}</div>
                <div class="ea-small" style="margin-top:2px;">{c['level']} · {c['duration']} · {c['cost']}{rating}</div>
                <div class="ea-small" style="margin-top:8px;">
                    Gaps closed <b>{c['gaps_closed']}</b> · Score uplift <b>{c['uplift']}</b><br/>
                    Asked for in {c['asked_in']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.button("Add to roadmap" if hero else "Details", type="primary" if hero else "secondary", key=f"cert-{c['rank']}", width="stretch")

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    left, right = st.columns([1, 1.4])
    with left:
        st.markdown('<div class="ea-section">Is it worth the time?</div>', unsafe_allow_html=True)
        st.caption("Bigger bubble means a pricier exam. Top-left is where you want to be.")
        durations = [8, 4, 12, 3]
        uplifts = [9, 6, 7, 3]
        costs = [12700, 6200, 33000, 3800]
        names = ["SAA", "TF-A", "CKA", "AZ-900"]
        import plotly.graph_objects as go
        fig = go.Figure(go.Scatter(
            x=durations, y=uplifts, mode="markers+text", text=names, textposition="top center",
            marker=dict(size=[c / 800 for c in costs], color="#6C5CE7", opacity=0.75),
        ))
        fig.update_layout(
            height=260, margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Weeks", yaxis_title="Score uplift",
        )
        st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})

    with right:
        st.markdown('<div class="ea-section">All of them side by side</div>', unsafe_allow_html=True)
        headers = ["Certification", "Provider", "Level", "Duration", "Cost", "Uplift"]
        rows = [[c["name"], c["provider"], c["level"], c["duration"], c["cost"], c["uplift"]] for c in CERT_TABLE]

        def mobile_row(r):
            name, provider, level, duration, cost, uplift = r
            return f"""
            <div class="ea-card" style="margin-bottom:8px;">
                <b>{name}</b><br/>
                <span class="ea-small">{provider} · {level} · {duration} · {cost} · {uplift}</span>
            </div>
            """
        responsive_table(headers, rows, mobile_row)
