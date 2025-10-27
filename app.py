# app.py
import streamlit as st
import pandas as pd
import datetime
import json

st.set_page_config(page_title="SyncUp - BPDC Resilience Hub", layout="wide")

# ------------------------------
# Helper Functions
# ------------------------------
def login_page():
    st.title("🔐 SyncUp Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Please enter both username and password.")

def dashboard():
    st.title("🏠 Dashboard")
    st.write("All-in-one student support app for BPDC students.")

    options = ["📚 Courses", "💬 Peer Chat", "📧 Inbox", "💼 Career Hub", "🗓️ Timetable Builder", "🧠 AI Productivity Bot"]
    choice = st.radio("Choose a section:", options)

    if choice == "📚 Courses":
        courses_page()
    elif choice == "💬 Peer Chat":
        peer_chat()
    elif choice == "📧 Inbox":
        inbox()
    elif choice == "💼 Career Hub":
        career_hub()
    elif choice == "🗓️ Timetable Builder":
        timetable_builder()
    elif choice == "🧠 AI Productivity Bot":
        ai_productivity_bot()

# ------------------------------
# Pages
# ------------------------------
def courses_page():
    st.subheader("📚 Courses")
    st.write("Explore your courses with curated playlists and practice materials.")

    with open("courses.json", "r") as f:
        courses = json.load(f)

    for course, links in courses.items():
        st.markdown(f"### 🎓 {course}")
        tab1, tab2 = st.tabs(["📺 Playlist", "📝 Practice Papers"])

        with tab1:
            st.video(links["playlist"])
            st.caption("Recommended YouTube playlist for deeper understanding.")

        with tab2:
            st.markdown(f"[📄 Access Practice Papers]({links['papers']})")
            st.caption("Practice questions from past exams and sample papers.")

        st.divider()


def peer_chat():
    st.subheader("💬 Peer Chat")
    chat_data = [
        {"sender": "Senior", "message": "Welcome to BPDC! Feel free to ask me anything."},
        {"sender": "Fresher", "message": "Thanks! Can you share tips for DAA exam?"},
        {"sender": "Senior", "message": "Yea sure. Practice problems and solve past year papers."},
    ]
    for chat in chat_data:
        st.markdown(f"**{chat['sender']}:** {chat['message']}")

def inbox():
    st.subheader("📧 Secure Inbox")
    inbox_items = [
        "[University] Mid-Semester Schedule",
        "[Placement Cell] Company Pre-Placement Talk",
        "[System Alert] Scam Alert – Avoid Phishing"
    ]
    for mail in inbox_items:
        st.markdown(f"- {mail}")

def career_hub():
    st.subheader("💼 Career Hub")
    careers = [
        {"company": "Deriv", "role": "AI intern", "alumni": "Nethradevi Baskar", "linkedin": "https://www.linkedin.com/in/nethradevi-baskar/"},
        {"company": "Google", "role": "Data Analyst Intern", "alumni": "John Doe", "linkedin": "https://www.linkedin.com/company/google/"},
        {"company": "Deloitte", "role": "Finance Analyst", "alumni": "Sarah Ali", "linkedin": "https://www.linkedin.com/company/deloitte/"}
    ]
    for job in careers:
        st.markdown(f"### {job['company']}")
        st.markdown(f"**Role:** {job['role']}")
        st.markdown(f"**Alumni:** {job['alumni']}")
        st.markdown(f"[🔗 Visit LinkedIn]({job['linkedin']})")
        st.divider()

def timetable_builder():
    st.subheader("🗓️ Timetable Builder")
    data = {
        "Mon": ["DAA"],
        "Tue": ["DBMS"],
        "Wed": ["OS"],
        "Thu": ["Math"],
        "Fri": ["AI"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

    if st.button("+ Add Custom Template"):
        st.info("Feature coming soon — design your own timetable!")


# ------------------------------
# Add AI Productivity Bot Page
# ------------------------------
def ai_productivity_bot():
    st.subheader("🧠 AI Productivity Bot")
    st.write("Plan your week effectively! Add tasks, set deadlines, and earn points for completing them on time.")

    # Initialize session states
    if "tasks" not in st.session_state:
        st.session_state.tasks = []
    if "points" not in st.session_state:
        st.session_state.points = 0

    # Task Input
    with st.form("add_task_form"):
        task = st.text_input("Enter your task:")
        deadline = st.date_input("Set a deadline:", min_value=datetime.date.today())
        submitted = st.form_submit_button("Add Task")
        if submitted and task:
            st.session_state.tasks.append({"task": task, "deadline": deadline, "completed": False})
            st.success(f"✅ Task '{task}' added!")

    # Display Tasks
    if st.session_state.tasks:
        st.write("### 🗓️ Your Tasks:")
        for i, t in enumerate(st.session_state.tasks):
            col1, col2, col3 = st.columns([3, 2, 2])
            col1.write(f"**{t['task']}**")
            col2.write(f"Deadline: {t['deadline']}")
            if not t["completed"]:
                if col3.button("Mark Complete", key=f"complete_{i}"):
                    t["completed"] = True
                    st.session_state.points += 10
                    st.success(f"🎉 Great job! You earned 10 points for completing '{t['task']}'!")
            else:
                col3.success("✅ Completed")

    else:
        st.info("No tasks yet — add one to get started!")

    st.divider()
    st.metric(label="🏆 Total Points", value=st.session_state.points)

    # Optional AI planning suggestion (mock version)
    if st.button("🤖 Suggest Weekly Plan"):
        st.info("AI Suggestion: Focus on your DAA assignment by Tuesday, complete OS lab report by Thursday, and prepare for AI quiz over the weekend!")


# ------------------------------
# Main Logic
# ------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
else:
    dashboard()
