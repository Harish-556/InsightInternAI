_QUERY = """Generate a professional resume/CV based on this internship report.

Format it exactly like this:

NAME: [Extract or use "Your Name"]
EMAIL: yourname@email.com
LINKEDIN: linkedin.com/in/yourname

PROFESSIONAL SUMMARY:
[2-3 lines based on the internship/project]

INTERNSHIP EXPERIENCE:
Company: [Extract from document]
Role: [Extract or infer]
Duration: [Extract if mentioned]
- Key responsibility 1
- Key responsibility 2
- Key achievement

PROJECTS:
Project Name: [From document]
- Description
- Technologies used
- Outcome

TECHNICAL SKILLS:
- Languages: [Extract from document]
- Frameworks: [Extract from document]
- Tools: [Extract from document]

EDUCATION:
[Leave placeholder]"""

def generate_resume(chain) -> str:
    return chain.invoke(_QUERY)