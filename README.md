# 🔍 RAG Web Scraper System

A modular **Retrieval-Augmented Generation (RAG)** system that combines **web scraping, semantic search, and large language models (LLMs)** to answer questions from real-world data.

---

## 🚀 Overview

This project demonstrates an end-to-end RAG pipeline:

```
URL → Scraper → Text → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer
```

It allows users to:

* Scrape live web data (e.g., Wikipedia)
* Convert text into embeddings
* Retrieve the most relevant information using vector search
* Generate accurate answers using an LLM
* Evaluate system performance using key metrics

---

## 🧠 Key Features

* 🌐 **Web Scraping**
  Extracts real-time data from web pages using `requests` and `BeautifulSoup`.

* ✂️ **Text Chunking**
  Splits large documents into manageable chunks for better retrieval.

* 🔢 **Embeddings**
  Uses `sentence-transformers` to convert text into dense vector representations.

* ⚡ **FAISS Vector Search**
  Efficient similarity search to retrieve top-k relevant chunks.

* 🤖 **LLM Generation**
  Uses `FLAN-T5` to generate answers based only on retrieved context.

* 📊 **Evaluation Metrics**

  * Latency / Response Time
  * Number of retrieved chunks
  * Average similarity score
  * (Extensible: recall, precision, accuracy)

---

## 🏗️ Project Structure

```
rag-web-scraper/
│
├── src/
│   ├── scraper.py        # Web scraping logic
│   ├── chunking.py       # Text chunking
│   ├── embeddings.py     # Embedding model
│   ├── retriever.py      # FAISS index + retrieval
│   ├── generator.py      # Prompt + LLM generation
│   └── pipeline.py       # End-to-end RAG pipeline
│
├── main.py               # Entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/rag-web-scraper.git
cd rag-web-scraper

pip install -r requirements.txt
```

---

## ▶️ Usage

Run the full pipeline:

```bash
python main.py
```

Example query inside `main.py`:

```python
query = "What is the World Health Organization?"
```

---

## 📌 Example Output

```
QUERY: What is WHO?

ANSWER:
The World Health Organization is a specialized agency of the United Nations responsible for international public health.

METRICS:
{
  'latency_sec': 0.82,
  'num_chunks_retrieved': 2,
  'avg_similarity_score': 0.87
}
```

---

## 📊 Evaluation Metrics Explained

| Metric                 | Description                                               |
| ---------------------- | --------------------------------------------------------- |
| **Latency**            | Time taken to generate a response                         |
| **Chunks Retrieved**   | Number of context chunks used                             |
| **Similarity Score**   | Relevance of retrieved chunks to query                    |
| **Recall / Precision** | (Optional) Retrieval quality if labeled data is available |

---

## 🔥 Why This Project Matters

This project showcases:

* End-to-end **RAG system design**
* Integration of **retrieval + generation**
* Understanding of **vector databases (FAISS)**
* Ability to **evaluate LLM systems**

---

## 🚀 Future Improvements

* Add **Streamlit UI** for interactive querying
* Support **multi-page web crawling**
* Improve **retrieval evaluation (precision/recall)**
* Integrate **real-time data sources**
* Add **caching for faster responses**

---

## 🧑‍💻 Author

**Ronald Agyei**

---

## 📄 License

This project is open-source and available under the MIT License.
