SUMMARY_PROMPTS = {
    "Executive Summary": "Generate a concise executive summary covering objectives, methodology, results, and conclusions.",
    "Project Summary":   "Summarize the project: goals, technologies, implementation, challenges, and outcomes.",
    "Internship Summary":"Summarize the internship: role, tasks completed, tools used, and key learnings.",
}

def generate_summary(chain, summary_type="Executive Summary") -> str:
    query = SUMMARY_PROMPTS.get(summary_type, SUMMARY_PROMPTS["Executive Summary"])
    return chain.invoke(query)