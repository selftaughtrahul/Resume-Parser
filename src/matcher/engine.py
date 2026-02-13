"""
Matching Engine using Scikit-Learn
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.utils.text_cleaner import clean_text
import pandas as pd
from typing import List, Dict

class JobMatcher:
    """Matches resumes against JD"""

    @staticmethod
    def calculate_match_score(resume_text: str, jd_text: str) -> float:
        """Calculate cosine similarity score (0-100)"""
        # Clean
        res_clean = clean_text(resume_text)
        jd_clean = clean_text(jd_text)
        
        if not res_clean or not jd_clean:
            return 0.0
            
        # Vectorize
        vectorizer = CountVectorizer().fit_transform([res_clean, jd_clean])
        vectors = vectorizer.toarray()
        
        # Calculate Similarity
        # vectors[0] is resume, vectors[1] is JD
        score = cosine_similarity(vectors)[0][1]
        
        return round(score * 100, 2)

    @staticmethod
    def match_batch(resumes_data: List[Dict], jd_text: str) -> pd.DataFrame:
        """
        Match a list of parsed resumes against a JD
        resumes_data: List of dicts from ResumeParser.parse()
        """
        results = []
        
        for res in resumes_data:
            score = JobMatcher.calculate_match_score(res['text'], jd_text)
            
            results.append({
                "Name": res.get('name'),
                "Email": res.get('email'),
                "Phone": res.get('phone'),
                "Skills": ", ".join(res.get('skills', [])),
                "Match Score": score
            })
            
        # Create DataFrame and sort
        df = pd.DataFrame(results)
        if not df.empty:
            df = df.sort_values(by="Match Score", ascending=False)
            
        return df