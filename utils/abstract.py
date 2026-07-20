_QUERY = """Write a formal project abstract (150-250 words) as one paragraph covering:
background, objectives, methodology, results, and conclusions."""

def generate_abstract(chain) -> str:
    return chain.invoke(_QUERY)