import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load dataset
with open("employees.json", "r") as f:
    data = json.load(f)["employees"]

# Use a SentenceTransformer model (free, no API key needed)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert each employee profile into a text string
employee_texts = []
for emp in data:
    text = f"{emp['name']} | Skills: {', '.join(emp['skills'])} | " \
           f"Experience: {emp['experience_years']} years | " \
           f"Projects: {', '.join(emp['projects'])} | " \
           f"Availability: {emp['availability']}"
    employee_texts.append(text)

# Create embeddings
embeddings = model.encode(employee_texts)

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings, dtype=np.float32))

# Save index + employee mapping
faiss.write_index(index, "employee_index.faiss")
with open("employee_texts.json", "w") as f:
    json.dump(employee_texts, f)

print("✅ FAISS index built and saved!")
