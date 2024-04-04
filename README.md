# Resume-ATS-tracking
This repository contains a Streamlit application for an Applicant Tracking System (ATS) that improves resumes. It uses the Google Generative AI (Gemini) API to evaluate resumes based on job descriptions. The application extracts text from PDF resumes using PyPDF2 and analyzes it against the job description provided by the user.

**Project Structure:**
![Screenshot (6)](https://github.com/avanishrai30/Resume-ATS-tracking/assets/82101000/a32a96c9-265d-4624-8362-4f1922fb3efd)

![Screenshot (7)](https://github.com/avanishrai30/Resume-ATS-tracking/assets/82101000/9c9e7d49-bccf-4e9c-b3ac-03497be579c4)

app.py: Main Streamlit application file.
requirements.txt: List of Python dependencies.
README.md: Project description, setup instructions, and usage guidelines.
Setup Instructions:

**Clone the repository:**
git clone https://github.com/<username>/resume-ATS-tracking.git
Navigate to the project directory: cd resume-ATS-tracking
Install dependencies: pip install -r requirements.txt
Set up the environment variables:
Create a .env file in the project directory.
Add your Google API key to the .env file: GOOGLE_API_KEY=<your_api_key>
Run the application: streamlit run app.py

Usage:
-Paste the job description into the text area.
-Upload the resume in PDF format.
-Click the "Submit" button to see the evaluation results.
***About LLMs (Large Language Models):**
Large Language Models, such as the Gemini model used in this project, are AI models that have been trained on vast amounts of text data to understand and generate human-like text. They are capable of a wide range of natural language processing tasks, including text generation, summarization, and language understanding. In this project, the Gemini model is used to analyze resumes and job descriptions, providing insights and suggestions for improving resumes to match job requirements better.
