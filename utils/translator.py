LANGUAGES = [
    "Hindi", "Tamil", "Telugu", "Kannada", "Malayalam",
    "French", "Spanish", "German", "Japanese", "Arabic",
    "Chinese", "Portuguese", "Russian", "Korean"
]

def translate_text(chain, text: str, language: str) -> str:
    query = f"""Translate the following text to {language}.
Keep the formatting, bullet points, and structure exactly the same.
Only translate the words, not the structure.

TEXT TO TRANSLATE:
{text}"""
    return chain.invoke(query)