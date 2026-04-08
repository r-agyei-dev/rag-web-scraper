from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_llm():
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
    return tokenizer, model

def build_prompt(query, context_chunks):
    context = "\n".join(context_chunks)

    return f"""Answer the question ONLY using the context below. 
If the answer is not in the context, say "I dont know".

Context:
{context}

Question:
{query}

Answer:"""

def generate_answer(query, context_chunks, tokenizer, model):
    prompt = build_prompt(query, context_chunks)
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(**inputs, max_new_tokens=150)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer.strip()
