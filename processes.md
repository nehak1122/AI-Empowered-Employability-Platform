# Process notes — EmployaAI frontend

What actually happened while building this, including the mistakes, so there's a record
beyond just the final code.

## Reading the design pack first

Before writing anything, I read the full 25-page v2 design pack you uploaded
(`Version 2 Summary (Key Changes & Improvements).pdf`) — the design system, component
library, responsive rules, and all eleven screens. That's what everything below is built
against; there was no separate image mock-up needed since the pack already has full
desktop screens.

## Bugs hit while building, and how they were found

**1. The app crashed on first run — wrong file path.**
`app.py` opened `assets/styles.css` using a path relative to wherever Streamlit happened
to be launched from, not relative to the app file itself. First run threw
`FileNotFoundError`. Fixed by building the path off `os.path.dirname(__file__)` instead of
assuming the working directory.

**2. Tablet-width sidebar bug, found by actually resizing the browser.**
The plan was: sidebar narrows to an icon rail at tablet width, and the text labels get
hidden with CSS. That doesn't work, because Streamlit's `st.button` renders plain text —
there's no `<span>` around the label to hide, so the CSS rule targeting it did nothing,
and the text wrapped one letter per line down the sidebar instead. This only showed up
once I actually resized the preview to 768px and looked — it wasn't visible at desktop
width. Fixed by dropping the icon-rail idea in favour of a narrower sidebar (200px) with
`text-overflow: ellipsis`, which doesn't need a wrapper element to work.

**3. Mobile bottom nav rendered as a tall stack instead of a row, also found by resizing.**
The bottom navigation bar (Home / Score / Gaps / Learn / More) is built from five
`st.columns()`. At phone width, it wasn't a row — it was five full-width buttons stacked
on top of each other, taking up most of the screen. I inspected the actual computed CSS in
the browser (via dev-tools-style JS, since it wasn't obvious from the screenshot alone) and
found the cause: Streamlit has its own responsive CSS that forces columns to
`min-width: calc(100% - 24px)` below its own breakpoint, so my "make it a row" CSS was
losing to Streamlit's own mobile styles. Fixed by adding a more specific override scoped
just to that one container, so it doesn't affect columns anywhere else in the app.

**4. Deprecation warnings in the server log.**
Streamlit 1.55 warns that `use_container_width=True` is being replaced by `width="stretch"`
across every widget that takes it (buttons, charts, etc.). Not a functional bug, but left
alone it would print a warning on every single widget on every page. Cleaned up across all
files in one pass rather than leaving it half-fixed in some files and not others.

**5. The browser-automation tool used for testing got flaky at the phone viewport size**
(coordinate clicks kept timing out on the "Sign in" button specifically at 375px width).
Worked around it by triggering the same click via a JS `element.click()` call instead, to
confirm the app itself was behaving correctly rather than fighting the test tool. Once
confirmed, testing continued normally.

**6. Scope correction, mid-build.**
While building, I initially wrote all eleven screens in one sitting after being told not
to leave placeholder pages in the nav. That overshot what was actually wanted — the ask
was to keep the three-day pacing, just make sure whatever ships each day is real and
working rather than a stub. Caught this after you flagged it directly. The eight extra
screens (Assessment, Employability Score, Skill Gap, Learning Roadmap, Certifications,
Career Suggestions, Analytics, Reports) were already written and are kept in the repo —
deleting working code just to redo it later would be wasteful — but I disconnected them
from the running app (`app.py`'s `SCREENS` dict and `utils/state.py`'s `LIVE_SCREENS` set
both only list what ships today) so the nav doesn't advertise anything that isn't really
live.

## What was actually verified, not just assumed

Before calling any of this done, I ran the app locally, signed in, and clicked through
Dashboard and Profile at three widths — 1280px (desktop), 768px (tablet), and 375px
(phone) — and looked at each one, rather than just reading the code and assuming the CSS
would behave. Two of the bugs above (#2 and #3) would not have been caught without
actually doing that. After trimming the scope back down to three screens, I re-ran the
app once more to confirm the nav and bottom bar only show Dashboard and Profile, with no
dead links.

## What's not done yet

Eight of the eleven screens (Assessment, Employability Score, Skill Gap, Learning
Roadmap, Certifications, Career Suggestions, Analytics, Reports) are written and syntax-
checked but not switched on in the running app — see `decisions.md` for exactly what
"wiring one in" involves, and `progress.md` for the plan on when that happens.
