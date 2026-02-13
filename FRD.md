# Functional Requirement Document (FRD)
**Project Name:** Resume Parser & Job Matcher
**Date:** 2026-02-12
**Author:** AI Assistant

## 1. Introduction
This document outlines the specific functional requirements for the Resume Parser & Job Matcher system.

## 2. User Roles
-   **System:** The automated script/application.
-   **User:** The person providing resumes and job descriptions.

## 3. Functional Requirements

### 3.1 Input Handling
-   **FR-01:** The system shall accept resumes in PDF (.pdf) format.
-   **FR-02:** The system shall accept resumes in Word (.docx) format.
-   **FR-03:** The system shall accept a Job Description (JD) as a text file or text input.
-   **FR-04:** The system shall support batch processing of multiple resumes from a directory.

### 3.2 Resume Parsing (Extraction)
-   **FR-05:** The system shall extract the candidate's **Name** (using NER/Rules).
-   **FR-06:** The system shall extract **Contact Information** (Email, Phone Number) using Regex.
-   **FR-07:** The system shall extract **Skills** using a predefined skill database or NER.
-   **FR-08:** The system shall extract **Education** details (Degree, University) using keyword matching/NER.
-   **FR-09:** (Optional) The system shall extract **Work Experience** (Company names, Job Titles).

### 3.3 Text Processing
-   **FR-10:** The system shall clean extracted text (remove special characters, extra spaces, stop words).
-   **FR-11:** The system shall tokenize and lemmatize text for better matching.

### 3.4 Job Matching & Ranking
-   **FR-12:** The system shall convert resume text and JD text into vector representations (e.g., TF-IDF, CountVectorizer).
-   **FR-13:** The system shall calculate the **Cosine Similarity** between the JD vector and each resume vector.
-   **FR-14:** The system shall rank resumes based on the similarity score (highest to lowest).
-   **FR-15:** The system shall identify missing skills in the resume compared to the JD.

### 3.5 Output Generation
-   **FR-16:** The system shall generate a report (CSV/Excel) containing:
    -   Candidate Name
    -   Email
    -   Phone
    -   Skills Found
    -   Matching Score (%)
    -   Missing Skills (optional)

## 4. UI/UX (Optional for Phase 1)
-   **FR-17:** A simple CLI to specify input directories.
-   **FR-18:** A basic Streamlit app to upload files and visualize results.
