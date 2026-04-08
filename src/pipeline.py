import time
import numpy as np
from src.retriever import retrieve
from src.generator import generate_answer

def run_rag_pipeline(query, embed_model, index, chunk_texts, tokenizer, model_llm, k=2):

    start_time = time.time()

    # Retrieve
    retrieved_chunks, similarity_scores = retrieve(
        query, embed_model, index, chunk_texts, k
    )

    # Generate
    answer = generate_answer(
        query, retrieved_chunks, tokenizer, model_llm
    )

    end_time = time.time()

    metrics = {
        "latency_sec": round(end_time - start_time, 3),
        "num_chunks_retrieved": len(retrieved_chunks),
        "avg_similarity_score": round(float(np.mean(similarity_scores)), 4),
        "retrieval_recall": None,
        "retrieval_precision": None
    }

    return {
        "query": query,
        "retrieved": retrieved_chunks,
        "answer": answer,
        "metrics": metrics
    }
