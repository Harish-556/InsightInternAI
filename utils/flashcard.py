_QUERY = """Generate 10 multiple choice questions (MCQs) from this document.

For each question use this exact format:
Q1. [Question]
A) [Option]
B) [Option]
C) [Option]
D) [Option]
Answer: [Correct letter]
Explanation: [One line explanation]

Cover key concepts, technologies, and findings from the document."""

def generate_flashcards(chain) -> str:
    return chain.invoke(_QUERY)