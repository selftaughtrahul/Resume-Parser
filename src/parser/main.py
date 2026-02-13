"""
Main Parser class
"""
from .file_reader import FileReader
from .extractor import Extractor
from src.utils.config import DEFAULT_SKILLS

class ResumeParser:
    def __init__(self, skills_list=None):
        self.skills_list = skills_list if skills_list else DEFAULT_SKILLS

    def parse(self, file_path: str) -> dict:
        """Parse a resume file and return dict"""
        # 1. Read Text
        text = FileReader.read_file(file_path)
       
        if not text:
            return None
        
        # 2. Extract Info
        
        data = {
            "name": Extractor.extract_name(text),
            "email": Extractor.extract_email(text),
            "phone": Extractor.extract_phone(text),
            "skills": Extractor.extract_skills(text, self.skills_list),
            "text": text # Keep raw text for matching later
        }
        return data
       