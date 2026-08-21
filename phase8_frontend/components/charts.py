"""
Chart wrappers around Plotly, one function per chart type in the design
system (gauge, radar, bar, line, pie, heatmap). Every screen should reach
for one of these instead of building a chart inline, so a colour or style
fix only has to happen in one place.
"""

import plotly.graph_objects as go
import streamlit as st

PRIMARY = "#0EA4AF"
PRIMARY_DARK = "#0B7A82"
SECONDARY = "#AFDDE5"
GREY = "#D1D5DB"
TEXT_SECONDARY = "#6B7280"

_LAYOUT_DEFAULTS = dict(
    margin=dict(l=10, r=10, t=10, b=10),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Poppins, sans-serif", color="#111827"),
)


def gauge(value: int, max_value: int = 100, height: int = 220):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        number={"suffix": f"", "font": {"size": 40}},
        gauge={
            "axis": {"range": [0, max_value], "visible": False},
            "bar": {"color": PRIMARY, "thickness": 0.3},
            "bgcolor": "#EEF0F4",
            "borderwidth": 0,
        },
    ))
    fig.update_layout(height=height, **_LAYOUT_DEFAULTS)
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def radar(categories, you, compare, compare_label="Role requires", height=320):
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=compare + [compare[0]], theta=categories + [categories[0]],
        name=compare_label, line=dict(color=GREY, dash="dot"), fill="none",
    ))
    fig.add_trace(go.Scatterpolar(
        r=you + [you[0]], theta=categories + [categories[0]],
        name="You", line=dict(color=PRIMARY), fillcolor="rgba(14,164,175,0.25)", fill="toself",
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, showticklabels=False)),
        showlegend=True,
        legend=dict(orientation="h", y=-0.1),
        height=height, **_LAYOUT_DEFAULTS,
    )
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def bar(labels, values, warn_below=None, height=260):
    colors = [PRIMARY] * len(values)
    if warn_below is not None:
        colors = [SECONDARY if v < warn_below else PRIMARY for v in values]
    fig = go.Figure(go.Bar(
        x=labels, y=values, marker_color=colors,
        text=[f"{v}%" for v in values], textposition="outside",
        marker_line_width=0,
    ))
    fig.update_traces(marker=dict(cornerradius=6))
    fig.update_yaxes(visible=False, range=[0, max(values) * 1.25])
    fig.update_layout(height=height, **_LAYOUT_DEFAULTS)
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def line(x, student, cohort=None, target=None, height=260):
    fig = go.Figure()
    if target is not None:
        fig.add_hline(y=target, line_dash="dot", line_color=PRIMARY_DARK,
                       annotation_text=f"job-ready {target}", annotation_position="top left")
    if cohort is not None:
        fig.add_trace(go.Scatter(x=x, y=cohort, name="Cohort", line=dict(color=GREY, dash="dot")))
    fig.add_trace(go.Scatter(
        x=x, y=student, name="You", line=dict(color=PRIMARY, width=3),
        fill="tozeroy", fillcolor="rgba(14,164,175,0.12)",
    ))
    fig.update_layout(height=height, showlegend=cohort is not None, **_LAYOUT_DEFAULTS)
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def donut(labels, values, colors=(PRIMARY, SECONDARY, PRIMARY_DARK), height=260):
    fig = go.Figure(go.Pie(
        labels=labels, values=values, hole=0.6,
        marker=dict(colors=list(colors)),
        textinfo="none",
    ))
    fig.update_layout(height=height, showlegend=True, legend=dict(orientation="h", y=-0.1), **_LAYOUT_DEFAULTS)
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def heatmap(rows, cols, matrix, height=220):
    fig = go.Figure(go.Heatmap(
        z=matrix, x=cols, y=rows,
        colorscale=[[0, "#E9F7F8"], [1, PRIMARY]],
        showscale=False, xgap=4, ygap=4,
    ))
    fig.update_layout(height=height, **_LAYOUT_DEFAULTS)
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})
