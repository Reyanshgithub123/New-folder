from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama


# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Load DB
db = FAISS.load_local(
    "db",
    embeddings,
    allow_dangerous_deserialization=True
)


# Llama Model
llm = Ollama(model="llama3.1:8b")


def ask(question):

    docs = db.similarity_search(question, k=5)

    if not docs:
        return "No evidence found"

    context = "\n\n".join(
        [d.page_content for d in docs]
    )

    prompt = f"""
You are a clinical document analyst.

Use ONLY this context.

Context:
{context}

Question:
{question}

Rules:
- Answer only from context
- If not found say: No evidence found
"""

    return llm.invoke(prompt)


# CLI
while True:

    q = input("Ask> ")

    if q.lower() == "exit":
        break

    print("\nAnswer:\n", ask(q), "\n")
