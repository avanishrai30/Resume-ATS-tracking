#Welcome to my git hub 
#Connect me, if this is helpful for you
#:)
import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
Imagine you are a highly skilled Application Tracking System (ATS) with expertise in the tech field, 
including software engineering, data science, data analysis, and big data engineering. 
Your task is to assess resumes based on the provided job description. 
The job market is extremely competitive, and you must provide the best assistance for improving resumes. 
Assign a percentage match based on the job description and accurately identify missing keywords.
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.markdown("---")
st.subheader("Improve Your Resume ATS")

# Text areas for job description and resume upload
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

# Submit button
if st.button("Submit"):
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_repsonse(input_prompt)
        st.subheader("Response:")
        st.write(response)

# Social media links
st.markdown("---")
st.write("Follow me on social media for more help:")
st.write("[Twitter](https://twitter.com/Avanishrai0)")
st.write("[LinkedIn](https://www.linkedin.com/in/avanishr/)")
st.write("[GitHub](https://github.com/avanishrai30)")
