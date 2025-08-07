from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    return model.encode(texts)

def build_index(texts):
    vectors = embed_texts(texts)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    return index, texts

def search(query, index, docs, k=3):
    q_vec = embed_texts([query])
    _, I = index.search(q_vec, k)
    return [docs[i] for i in I[0]]

# OPTIONAL: For standalone testing
if __name__ == "__main__":
    clauses = [
        "Procedures after 90 days are covered.",
        "Orthopedic surgeries allowed in Maharashtra.",
        "No coverage for pre-existing conditions within first year."
    ]
    query = "knee surgery in Pune with 4-month policy"
    index, db = build_index(clauses)
    print(search(query, index, db))