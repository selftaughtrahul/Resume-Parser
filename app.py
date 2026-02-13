"""
Streamlit Application Entry Point
"""
import streamlit as st
import os
import pandas as pd
from src.parser.main import ResumeParser
from src.matcher.engine import JobMatcher

# Page Config
st.set_page_config(page_title="Resume Matcher", page_icon="📄", layout="wide")

def save_uploaded_file(uploaded_file):
    """Helper to save uploaded file locally"""
    try:
        with open(os.path.join("data/resumes", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return os.path.join("data/resumes", uploaded_file.name)
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return None

def main():
    st.title("📄 Resume Parser & Job Matcher")
    st.markdown("Upload resumes and a job description to find the best candidates.")

    # Sidebar: Inputs
    with st.sidebar:
        st.header("1. Job Description")
        jd_text = st.text_area("Paste JD here:", height=300)
        
        st.header("2. Upload Resumes")
        uploaded_files = st.file_uploader(
            "Upload PDF/DOCX", 
            type=['pdf', 'docx', 'txt'], 
            accept_multiple_files=True
        )

    # Main Area: Results
    if st.button("Analyze Candidates"):
        if not jd_text:
            st.warning("Please paste a Job Description.")
            return
            
        if not uploaded_files:
            st.warning("Please upload at least one resume.")
            return
            
        # Processing
        with st.spinner("Parsing and Matching..."):
            parser = ResumeParser()
            parsed_resumes = []
            
            # 1. Parse each resume
            for uploaded_file in uploaded_files:
                file_path = save_uploaded_file(uploaded_file)
                if file_path:
                    data = parser.parse(file_path)
                    if data:
                        parsed_resumes.append(data)
                    
                    # Optional: Clean up file after processing
                    # os.remove(file_path)
            # print(parsed_resumes,'parsed_resumes')
            # 2. Match against JD
            if parsed_resumes:
                results_df = JobMatcher.match_batch(parsed_resumes, jd_text)
                
                # 3. Display Results
                st.success("Analysis Complete!")
                st.subheader("🏆 Ranked Candidates")
                st.dataframe(results_df, use_container_width=True)
                
                # 4. Download
                csv = results_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "Download CSV Report",
                    csv,
                    "candidates.csv",
                    "text/csv"
                )
            else:
                st.error("No valid resumes could be parsed.")

if __name__ == "__main__":
    main()