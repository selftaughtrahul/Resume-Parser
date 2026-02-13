# Statement of Work (SOW)
**Project Name:** Resume Parser & Job Matcher
**Date:** 2026-02-12
**Author:** AI Assistant

## 1. Project Background
The goal of this project is to automate the extraction of key information from resumes (CVs) and match them against job descriptions to streamline the recruitment process. Manual screening of resumes is time-consuming and prone to bias. This tool aims to leverage Natural Language Processing (NLP) techniques to improve efficiency and accuracy in candidate shortlisting.

## 2. Scope of Work
The scope includes the development of a Python-based application that can:
- **Parse Resumes:** Extract candidate details such as Name, Email, Phone Number, Skills, Education, and Work Experience from PDF and DOCX files.
- **Parse Job Descriptions:** Process job description text to identify required skills and qualifications.
- **Match & Rank:** Calculate a compatibility score between resumes and job descriptions using Cosine Similarity and other metrics.
- **Interface:** (Optional/Future) A simple CLI or Web Interface (Streamlit/Flask) to upload files and view results.

## 3. Deliverables
1.  **Source Code:** Complete Python source code for the parser and matcher.
2.  **Documentation:** SOW, BRD, FRD, Implementation Roadmap, and Technical Guides.
3.  **Unit Tests:** Test cases for parser accuracy and matching logic.
4.  **User Guide:** Instructions on how to set up and run the application.

## 4. Technology Stack
-   **Language:** Python 3.8+
-   **NLP Libraries:** Spacy, NLTK, Scikit-learn
-   **Text Extraction:** PDFMiner, PyPDF2, python-docx
-   **Data Handling:** Pandas, NumPy

## 5. Timeline (Estimated)
-   **Phase 1: Planning & Setup** (Day 1) - Complete
-   **Phase 2: Resume Parser Development** (Day 2-3)
-   **Phase 3: Job Matcher Development** (Day 4)
-   **Phase 4: Testing & Refinement** (Day 5)
-   **Phase 5: Documentation & Handover** (Day 5)

## 6. Assumptions & Constraints
-   Resumes are in standard English.
-   Resumes are in PDF or DOCX format.
-   The accuracy of extraction depends on the formatting of the input documents.
