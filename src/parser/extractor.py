"""
Module to extract entities (Name, Email, Skills) from text
"""
import spacy
import re
from typing import List

# Load Spacy Model
try:
    nlp = spacy.load('en_core_web_sm')
except:
    nlp = None

class Extractor:
    """Extracts structured data from raw resume text"""
    
    @staticmethod
    def extract_name(text: str) -> str:
        """Extract person name from the first few lines or using Spacy NER"""
        if not text:
            return "Unknown"
            
        # Strategy 1: Check the first 5 non-empty lines
        # Names are usually at the top and 2nd or 3rd line.
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        for line in lines[:5]:
            # If a line is short (2-4 words) and contains alphabets only, it's likely a name
            if 2 <= len(line.split()) <= 4 and re.match(r'^[a-zA-Z\s]+$', line):
                # Avoid common headers
                if line.lower() not in ['resume', 'curriculum vitae', 'cv', 'summary', 'contact', 'profile']:
                    return line

        # Strategy 2: Fallback to Spacy NER
        if nlp:
            doc = nlp(text)
            for ent in doc.ents:
                if ent.label_ == "PERSON":
                    # Simple heuristic: names usually don't have digits or special chars
                    if not any(char.isdigit() for char in ent.text) and len(ent.text.split()) >= 2:
                        return ent.text
        
        return "Unknown"

    @staticmethod
    def extract_email(text: str) -> str:
        """Extract email using Regex"""
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        match = re.search(pattern, text)
        return match.group(0) if match else "No Email"

    @staticmethod
    def extract_phone(text: str) -> str:
        """Extract phone number using Regex (handles international formats)"""
        # Look for patterns like +91 98765 43210, 09876543210, 98765-43210, etc.
        # This regex looks for 10-12 digits with optional separators
        pattern = r'(?:\+?\d{1,4}[\s\-])?\(?\d{2,5}\)?[\s\-]?\d{3,5}[\s\-]?\d{4,6}'
        
        # Clean text: keep only characters often found in phone numbers plus space
        clean_text = re.sub(r'[^\d\s\+\-\(\)]', ' ', text)
        
        match = re.search(pattern, clean_text)
        if match:
            phone = match.group(0).strip()
            # Basic validation: must have at least 10 digits
            if sum(c.isdigit() for c in phone) >= 10:
                return phone
        return "No Phone"

    @staticmethod
    def extract_skills(text: str, skills_list: List[str]) -> List[str]:
        """Extract skills present in text based on a list"""
        found_skills = []
        text_lower = text.lower()
        for skill in skills_list:
            # Use regex word boundary to avoid partial matches
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            if re.search(pattern, text_lower):
                found_skills.append(skill)
        return list(set(found_skills))