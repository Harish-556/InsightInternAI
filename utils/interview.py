_QUERY = """Generate 10 technical interview questions from this document.
Number each question and add a short answer hint below it.
Cover: project goals, technologies, methodology, challenges, and outcomes."""

def generate_interview_questions(chain) -> str:
    return chain.invoke(_QUERY)