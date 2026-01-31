import json
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


# Load OCR JSON
with open("../structured_ocr.json", "r", encoding="utf-8") as f:
    data = json.load(f)


# Convert to text
texts = []

for page in data["pages"]:
    for line in page["lines"]:
        texts.append(line["text"])

full_text = "\n".join(texts)


# Chunk
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

docs = splitter.create_documents([full_text])


# Free embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# FAISS DB
db = FAISS.from_documents(docs, embeddings)

db.save_local("db")

print("Local vector DB built ✅")
