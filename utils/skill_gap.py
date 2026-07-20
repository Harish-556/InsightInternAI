def analyze_skill_gap(chain, job_description: str) -> str:
    query = f"""
    Based on this internship report/project document, analyze the skill gap
    against this job description:
 
    JOB DESCRIPTION:
    {job_description}
 
    Provide:
    1. Skills you HAVE (from the document) that match the job
    2. Skills you are MISSING that the job requires
    3. Skills you have that are BONUS (not required but valuable)
    4. A match percentage score out of 100
    5. Top 3 recommendations to close the skill gap
 
    Format clearly with sections and bullet points.
    """
    return chain.invoke(query)
 