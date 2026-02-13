# Business Requirement Document (BRD)
**Project Name:** Resume Parser & Job Matcher
**Date:** 2026-02-12
**Author:** AI Assistant

## 1. Executive Summary
The Resume Parser & Job Matcher is an automated tool designed to improve the initial screening process of recruitment. By allowing recruiters to upload multiple resumes and match them against a specific Job Description (JD), the tool will output a ranked list of candidates based on relevancy, saving significant time and effort.

## 2. Business Objectives
-   **Reduce Screening Time:** Automate the manual review of resumes.
-   **Improve Accuracy:** Reduce human error and bias in candidate selection.
-   **standardization:** Ensure consistent criteria are applied to all candidates.
-   **Scalability:** Process large volumes of resumes quickly.

## 3. Target Audience
-   **Recruiters/HR Managers:** Who need to filter through hundreds of applications.
-   **Hiring Managers:** Who want to see the most relevant candidates first.

## 4. Functional Scope
See FRD for detailed functional requirements.

## 5. Non-Functional Requirements
-   **Performance:** Should process a resume within seconds.
-   **Reliability:** Should handle standard resume formats (PDF, DOCX) without crashing.
-   **Security:** Should process data locally to ensure data privacy (unless deployed to cloud).
-   **Usability:** Simple command-line or web interface for easy interaction.

## 6. Success Metrics
-   **Parsing Accuracy:** > 85% accuracy in extracting Name, Email, and Skills.
-   **Matching Relevance:** Top 5 ranked candidates should be deemed relevant by a human reviewer.
-   **Processing Speed:** Batch processing of 50 resumes under 2 minutes.
