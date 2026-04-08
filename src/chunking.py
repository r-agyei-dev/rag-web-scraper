import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def chunk_text(text, chunk_size=3, overlap=1):
    sentences = sent_tokenize(text)

    step = chunk_size - overlap
    chunks = []

    for i in range(0, len(sentences), step):
        chunk = sentences[i:i+chunk_size]
        if chunk:
            chunks.append(" ".join(chunk))

    return chunks
