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
    answer = gpt2(starting_text, max_length=50, num_return_sequences=2)
    return answer


@st.cache(suppress_st_warning=True)
def generatesummary(text):
    summarizer = pipeline("summarization")
    answer = (summarizer(text, max_length=100, min_length=30, do_sample=False))
    return answer


def website_qna():
    st.write("# Website QnA")
    user_input = st.text_input("Website Link:", value="https://en.wikipedia.org/wiki/Machine_learning")
    question = st.text_input("Question:", value="What is Machine Learning?")

    if st.button("Get Answer"):
        scraped_data = requests.get(user_input)
        article = scraped_data.text

        parsed_article = BeautifulSoup(article, 'lxml')

        paragraphs = parsed_article.find_all('p')

        article_text = ""
        for p in paragraphs:
            article_text += p.text

        answer = generateAnswer(question, article_text)
        st.header("Answer")
        st.write(answer)


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
