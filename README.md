# 📄 DocIntel OCR + RAG System

An intelligent document processing system that extracts text from documents using OCR and enables semantic search using RAG (Retrieval-Augmented Generation).

---

## 🚀 Features

* 📷 OCR processing for scanned documents
* 📑 Layout-aware text extraction
* 📊 Table detection and structured output
* 🔍 RAG-based document querying
* ☁️ Cloud storage integration (Azure Blob)
* 🧠 OpenAI-powered embeddings and responses

---

## 🛠️ Tech Stack

* **Backend:** Python / Node.js
* **OCR:** Azure Form Recognizer
* **LLM:** OpenAI API
* **Database:** PostgreSQL
* **Storage:** Azure Blob Storage
* **Framework:** FastAPI / Express (as applicable)

---

## 📁 Project Structure

```
docintel-ocr/
│
├── rag/              # RAG pipeline
├── processed_docs/   # OCR outputs
├── scripts/          # Helper scripts
├── .env.example      # Environment template
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd docintel-ocr
```

---

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or (for Node.js):

```bash
npm install
```

---

### 4️⃣ Environment Setup

Create `.env` file:

```env
OPENAI_API_KEY=your_key_here
AZURE_FORM_KEY=your_key_here
AZURE_FORM_ENDPOINT=your_endpoint_here
DB_URL=your_database_url
```

⚠️ Never commit `.env` files.

---

### 5️⃣ Run the Project

```bash
python main.py
```

or

```bash
npm start
```

---

## 🔍 Usage

1. Upload documents (PDF/Image)
2. System performs OCR + layout analysis
3. Data stored in DB and Blob storage
4. Query documents using RAG
5. Get AI-powered responses

---

## 📌 Output Format (JSON)

```json
{
  "text": "Extracted content",
  "bounding_boxes": [],
  "page_number": 1,
  "tables": []
}
```

---

## 🔐 Security Best Practices

* Do not commit API keys
* Rotate keys regularly
* Use `.env.example` for reference
* Enable GitHub secret scanning

---

## 📈 Future Improvements

* UI dashboard
* Multi-language OCR
* Advanced vector search
* User authentication
* Batch processing

---

## 👨‍💻 Author

**Reyansh Sidha**
ECE, PEC Chandigarh
Web Developer (MERN + Backend)

---

## 📄 License

This project is licensed under the MIT License.

---

Feel free to contribute, raise issues, or suggest imp
