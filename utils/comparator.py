def compare_documents(chain1, chain2) -> str:
    query = """Summarize this document's: main topic, technologies used,
    key outcomes, methodology, and conclusions in a structured format."""
 
    summary1 = chain1.invoke(query)
    summary2 = chain2.invoke(query)
 
    return summary1, summary2
 