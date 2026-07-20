_QUERY = """Generate a professional LinkedIn post (150-250 words) from this document.
Include: key achievements, technologies used, hashtags, and a strong opening line.
Write in first person."""

def generate_linkedin_post(chain) -> str:
    return chain.invoke(_QUERY)