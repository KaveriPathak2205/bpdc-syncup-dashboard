# bpdc-syncup-dashboard

An all-in-one Student Dashboard application designed to enhance academic organization, resource accessibility, and productivity for students. Built using Streamlit for rapid deployment and a clean, interactive user experience.

🚀 Features

SyncUp provides a centralized hub with several modules to help students manage their academic life:

📚 Course Materials: Access a structured list of courses with direct links to curated YouTube playlists and Google Drive folders for practice papers and notes.

📝 To-Do List & Gamification: A functional to-do list where students can add tasks, set deadlines, and track completion. Completing tasks rewards the user with points, adding a gamified element to productivity.

🗓️ Timetable Builder (Mock): A tool to visualize and manage a weekly schedule.

💼 Career Hub (Mock): A section dedicated to tracking placement drives and accessing interview preparation resources.

💬 Peer Chat & 📧 Inbox (Mock): Placeholder sections simulating communication tools for peer-to-peer interaction and administrative correspondence.

🔐 Simple Authentication: A basic login screen to gate access to the main dashboard.

🛠️ Local Setup and Installation

Follow these steps to run the SyncUp Dashboard on your local machine.

Prerequisites

Python 3.8+

pip (Python package installer)

Git (Optional, but recommended for cloning the repository)

Steps

Clone the Repository (If hosting on GitHub):

git clone [https://github.com/YourUsername/bpdc-syncup-dashboard.git](https://github.com/KaveriPathak2205/bpdc-syncup-dashboard.git)
cd bpdc-syncup-dashboard


(If not using Git, ensure you have app.py, requirements.txt, and courses.json in the same directory.)

Install Dependencies:
The project relies on Streamlit and Pandas. Install them using the provided requirements.txt file:

pip install -r requirements.txt


Run the Application:
Start the Streamlit server from the project directory:

streamlit run app.py


The application will open automatically in your web browser (usually at http://localhost:8501).

🗂️ Project Structure

File

Purpose

app.py

The main application logic. Contains all Streamlit UI components, session state management, and page functions.

requirements.txt

Lists the necessary Python libraries (streamlit, pandas) required to run the application.

courses.json

The static data source containing course names and their corresponding external links (YouTube playlists and practice papers).

Deployment Status
https://bpdc-syncup.streamlit.app/
