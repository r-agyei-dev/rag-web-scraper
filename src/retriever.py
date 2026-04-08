import faiss
import numpy as np

def build_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

def retrieve(query, model, index, chunk_texts, k=2):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)

    retrieved = [chunk_texts[i] for i in indices[0]]
    similarity_scores = 1 / (1 + distances[0])

    return retrieved, similarity_scores
