import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="Employee Chat Search", page_icon="💼", layout="centered")

st.title("💼 Employee Chat Search")
st.write("Ask me to find employees by skills, projects, or experience.")

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# User input
user_input = st.text_input("💬 Your query:", placeholder="Find me a React Native dev with 3+ years experience")

if st.button("Search"):
    if user_input.strip():
        # Call FastAPI backend
        response = requests.post(API_URL, json={"message": user_input})
        if response.status_code == 200:
            data = response.json()
            results = data["matches"]

            # Store conversation
            st.session_state["messages"].append(("user", user_input))
            st.session_state["messages"].append(("bot", results))
        else:
            st.error("❌ Something went wrong with the API request!")

# Display chat history
for sender, msg in st.session_state["messages"]:
    if sender == "user":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown("**🤖 Bot:** Here are some matches:")
        for emp in msg:
            st.markdown(f"- {emp['name']} | Skills: {', '.join(emp['skills'])} | "
                        f"Experience: {emp['experience_years']} years | "
                        f"Projects: {', '.join(emp['projects'])} | "
                        f"Availability: {emp['availability']}")
