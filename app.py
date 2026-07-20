import streamlit as st
from rag.pdf_loader import load_pdf
from rag.chunking import split_text
from rag.embeddings import get_embeddings
from rag.vector_store import create_vector_store
from rag.retriever import get_retriever
from rag.chain import get_qa_chain
from utils.summary import generate_summary
from utils.linkedin import generate_linkedin_post
from utils.abstract import generate_abstract
from utils.interview import generate_interview_questions
from utils.helper import save_uploaded_file, cleanup_temp_file

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="InsightIntern AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 InsightIntern AI")
st.caption("RAG-Powered Internship Report Assistant — Ask questions about your PDF instantly!")

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("📂 Upload Your Document")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file:
        st.success(f"✅ **{uploaded_file.name}** uploaded!")
        st.info("Scroll right → to explore all features via the tabs.")

    st.divider()
    st.markdown("### 💡 Example Questions")
    st.markdown(
        "- Explain the project objective.\n"
        "- What technologies were used?\n"
        "- Summarize Chapter 3.\n"
        "- What are the project outcomes?"
    )

# ─── Process PDF ─────────────────────────────────────────────────────────────
if uploaded_file:
    # Only re-process when a new file is uploaded
    if (
        "chain" not in st.session_state
        or st.session_state.get("file_name") != uploaded_file.name
    ):
        with st.spinner("⚙️ Processing document… This may take a moment."):
            file_path = save_uploaded_file(uploaded_file)
            text      = load_pdf(file_path)

            if not text.strip():
                st.error("❌ Could not extract text from the PDF. Please try a text-based PDF.")
                st.stop()

            chunks       = split_text(text)
            embeddings   = get_embeddings()
            vector_store = create_vector_store(chunks, embeddings)
            retriever    = get_retriever(vector_store)
            chain        = get_qa_chain(retriever)

            st.session_state.chain     = chain
            st.session_state.file_name = uploaded_file.name
            st.session_state.messages  = []   # reset chat on new upload
            cleanup_temp_file(file_path)

        st.success("✅ Document processed successfully! Use the tabs below.")

    # ─── Tabs ─────────────────────────────────────────────────────────────────
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🤖 AI Chat",
        "📑 AI Summary",
        "💼 LinkedIn Post",
        "📚 Interview Questions",
        "📝 Project Abstract",
    ])

    # ── Tab 1 : AI Chat ───────────────────────────────────────────────────────
    with tab1:
        st.header("🤖 AI Chat")
        st.write("Ask anything about your uploaded document:")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Type your question here…"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Thinking…"):
                   # result   = st.session_state.chain.invoke({"query": prompt})
                    # response = result["answer"]
                    response = st.session_state.chain.invoke(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

    # ── Tab 2 : AI Summary ────────────────────────────────────────────────────
    with tab2:
        st.header("📑 AI Summary")
        summary_type = st.selectbox(
            "Choose summary type:",
            ["Executive Summary", "Project Summary", "Internship Summary"],
        )
        if st.button("Generate Summary", key="summary_btn"):
            with st.spinner("Generating summary…"):
                summary = generate_summary(st.session_state.chain, summary_type)
            st.subheader(f"📄 {summary_type}")
            st.write(summary)
            st.download_button("⬇️ Download Summary", summary, file_name="summary.txt")

    # ── Tab 3 : LinkedIn Post ─────────────────────────────────────────────────
    with tab3:
        st.header("💼 LinkedIn Post Generator")
        if st.button("Generate LinkedIn Post", key="linkedin_btn"):
            with st.spinner("Crafting your LinkedIn post…"):
                post = generate_linkedin_post(st.session_state.chain)
            st.subheader("✍️ Your LinkedIn Post")
            st.text_area("Copy and paste this post:", value=post, height=300)
            st.download_button("⬇️ Download Post", post, file_name="linkedin_post.txt")

    # ── Tab 4 : Interview Questions ───────────────────────────────────────────
    with tab4:
        st.header("📚 Interview Question Generator")
        if st.button("Generate Interview Questions", key="interview_btn"):
            with st.spinner("Generating interview questions…"):
                questions = generate_interview_questions(st.session_state.chain)
            st.subheader("🎯 Interview Questions")
            st.write(questions)
            st.download_button("⬇️ Download Questions", questions, file_name="interview_questions.txt")

    # ── Tab 5 : Project Abstract ──────────────────────────────────────────────
    with tab5:
        st.header("📝 Project Abstract Generator")
        if st.button("Generate Abstract", key="abstract_btn"):
            with st.spinner("Writing project abstract…"):
                abstract = generate_abstract(st.session_state.chain)
            st.subheader("📄 Project Abstract")
            st.write(abstract)
            st.download_button("⬇️ Download Abstract", abstract, file_name="abstract.txt")

else:
    # ── Landing screen ────────────────────────────────────────────────────────
    st.info("👈 Please upload a PDF from the sidebar to get started.")
    st.markdown("""
    ## 🚀 What InsightIntern AI can do for you

    | Feature | Description |
    |---|---|
    | 🤖 **AI Chat** | Ask any question about your document |
    | 📑 **AI Summary** | Get executive / project / internship summaries |
    | 💼 **LinkedIn Post** | Auto-generate a professional post |
    | 📚 **Interview Questions** | Prepare for interviews from your own project |
    | 📝 **Project Abstract** | Create a concise academic abstract |
    """)
