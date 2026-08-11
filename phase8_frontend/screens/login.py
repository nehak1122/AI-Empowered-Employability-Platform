import streamlit as st


def render():
    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown("""
        <div class="ea-card-hero" style="min-height:520px;display:flex;flex-direction:column;justify-content:space-between;">
            <div>
                <div style="display:flex;align-items:center;gap:8px;">
                    <div style="width:28px;height:28px;border-radius:8px;background:rgba(255,255,255,.2);
                    display:flex;align-items:center;justify-content:center;font-weight:700;">E</div>
                    <span style="font-weight:600;">EmployaAI</span>
                </div>
                <div class="ea-small" style="color:rgba(255,255,255,.75);margin-top:32px;">BUILT FOR FINAL-YEAR STUDENTS</div>
                <div class="ea-heading" style="color:#fff;margin-top:8px;">Find out how job-ready you actually are.</div>
                <div class="ea-body" style="color:rgba(255,255,255,.85);margin-top:12px;">
                    We compare your profile against what employers are actually asking for right now,
                    tell you which skills you're short on, and give you a plan to fix them.
                </div>
            </div>
            <div>
                <div style="background:rgba(255,255,255,.12);border-radius:12px;padding:14px 16px;margin-bottom:12px;">
                    <div class="ea-small" style="color:rgba(255,255,255,.75);">Students gain this much, on average</div>
                    <div class="ea-subhead" style="color:#fff;">+14 points</div>
                </div>
                <div class="ea-small" style="color:rgba(255,255,255,.75);">
                    412 students so far &nbsp;·&nbsp; 58 certifications &nbsp;·&nbsp; 2 domains
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="ea-subhead">Welcome back</div>', unsafe_allow_html=True)
        st.markdown('<div class="ea-body" style="color:#6B7280;margin-bottom:16px;">Sign in and pick up where you left off.</div>', unsafe_allow_html=True)

        st.text_input("Email address", value="aarav.d@college.edu", key="login_email")
        st.text_input("Password", type="password", value="", placeholder="••••••••••", key="login_password")
        st.checkbox("Keep me signed in", value=True)

        if st.button("Sign in", type="primary", width="stretch"):
            st.session_state.authenticated = True
            st.session_state.page = "dashboard"
            st.rerun()

        st.markdown('<div style="text-align:center;color:#9CA3AF;margin:12px 0;">or</div>', unsafe_allow_html=True)
        st.button("Continue with Google", width="stretch")

        st.markdown(
            '<div style="text-align:center;margin-top:12px;color:#6B7280;">First time here? '
            '<span style="color:#6C5CE7;font-weight:600;">Create an account</span></div>',
            unsafe_allow_html=True,
        )
        st.caption("This is a static frontend preview — sign-in is a stand-in, no real auth or backend is wired up yet.")
