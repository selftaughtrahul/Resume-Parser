"""
Text cleaning utility
"""
import re

def clean_text(text: str) -> str:
    """Basic text cleaning"""
    if not text: return ""
    
    # Lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove non-alphanumeric (keep spaces)
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    
    # Remove extra spaces
    return " ".join(text.split())