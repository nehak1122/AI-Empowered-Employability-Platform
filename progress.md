# Progress — Task 3 (frontend build)

Honest, dated log. One entry per day this was actually worked on — nothing backdated,
nothing written in advance for days that haven't happened yet.

---

## 2026-08-11

**Work completed**
- Read the full v2 design pack (design system, component library, responsive rules, all
  eleven screens) and set up `phase8_frontend/` as the Streamlit frontend.
- Built the shared foundation: design-token CSS (`assets/styles.css`), the reusable
  component library (`components/` — navigation, cards, charts, badges, tables, modals),
  and the static dummy-data module (`data/dummy_data.py`).
- Shipped three fully working, tested screens: **Login, Dashboard, Student Profile** —
  wired into `app.py`, verified in-browser at desktop (1280px), tablet (768px), and
  phone (375px) widths.
- Also wrote (but did not wire into the running app) the remaining eight screens:
  Assessment, Employability Score, Skill Gap, Learning Roadmap, Certifications, Career
  Suggestions, Analytics, Reports. These exist as real code in `screens/`, pass a syntax
  check, but aren't switched on yet — see `decisions.md` for why.
- Found and fixed three real bugs by actually testing in the browser rather than just
  reading the code: a startup path crash, a tablet-width sidebar text bug, and a mobile
  bottom-nav layout bug caused by Streamlit's own responsive CSS. Full detail in
  `processes.md`.

**Current progress**
3 of 11 screens live and verified working (desktop/tablet/mobile). Foundation
(design system, component library, dummy data, routing) is done and doesn't need to be
redone for the remaining screens — wiring each one in from here is mechanical.

**Blockers / issues**
None blocking. Two things worth flagging:
- Local git is set to `nehak1122` / `nehakhetawat2@gmail.com`; if commits should show a
  different name, that needs to be changed in git config directly (not something I do
  automatically).
- Nothing has been pushed to GitHub yet — the repo has a remote configured
  (`neoaitech/Employability_Framework`), but pushing wasn't part of today's session.

**Next-day plan**
Wire in the next batch of already-written screens (Assessment, Employability Score are
the natural next two, since Profile → Assessment → Score is the flow order), then
Skill Gap and Learning Roadmap. Test each one in-browser the same way as today before
calling it done, same as today.

---

## 2026-08-13

**Work completed**
- Wired in all eight remaining screens — Assessment, Employability Score, Skill Gap,
  Learning Roadmap, Certifications, Career Suggestions, Analytics, Reports — plus
  Settings, into `app.py` and `utils/state.py`'s `LIVE_SCREENS` set. All eleven screens
  from the design pack are now live in the nav.
- Clicked through every single screen in the running app (not just a syntax check) at
  desktop (1280px), tablet (768px), and phone (375px) widths, and checked the server logs
  for runtime errors after each pass. Nothing broke.
- Specifically re-checked the table → stacked-card responsive pattern on Skill Gap and
  Certifications at phone width, since those are the two screens that actually use it —
  both held up correctly.
- One cosmetic-only note, not fixed because there's nothing to fix in the code: the emoji
  icons on the Reports cards sit a little close to their heading text in the browser —
  the markup has a normal space, it's just how that emoji glyph measures.

**Current progress**
All 11 of 11 screens live, wired, and verified working across all three breakpoints. No
open bugs. Still running entirely on static dummy data — no backend/ML integration.

**Blockers / issues**
None. Explicitly holding off on pushing to GitHub until told to — everything so far is
local commits only.

**Next-day plan**
Nothing scheduled yet — next steps depend on what the project lead wants reviewed first
(a live walkthrough, or pushing once given the go-ahead).
