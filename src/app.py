import streamlit as st
from transformers import pipeline


st.sidebar.markdown(
    "This app allows users to input text of their choice using the tools provided, and ask questions with the answer "
    "being extracted from the text.")
st.sidebar.markdown(
    "_When running the app the first time, it may take some time to initialise due to the requirements needing to be "
    "downloaded._")
tool = st.sidebar.selectbox("Tool", ["Sentiment Analysis", "Text Generation"])


@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def generatesentiment():
    nlp = pipeline('sentiment-analysis')
    return nlp


@st.cache(suppress_st_warning=True)
def generatetext(starting_text):
    gpt2 = pipeline('text-generation')
    return gpt2


def sentiment():
    st.write("# Sentiment Analysis")
    user_input = st.text_input("Enter Text")

    if st.button('Get Sentiment'):
        nlp = generatesentiment()
        answer = nlp(user_input)
        st.header("Answer")
        st.write(answer)


def text():
    st.write("# GPT-2 Text Generation")
    user_input = st.text_input("Enter Text",value="I love Machine Learning but")

    if st.button('Get Text Answer'):
        gpt2 = generatetext()
        answer = gpt2(user_input, max_length=50, num_return_sequences=2)
        st.header("Answer")
        st.write(answer)

if tool == "Sentiment Analysis":
    sentiment()

if tool == "Text Generation":
    text()
