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

---

## 2026-08-18

Project lead sent detailed review feedback (16 items) covering colour theme, spacing,
button placement, assessment flow, results, and per-page UI refinement across all 11
screens. Given the 18–20 Aug timeline, splitting this across the three days rather than
doing it all in one sitting — today is item 1 (colour palette) and item 6 (sidebar
spacing), the two foundational changes everything else builds on.

**Work completed**
- Replaced the entire purple palette (`#6C5CE7` / `#8B5CF6`) with the requested teal/cyan
  palette (`#0EA4AF` primary, `#AFDDE5` secondary) — updated the CSS design tokens first,
  then swapped every hardcoded hex value across 9 files (`screens/login.py`,
  `dashboard.py`, `roadmap.py`, `profile.py`, `careers.py`, `certifications.py`,
  `components/charts.py`, `components/navigation.py`) so nothing was left on the old
  colour by accident.
- Kept the semantic status colours (green/amber/red for success/warning/error) as-is —
  those carry meaning, not just decoration, so changing them wasn't part of "unify the
  palette." Replaced the one purely decorative off-palette colour (a violet donut-chart
  slice) with a teal-family shade instead.
- Fixed sidebar crowding: nav row height 38px → 44px, spacing between rows 2px → 6px,
  more breathing room around section labels (MAIN/INSIGHTS/OUTPUT) and sidebar padding.
- Verified in the running app (not just reading the CSS) — Dashboard and Learning Roadmap
  checked directly, other screens spot-checked via the shared component/token system
  since they all pull from the same `styles.css` and `components/` — a colour-only change
  doesn't need a full per-screen browser pass the way a layout change would.

**Current progress**
Colour palette and sidebar spacing done, consistent across the app. Remaining 14 items
from the feedback (card alignment, button placement on Profile/Skill Gap/Assessment,
assessment step flow + results page, domain selection at start, user-created ID,
Employability Score chart cleanup, Roadmap/Certifications/Career Suggestions page
redesigns, full cross-page consistency pass) are not started — deliberately, to keep
today's slice real and reviewable rather than showing 14 half-finished changes.

**Blockers / issues**
None.

**Next-day plan (19 Aug)**
Card alignment/spacing pass, button repositioning (Save Changes → bottom of Profile,
Submit Session → end of Assessment, Build Resume/Download Plan → end of Skill Gap flow),
and the Assessment box/flow clarity work — these are the layout-level items and make
sense to batch together before touching the deeper per-page content work on the 20th.
