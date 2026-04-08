from src.scraper import scrape_wikipedia
from src.chunking import chunk_text
from src.embeddings import load_embedding_model, create_embeddings
from src.retriever import build_faiss_index
from src.generator import load_llm
from src.pipeline import run_rag_pipeline

# Step 1: Scrape
url = "https://en.wikipedia.org/wiki/World_Health_Organization"
text = scrape_wikipedia(url)

# Step 2: Chunk
chunks = chunk_text(text)

# Step 3: Embeddings
embed_model = load_embedding_model()
embeddings = create_embeddings(embed_model, chunks)

# Step 4: FAISS
index = build_faiss_index(embeddings)

# Step 5: LLM
tokenizer, model_llm = load_llm()

# Step 6: Run Query
query = "What is WHO?"
result = run_rag_pipeline(query, embed_model, index, chunks, tokenizer, model_llm)

print("QUERY:", result["query"])
print("\nANSWER:", result["answer"])
print("\nMETRICS:", result["metrics"])
