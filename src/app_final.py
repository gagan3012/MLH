import googlesearch
import streamlit as st
from transformers import pipeline
import requests
from bs4 import BeautifulSoup

st.set_page_config(
    page_title="Machine Learning for Hackathons",
    layout='wide'
)



st.sidebar.header("""
© ML Workshop By DSC UBC
""")
st.sidebar.markdown(
    "This app allows users to input text of their choice using the tools provided, and ask questions with the answer "
    "being extracted from the text.")
st.sidebar.markdown(
    "_When running the app the first time, it may take some time to initialise due to the requirements needing to be "
    "downloaded._")
tool = st.sidebar.selectbox("Tool", ["Mood Analyzer", "Help Me Write My Essay", "Help Me Summarize A Passage", "Wikipedia Answers"])


@st.cache(suppress_st_warning=True)
def generate_answer(question, context):
    nlp = pipeline("question-answering")
    answer = nlp(question=question, context=context)
    return answer


@st.cache(suppress_st_warning=True)
