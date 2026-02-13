"""
Configuration settings
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RESUMES_DIR = DATA_DIR / "resumes"
JD_DIR = DATA_DIR / "job_descriptions"

# Ensure directories exist
RESUMES_DIR.mkdir(parents=True, exist_ok=True)
JD_DIR.mkdir(parents=True, exist_ok=True)

# Skills to look for (Default List)
DEFAULT_SKILLS = [
    "Python", "Java", "SQL", "Machine Learning", "Data Science",
    "NLP", "Spacy", "NLTK", "Pandas", "NumPy", "TensorFlow",
    "AWS", "Docker", "Git", "Flask", "Django", "React",
    "MS Office", "Excel", "Data Entry", "Typing", "Communication",
    "Customer Service", "Accounting", "Statistics", "MIS", "HIPAA",
    "CRM", "ERP", "Tally", "Billing", "Market Research"
]