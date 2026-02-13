"""
Module to read text from different file formats
"""
import docx
from pdfminer.high_level import extract_text
import os

class FileReader:
    """Reads content from PDF, DOCX, and TXT files"""
    
    @staticmethod
    def read_pdf(file_path: str) -> str:
        """Extract text from PDF"""
        try:
            return extract_text(file_path)
        except Exception as e:
            print(f"Error reading PDF {file_path}: {e}")
            return ""

    @staticmethod
    def read_docx(file_path: str) -> str:
        """Extract text from DOCX"""
        try:
            doc = docx.Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])
        except Exception as e:
            print(f"Error reading DOCX {file_path}: {e}")
            return ""

    @staticmethod
    def read_txt(file_path: str) -> str:
        """Extract text from TXT"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading TXT {file_path}: {e}")
            return ""

    @staticmethod
    def read_file(file_path: str) -> str:
        """Universal read function dispatcher"""
        if file_path.endswith('.pdf'):
            return FileReader.read_pdf(file_path)
        elif file_path.endswith('.docx'):
            return FileReader.read_docx(file_path)
        elif file_path.endswith('.txt'):
            return FileReader.read_txt(file_path)
        else:
            print(f"Unsupported file format: {file_path}")
            return ""