"""
Static placeholder data standing in for the phase1-phase7 pipeline output.
Every screen reads from here instead of hitting real logic. Swapping this
module for real service calls is the whole point of keeping it separate -
none of the screens should need to change when that happens.
"""

STUDENT = {
    "name": "Aarav Deshpande",
    "initials": "AD",
    "track": "Cloud Computing",
    "semester": "Sem 6",
    "email": "aarav.d@college.edu",
    "phone": "+91 98•••210",
    "enrolment_id": "S-1042",
    "degree": "B.E. Computer Engineering",
    "cgpa": 8.24,
    "github": "github.com/aaravd",
    "linkedin": "linkedin.com/in/aaravd",
    "languages": "English, Hindi, Marathi",
    "profile_completion": 74,
}

SCORE = {
    "overall": 74,
    "band": "Band B",
    "verdict": "Near-ready",
    "cohort_average": 61.4,
    "job_ready_threshold": 80,
    "percentile": 68,
    "cohort_size": 412,
    "points_this_week": 4,
    "confidence": 0.86,
}

SCORE_BREAKDOWN = [
    {"label": "Technical skills", "value": 78, "cohort": 65},
    {"label": "Aptitude", "value": 71, "cohort": 68},
    {"label": "Communication", "value": 66, "cohort": 60},
    {"label": "Resume quality", "value": 68, "cohort": 62},
    {"label": "Projects", "value": 64, "cohort": 58},
    {"label": "Certifications", "value": 48, "cohort": 55},
    {"label": "Company readiness", "value": 73, "cohort": 63},
]

SCORE_DRIVERS = [
    {"label": "CGPA 8.24", "impact": 9.1},
    {"label": "Technical MCQ 82%", "impact": 7.2},
    {"label": "Networking depth", "impact": 4.8},
    {"label": "No IaC exposure", "impact": -7.3},
    {"label": "Thin AWS security", "impact": -4.8},
    {"label": "No internship", "impact": -3.0},
]

SCORE_HISTORY = {
    "months": ["Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    "student": [45, 52, 58, 63, 68, 74],
    "cohort": [40, 44, 48, 52, 57, 61],
    "target": 80,
}

SKILLS_OVERVIEW = [
    {"skill": "Networking", "level": "Strong", "score": 4, "max": 5},
    {"skill": "Python", "level": "Strong", "score": 4, "max": 5},
    {"skill": "Linux admin", "level": "Growing", "score": 3, "max": 5},
    {"skill": "AWS core", "level": "Growing", "score": 2, "max": 5},
    {"skill": "Terraform / IaC", "level": "Gap", "score": 1, "max": 5},
]

QUICK_ACTIONS = [
    {"label": "Continue assessment", "hint": "Technical - 12 of 30 done", "icon": "▶"},
    {"label": "Update resume", "hint": "Last uploaded 26 Jul", "icon": "📄"},
    {"label": "Continue learning", "hint": "Week 3 - Terraform", "icon": "📘"},
    {"label": "Download report", "hint": "Updated today", "icon": "⬇"},
]

RECENT_ACTIVITY = [
    {"text": "Your score went from 70 to 74", "when": "Today, 4:12 PM", "kind": "success"},
    {"text": "You finished week 2 of your plan", "when": "Yesterday", "kind": "success"},
    {"text": "AWS Cloud Practitioner added", "when": "27 Jul", "kind": "info"},
    {"text": "You uploaded a new resume", "when": "26 Jul", "kind": "neutral"},
]

JOB_MATCHES = [
    {"role": "Cloud Support Associate", "match": 86},
    {"role": "DevOps Trainee", "match": 74},
    {"role": "SOC Analyst L1", "match": 61},
]

ASSESSMENT_SECTIONS = [
    {"name": "Technical MCQ", "status": "Done", "score": "82%"},
    {"name": "Aptitude", "status": "Done", "score": "71%"},
    {"name": "Communication", "status": "In progress", "score": "6/15 answered"},
    {"name": "Domain - Cloud", "status": "Locked", "score": "45 min - not started"},
]

ASSESSMENT_DOMAINS = [
    {"key": "cloud", "name": "Cloud Computing", "desc": "AWS, networking, IaC, and cloud security fundamentals.", "questions": 30, "minutes": 45},
    {"key": "cyber", "name": "Cybersecurity", "desc": "Threats, identity and access, incident response basics.", "questions": 28, "minutes": 40},
]

ASSESSMENT_RESULT = {
    "overall": 76,
    "band": "Band B - Near-ready",
    "sections": [
        {"name": "Technical MCQ", "score": 82},
        {"name": "Aptitude", "score": 71},
        {"name": "Communication", "score": 66},
        {"name": "Domain - Cloud", "score": 84},
    ],
    "strengths": [
        "Strong grasp of IAM and access-control scenarios - scored in the top band on every identity question.",
        "Networking fundamentals are solid across both the technical and domain sections.",
    ],
    "weaknesses": [
        "Infrastructure-as-code questions were the weakest area - most Terraform-related questions were missed.",
        "Communication section ran short on time - 4 questions were left unanswered.",
    ],
    "insight": "This attempt moved your employability score from 70 to 74. Closing the IaC gap alone is worth "
               "roughly 7 more points - it's the single highest-impact thing to fix before your next attempt.",
}

RECOMMENDATIONS = [
    {"provider": "HC", "title": "Terraform Associate", "meta": "4 weeks - closes 2 gaps - ₹6,200", "tag": "Best fit"},
    {"provider": "AWS", "title": "Solutions Architect - Associate", "meta": "8 weeks - closes 3 gaps - ₹12,700", "tag": "Week 5"},
]

# --- Profile screen ---

PROFILE_STEPS = [
    {"label": "Personal details", "status": "done"},
    {"label": "Education", "status": "done"},
    {"label": "Skills & certifications", "status": "current"},
    {"label": "Projects", "status": "pending"},
    {"label": "Internship", "status": "pending"},
    {"label": "Resume & links", "status": "pending"},
    {"label": "Preview profile", "status": "pending"},
]

EDUCATION = [
    {"level": "B.E. Computer Engineering", "meta": "2023 - 2027 - Sem 6 - No backlogs", "score": "8.24"},
    {"level": "HSC - Science", "meta": "2023", "score": "88%"},
]

SKILLS = [
    {"name": "Python", "level": 4},
    {"name": "Networking", "level": 4},
    {"name": "Linux", "level": 3},
    {"name": "AWS core", "level": 2},
    {"name": "Terraform", "level": 1, "warning": True},
]

CERTIFICATIONS_HELD = [
    {"badge": "AWS", "name": "Cloud Practitioner", "meta": "Amazon - Mar 2026", "status": "Verified"},
    {"badge": "CSC", "name": "CCNA", "meta": "Cisco - Nov 2025", "status": "Verified"},
]

PROJECTS = [
    {"title": "Campus bus tracker", "meta": "Team of 3",
     "desc": "Live GPS tracking with a Flask backend and a Postgres store, deployed on a single EC2 instance.",
     "tags": ["Python", "Flask", "AWS EC2"]},
]

RESUME = {"filename": "Aarav_Deshpande_v2.pdf", "meta": "Parsed - 26 Jul - 214 KB", "score": 68}

# --- Skill gap screen ---

SKILL_GAP_ROWS = [
    {"skill": "Terraform / IaC", "asked": "61 of 74 postings", "required": "Level 3", "have": "Level 0",
     "priority": "High", "action": "Terraform Associate track, weeks 3-5", "impact": -7.3},
    {"skill": "AWS IAM & security", "asked": "58 of 74 postings", "required": "Level 3", "have": "Level 1",
     "priority": "High", "action": "AWS Solutions Architect - Associate", "impact": -4.8},
    {"skill": "Containers / K8s", "asked": "44 of 74 postings", "required": "Level 2", "have": "Level 1",
     "priority": "Medium", "action": "Docker fundamentals, then a single-node cluster", "impact": -3.1},
    {"skill": "Shell scripting", "asked": "Not in curriculum", "required": "Level 2", "have": "Level 1",
     "priority": "Medium", "action": "Self-study, week 2 of the roadmap", "impact": -1.9},
    {"skill": "CI/CD pipelines", "asked": "31 of 74 postings", "required": "Level 2", "have": "Level 1",
     "priority": "Medium", "action": "Build one pipeline on the bus-tracker project", "impact": -1.6},
    {"skill": "Linux admin", "asked": "71 of 74 postings", "required": "Level 2", "have": "Level 3",
     "priority": "Met", "action": "Nothing needed", "impact": 0.0},
    {"skill": "Networking", "asked": "71 of 74 postings", "required": "Level 2", "have": "Level 3",
     "priority": "Met", "action": "Nothing needed", "impact": 0.0},
]

RADAR_ROLE = {
    "categories": ["Networking", "Linux", "Python", "Containers", "IaC", "AWS security"],
    "you": [4, 4, 4, 2, 0, 1],
    "role_requires": [3, 3, 2, 2, 3, 3],
}

# --- Learning roadmap ---

ROADMAP_PHASES = [
    {"title": "Foundation", "weeks": "Week 1-4", "status": "In progress",
     "desc": "Linux, shell scripting, then your first Terraform files. None of this costs anything to run.",
     "progress": 55},
    {"title": "Core cloud skills", "weeks": "Week 5-8", "status": "Upcoming",
     "desc": "AWS IAM and networking properly, containers from Docker up to a single-node cluster.",
     "progress": 0},
    {"title": "Job-ready & cert prep", "weeks": "Week 9-12", "status": "Upcoming",
     "desc": "CI/CD on your own project, then four weeks of AWS SAA preparation and mock exams.",
     "progress": 0},
]

ROADMAP_TIMELINE = [
    {"track": "Linux & shell", "start_week": 1, "end_week": 3, "status": "done"},
    {"track": "Terraform / IaC", "start_week": 3, "end_week": 5, "status": "now"},
    {"track": "AWS IAM & security", "start_week": 5, "end_week": 7, "status": "upcoming"},
    {"track": "Containers / K8s", "start_week": 7, "end_week": 9, "status": "upcoming"},
    {"track": "CI/CD pipelines", "start_week": 9, "end_week": 10, "status": "upcoming"},
    {"track": "AWS SAA prep", "start_week": 10, "end_week": 12, "status": "upcoming"},
]

THIS_WEEK = [
    {"title": "Terraform providers & state", "meta": "2 readings - 1 lab - checkpoint quiz", "status": "active"},
    {"title": "Week 2 - Shell scripting basics", "meta": "", "status": "done"},
    {"title": "Week 4 - Modules, remote state, a small VPC", "meta": "", "status": "next"},
]

# --- Certifications ---

CERT_RECOMMENDATIONS = [
    {"provider": "AWS", "vendor": "Amazon", "rank": 1, "match": 0.91, "name": "Solutions Architect - Associate",
     "level": "Intermediate", "duration": "8 weeks", "cost": "₹12,700", "rating": 4.8,
     "gaps_closed": "3 of 7", "uplift": "+9 points", "asked_in": "38 of 74 roles",
     "skills": ["AWS IAM", "Networking", "Architecture"]},
    {"provider": "HC", "vendor": "HashiCorp", "rank": 2, "match": 0.83, "name": "Terraform Associate",
     "level": "Beginner", "duration": "4 weeks", "cost": "₹6,200", "rating": None,
     "gaps_closed": "2 of 7", "uplift": "+6 points", "asked_in": "24 of 74 roles", "skills": []},
    {"provider": "CNF", "vendor": "CNCF", "rank": 3, "match": 0.77, "name": "Certified Kubernetes Administrator",
     "level": "Advanced", "duration": "12 weeks", "cost": "₹33,000", "rating": None,
     "gaps_closed": "2 of 7", "uplift": "+7 points", "asked_in": "19 of 74 roles", "skills": []},
]

CERT_TABLE = [
    {"name": "Solutions Architect - Associate", "provider": "Amazon", "level": "Intermediate",
     "duration": "8 weeks", "cost": "₹12,700", "uplift": "+9"},
    {"name": "Terraform Associate", "provider": "HashiCorp", "level": "Beginner",
     "duration": "4 weeks", "cost": "₹6,200", "uplift": "+6"},
    {"name": "Certified Kubernetes Administrator", "provider": "CNCF", "level": "Advanced",
     "duration": "12 weeks", "cost": "₹33,000", "uplift": "+7"},
    {"name": "Azure Fundamentals", "provider": "Microsoft", "level": "Beginner",
     "duration": "3 weeks", "cost": "₹3,800", "uplift": "+3"},
    {"name": "Cloud Practitioner", "provider": "Amazon", "level": "Beginner",
     "duration": "-", "cost": "-", "uplift": "held"},
]

# --- Career suggestions ---

CAREER_MATCHES = [
    {"role": "Cloud Support Associate", "match": 86, "status": "Ready now",
     "skills_ok": ["Linux", "Networking", "Python"], "skills_gap": ["AWS depth", "IaC"],
     "salary": "₹5.2 - 7.0 LPA", "hiring": "TCS, Rackspace, Zensar", "openings": 23},
    {"role": "Cloud Ops / DevOps Trainee", "match": 74, "status": "2 gaps away",
     "skills_ok": ["Linux", "Python"], "skills_gap": ["Terraform", "CI/CD", "Containers"],
     "salary": "₹6.5 - 9.0 LPA", "hiring": "Infosys, Persistent, Quest", "openings": 17},
    {"role": "SOC Analyst L1", "match": 61, "status": "Stretch",
     "skills_ok": ["Networking"], "skills_gap": ["SIEM", "Incident handling", "Log analysis"],
     "salary": "₹4.8 - 6.5 LPA", "hiring": "Wipro, Deloitte, LTIMindtree", "openings": 11},
]

FIT_BREAKDOWN = [
    {"label": "Skills match", "value": 88},
    {"label": "Academic fit", "value": 82},
    {"label": "Project evidence", "value": 79},
    {"label": "Certification match", "value": 50},
]

ROLE_REQUIREMENTS = [
    {"item": "Linux and networking fundamentals", "asked": "71 of 74", "status": "Met"},
    {"item": "One cloud provider at associate depth", "asked": "68 of 74", "status": "Partial"},
    {"item": "Scripting for automation", "asked": "55 of 74", "status": "Partial"},
    {"item": "Ticketing and customer communication", "asked": "49 of 74", "status": "Met"},
    {"item": "Infrastructure as code exposure", "asked": "41 of 74", "status": "Gap"},
    {"item": "A named cloud certification", "asked": "38 of 74", "status": "Partial"},
]

# --- Analytics ---

ANALYTICS_SUMMARY = [
    {"label": "Assessments taken", "value": "6", "delta": "+2"},
    {"label": "Average performance", "value": "76%", "delta": "+9%"},
    {"label": "Learning hours", "value": "18", "delta": "Target 24"},
    {"label": "Skills improved", "value": "4 of 11", "delta": ""},
]

SECTION_PERFORMANCE = [
    {"section": "Technical", "score": 82},
    {"section": "Aptitude", "score": 71},
    {"section": "Comms", "score": 66},
    {"section": "Resume", "score": 68},
    {"section": "Certs", "score": 48},
]

HOURS_LOGGED = [
    {"month": "May", "hours": 26, "target": 24, "met": True},
    {"month": "June", "hours": 24, "target": 24, "met": True},
    {"month": "July", "hours": 18, "target": 24, "met": False},
]

SKILL_PRACTICE_HEATMAP = {
    "skills": ["Linux", "Python", "Networking", "AWS", "Terraform", "Containers"],
    "months": ["Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    "matrix": [
        [1, 2, 2, 3, 2, 1],
        [2, 3, 1, 0, 0, 0],
        [3, 2, 1, 1, 1, 0],
        [0, 0, 1, 2, 3, 2],
        [0, 0, 0, 1, 2, 3],
        [0, 0, 0, 0, 1, 1],
    ],
}

ATTEMPT_HISTORY = [
    {"name": "Technical - Cloud", "when": "28 Jul - attempt 2", "score": "82%", "kind": "success"},
    {"name": "Aptitude", "when": "28 Jul - attempt 1", "score": "71%", "kind": "success"},
    {"name": "Technical - Cloud", "when": "14 Jun - attempt 1", "score": "64%", "kind": "warning"},
    {"name": "Resume review", "when": "26 Jul - v2", "score": "68%", "kind": "success"},
    {"name": "Communication", "when": "In progress", "score": "6/15", "kind": "warning"},
]

# --- Reports ---

REPORT_CONTENTS = [
    {"item": "Employability score and components", "included": True},
    {"item": "Skill gap table", "included": True},
    {"item": "Learning roadmap", "included": True},
    {"item": "Assessment answer sheet", "included": False},
    {"item": "Cohort comparison", "included": False},
]

REPORT_HISTORY = [
    {"name": "Full employability report", "when": "31 Jul 2026, 4:14 PM", "score": 74, "size": "1.2 MB"},
    {"name": "Progress report", "when": "30 Jun 2026", "score": 68, "size": "640 KB"},
    {"name": "Full employability report", "when": "14 Jun 2026", "score": 64, "size": "1.1 MB"},
    {"name": "Skill gap summary", "when": "02 May 2026", "score": 58, "size": "420 KB"},
]
