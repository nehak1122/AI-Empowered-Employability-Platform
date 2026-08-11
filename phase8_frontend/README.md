# EmployaAI frontend (phase8_frontend)

Streamlit frontend for the AI-Powered Employability Assessment Platform, built against the
v2 design pack (`Version 2 Summary (Key Changes & Improvements).pdf` in the repo root).
Runs entirely on static data in `data/dummy_data.py` — no backend or ML integration yet.

## Run it

```bash
cd phase8_frontend
pip install -r requirements.txt
streamlit run app.py
```

## Layout

- `app.py` — entry point: page config, global CSS, session routing.
- `assets/styles.css` — design tokens (colours, type scale, spacing, radius, shadow) and
  the responsive breakpoints (1440 / 768 / 390, matching the design pack).
- `components/` — the reusable piece library: navigation, cards, charts, badges, tables,
  modals. Screens are built from these, not from one-off markup.
- `data/dummy_data.py` — every static value the screens read. This is the single place to
  swap for real API/DB calls later.
- `screens/` — one module per screen, each exposing a `render()` function.
- `utils/state.py` — session-state routing and the nav item list.

See `decisions.md` and `processes.md` in the repo root for the reasoning behind these choices
and what happened while building it. `progress.md` has the dated work log.

## Status

Built so far: Login, Dashboard, Student Profile, Assessment, Employability Score.
Remaining: Skill Gap, Learning Roadmap, Certifications, Career Suggestions, Analytics, Reports —
these currently render a "not built yet" placeholder in the app.
