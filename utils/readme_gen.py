_QUERY = """Generate a professional GitHub README.md file based on this project document.
 
Include these sections in markdown format:
# Project Title
## Overview
## Features
## Tech Stack (as a table)
## Installation
## How It Works
## Results
## Future Scope
## Author
 
Use proper markdown formatting with badges, tables, and code blocks."""
 
def generate_readme(chain) -> str:
    return chain.invoke(_QUERY)
 