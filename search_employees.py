import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load index + data
index = faiss.read_index("employee_index.faiss")
with open("employee_texts.json", "r") as f:
    employee_texts = json.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def search_employees(query, top_k=3):
    # Create embedding for query
    query_vec = model.encode([query])
    query_vec = np.array(query_vec, dtype=np.float32)

    # Search in FAISS
    distances, indices = index.search(query_vec, top_k)

    # Return top employees
    results = [employee_texts[i] for i in indices[0]]
    return results

# Test
if __name__ == "__main__":
    query = "Suggest people for a React Native project"
    results = search_employees(query)
    print("🔎 Query:", query)
    print("✅ Results:")
    for r in results:
        print("-", r)
