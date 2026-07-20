from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from rag.llm import get_llm
from rag.prompt import get_qa_prompt


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_qa_chain(retriever):
    llm    = get_llm()
    prompt = get_qa_prompt()

    chain = (
        {"context": retriever | format_docs, "input": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain