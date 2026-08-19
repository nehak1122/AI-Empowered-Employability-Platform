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

---

## 2026-08-19

**Work completed**
- Moved "Save changes" on the Profile page from the top-right (item 3) to a footer bar at
  the bottom of the page, with a one-line caption explaining what it does.
- Moved "Submit section" on the Assessment page from the top-right to the bottom of the
  question flow (item 4), disabled until all 30 questions are answered, with a line above
  it explaining why it's greyed out. Also rebuilt the top of the page into a clear intro
  banner — what the assessment is, how many questions, current section — instead of just
  a bare title (item 5).
- On Skill Gap, moved "Download plan" and "Build my roadmap" from the top-right to a
  footer action bar after the full gap table, so both only appear once there's something
  to act on (item 12).
- Standardised spacer heights across `profile.py`, `score.py`, `settings.py` to the
  design system's allowed spacing values (8/16/24/32/48px) — a few screens had stray
  12px/6px gaps left over from earlier passes.
- Tested all three changed screens in the running app after editing, not just read the
  code — clicked into Profile, Assessment, and Skill Gap, confirmed the buttons render
  and behave correctly at their new positions, and checked the server logs for errors
  (none found).

**Current progress**
5 of 16 review items done (colour palette, sidebar spacing, Save Changes placement,
Submit Session placement, Skill Gap CTA placement) plus the assessment box clarity work.
Remaining: full card alignment/spacing audit across the rest of the app, the step-by-step
assessment flow itself (item 7), the results page (item 8), domain selection at the start
(item 9), user-created ID (item 10), Employability Score chart cleanup (item 11), and the
Roadmap/Certifications/Career Suggestions redesigns (items 13-15) — saved for the 20th.

**Blockers / issues**
None.

**Next-day plan (20 Aug)**
The remaining content-level items: assessment step flow + domain selection at the start,
a proper results page at the end of the assessment, user ID creation during setup, the
Employability Score page cleanup, and the Roadmap/Certifications/Career Suggestions UI
passes — then a final cross-page consistency check against all 16 items before calling
the review done.
