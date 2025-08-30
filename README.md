# HR Resource Query Chatbot

## Overview
The HR Resource Query Chatbot is an intelligent assistant that helps recruiters and HR teams quickly search for employees or candidates based on **skills, experience, and projects**.  
It uses **semantic search with embeddings** and a **chat-style interface** to handle natural language queries. The system is built with **FastAPI** for the backend, **Streamlit** for the frontend, and integrates **LLMs** for query refinement (handling typos, grammar, and contextual understanding).

---

## Features
- 🔍 **Natural language queries** for employee search  
- 🧑‍💻 **Skill-based, project-based, and experience-based filtering**  
- ⚡ **FastAPI backend** with REST endpoints  
- 💬 **Streamlit frontend** with chat-style interface  
- 📊 Embedding-based **semantic search** using `all-MiniLM-L6-v2`  
- 🔑 Optional integration with **Gemini/OpenAI** for query correction  

---

## Architecture
**Components:**
1. **FastAPI Backend**  
   - `/employees/search` → GET endpoint for employee filtering  
   - `/chat` → POST endpoint for natural language queries  
   - Uses **sentence-transformers** for embeddings  
   - Optionally integrates **Gemini/OpenAI** for query correction  

2. **Streamlit Frontend**  
   - Simple **chat UI** for HR queries  
   - Calls FastAPI endpoints via REST APIs  
   - Displays chat history and search results  

3. **Dataset**  
   - JSON dataset of employee profiles  
   - Each entry contains: `name`, `skills`, `experience_years`, `projects`, `availability`

---
## Demo
https://hr-resource-query-chatbot-rishika.streamlit.app/


