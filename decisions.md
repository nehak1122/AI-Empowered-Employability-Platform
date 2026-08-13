# Decisions — EmployaAI frontend

This is a plain-language record of the choices made while building the Streamlit frontend
in `phase8_frontend/`, and why. Written so you can explain any of it in a review without
having to re-read the code first.

## Where the frontend lives

The repo already had a numbering pattern for the pipeline: `phase1_data_integration`
through `phase7_feedback_loop`. The frontend isn't really one of those pipeline steps —
it sits on top of all of them — but you asked me to keep the same numbering convention,
so I called it `phase8_frontend` rather than inventing a different naming scheme. If you'd
rather it just be `frontend/` at the root, it's a plain folder rename, nothing else depends
on the number.

## One app, not Streamlit's built-in multipage system

Streamlit has a built-in way to make multi-page apps (a `pages/` folder where each file
becomes a page), but its automatic sidebar is a flat list — it can't do the grouped,
badged navigation the design calls for (MAIN / INSIGHTS / OUTPUT sections, a "7" badge
next to Skill Gap, an active-page highlight). So instead there's one `app.py` that decides
which "screen" to show based on a value stored in the session (`st.session_state.page`),
and the sidebar is hand-built to match the design exactly. Every screen still lives in its
own file — it just isn't Streamlit's native multipage mechanism doing the routing.

## Why a separate `data/dummy_data.py`

Every number, name, and status you see (Aarav Deshpande, a score of 74, the skill gap
table, the roadmap weeks) lives in one file: `data/dummy_data.py`. No screen computes or
hardcodes its own numbers. The reason is entirely about what happens later: when the
ML/data pipeline (phase1–phase7) is ready to plug in, that one file is what gets replaced
with real API or database calls — the screens themselves shouldn't need to change, because
they don't know or care whether the data is fake or real.

## Why a component library instead of styling each screen by hand

The design pack is explicit about this: "if something close already exists, use it."
So `components/` has one function per reusable piece — cards, badges, charts, tables,
navigation, pop-ups — and every screen is built by calling those functions rather than
writing its own HTML/CSS each time. If a color or spacing value needs to change later,
it changes in one place and every screen picks it up.

## How the colours/fonts/spacing are enforced

Everything from the Design System page of the pack (colours, the six text sizes, the five
spacing values, the one corner radius, the one shadow) is defined once as CSS custom
properties in `assets/styles.css`, and the components reference those instead of raw hex
codes or pixel values scattered through the code. This is the same idea as the component
library, one level lower — a single source of truth for "what does this look like."

## How "responsive" actually works in Streamlit

This is the trickiest part, worth explaining properly. Streamlit re-runs your Python script
top to bottom on every interaction, and it doesn't give you a live "how wide is the
browser right now" value in Python — that only exists in the browser, via CSS. So true
responsiveness (desktop sidebar → tablet rail → mobile drawer, a table turning into
stacked cards) is done with CSS breakpoints, not Python logic:

- **Charts, cards, and general reflow** — Streamlit's own column system already stacks
  columns vertically below a certain width, so a lot of this comes "for free."
- **The sidebar** — narrows itself at tablet width and reverts to a slide-in drawer on
  mobile, using Streamlit's own collapsible sidebar behaviour, styled to match the pack.
- **Tables → cards on mobile** — both versions are rendered every time (a real table, and
  a stacked-card list of the same rows); CSS shows only one of them depending on screen
  width. It's a little more HTML than strictly needed, but it means nothing has to be
  recomputed or reloaded when you resize the window.
- **The bottom nav bar on phones** — only exists as a fixed strip below 768px width; above
  that, it's not shown at all.

The trade-off: because Streamlit itself also has some built-in responsive rules (for
example, it forces its own columns to stack under a certain width), a couple of spots
needed CSS written specifically to override Streamlit's default behaviour rather than
just adding new rules on top. Details on where that came up are in `processes.md`.

## Charts

The pack specifies six chart types (gauge, radar, bar, line, progress, pie/donut,
heatmap). All of them are done with Plotly, wrapped in `components/charts.py` — one
function per chart type, so a screen just calls `charts.bar(...)` or `charts.radar(...)`
rather than configuring Plotly from scratch each time.

## Scope for today

Shipped in stages: first Login, Dashboard, and Student Profile only (tested and verified
before moving on), then the remaining eight screens once you confirmed you wanted the
full set wired in rather than held back. All eleven screens are now live in `app.py` and
were re-tested at desktop, tablet, and mobile widths after wiring them in. The nav only
shows entries for screens that are actually live — there's no "coming soon" placeholder
page anywhere in the app; a nav item either works or it isn't there. See `progress.md`
for the day-by-day record of when each batch shipped.
