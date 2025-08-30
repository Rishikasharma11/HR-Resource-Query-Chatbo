from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import json
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

# -----------------------
# Load dataset
# -----------------------
with open("employees.json", "r") as f:
    data = json.load(f)

employees = data["employees"]

# -----------------------
# Embedding Model
# -----------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create FAISS index
texts = [
    f"{emp['name']} | Skills: {', '.join(emp['skills'])} | Experience: {emp['experience_years']} years | Projects: {', '.join(emp['projects'])} | Availability: {emp['availability']}"
    for emp in employees
]
embeddings = model.encode(texts, convert_to_numpy=True)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# -----------------------
# FastAPI app
# -----------------------
app = FastAPI()

class Employee(BaseModel):
    name: str
    skills: List[str]
    experience_years: int
    projects: List[str]
    availability: str

class ChatRequest(BaseModel):
    message: str


@app.get("/employees/search", response_model=List[Employee])
def search_employees(query: str = Query(..., description="Search for employees")):
    query_vec = model.encode([query], convert_to_numpy=True)
    D, I = index.search(query_vec, k=5)
    results = [employees[i] for i in I[0]]

    # ✅ Example post-filter
    if "react native" in query.lower():
        results = [emp for emp in results if "React Native" in emp['skills']]

    return results


@app.post("/chat")
def chat_query(chat: ChatRequest):
    """
    Chat-like endpoint for employee search.
    Example: { "message": "Find me a React Native dev with 3+ years experience" }
    """
    query_vec = model.encode([chat.message], convert_to_numpy=True)
    D, I = index.search(query_vec, k=5)
    results = [employees[i] for i in I[0]]

    return {
        "query": chat.message,
        "matches": results
    }
