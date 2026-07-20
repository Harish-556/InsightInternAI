# 📄 InsightIntern AI — RAG-Powered Internship Report Assistant

> Ask questions about your internship reports, project documents, and PDFs using AI.

---

## 🗂 Folder Structure

```
InsightInternAI/
│
├── app.py                  ← Main Streamlit application (entry point)
├── requirements.txt        ← All Python dependencies
├── .env                    ← Your Groq API key (never commit this!)
│
├── rag/                    ← RAG pipeline modules
│     ├── __init__.py
│     ├── pdf_loader.py     ← Extract text from PDF using PyMuPDF
│     ├── chunking.py       ← Split text into overlapping chunks
│     ├── embeddings.py     ← HuggingFace sentence-transformer embeddings
│     ├── vector_store.py   ← Create FAISS in-memory vector store
│     ├── retriever.py      ← Similarity-search retriever
│     ├── llm.py            ← Groq LLM (Llama 3) integration
│     ├── prompt.py         ← RAG prompt template
│     └── chain.py          ← Full RetrievalQA chain
│
├── utils/                  ← Feature utility modules
│     ├── __init__.py
│     ├── summary.py        ← Summary generator
│     ├── linkedin.py       ← LinkedIn post generator
│     ├── abstract.py       ← Project abstract generator
│     ├── interview.py      ← Interview question generator
│     └── helper.py         ← File save/cleanup helpers
│
├── uploaded_docs/          ← (optional) store sample PDFs here
└── .streamlit/
      └── secrets.toml      ← Used for Streamlit Cloud deployment
```

---

## ⚙️ Setup & Execution — Step by Step

### Step 1 — Get a FREE Groq API Key

1. Go to https://console.groq.com
2. Sign up (free account)
3. Navigate to **API Keys → Create API Key**
4. Copy the key — you will use it in Step 4

---

### Step 2 — Clone the repository

```bash
git clone https://github.com/yourusername/InsightInternAI.git
cd InsightInternAI
```

---

### Step 3 — Create & activate a virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python -m venv venv
source venv/bin/activate
```

---

### Step 4 — Add your API key

Open `.env` and replace the placeholder:

```
GROQ_API_KEY=your_actual_key_here
```

---

### Step 5 — Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ First install takes 3–5 minutes (downloads the embedding model ~90 MB).

---

### Step 6 — Run the application

```bash
streamlit run app.py
```

The browser opens automatically at **http://localhost:8501**

---

### Step 7 — Use the app

1. **Upload** your internship report PDF from the left sidebar
2. Wait ~10 seconds for processing
3. Switch between tabs:
   - **🤖 AI Chat** — ask free-form questions
   - **📑 AI Summary** — get executive/project/internship summaries
   - **💼 LinkedIn Post** — auto-generate a post
   - **📚 Interview Questions** — prepare for HR/technical rounds
   - **📝 Project Abstract** — get a report-ready abstract

---

## 🌐 Deploy to Streamlit Community Cloud (Free)

1. Push the repo to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub repo
4. Under **Settings → Secrets**, paste:
   ```
   GROQ_API_KEY = "your_key_here"
   ```
5. Click **Deploy** — done!

---

## 🧩 How RAG Works (Simple Explanation)

```
Your PDF
   │
   ▼
Extract Text (PyMuPDF)
   │
   ▼
Split into Chunks (LangChain)
   │
   ▼
Convert to Vectors (HuggingFace)
   │
   ▼
Store in FAISS (Vector DB)
   │
   ▼
Your Question → Find Similar Chunks
   │
   ▼
Send [Context + Question] to Groq LLM
   │
   ▼
Get Context-Aware Answer ✅
```

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| LLM | Groq (Llama 3 8B) |
| RAG Framework | LangChain |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector DB | FAISS |
| PDF Reader | PyMuPDF |
| Env Management | python-dotenv |

---

## 📄 License

MIT License — free to use and extend.
