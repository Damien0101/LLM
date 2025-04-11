import streamlit as st
from streamlit_chat import message
from google import genai
from google.genai import types
import json
from langchain.chains import RetrievalQA
from model.model import model



def get_client():
    with open('api_key.json') as f:
        API_KEY = json.load(f)['API_KEY']

    client = genai.Client(api_key=API_KEY)
    return client

def gen_answer():
    response = get_client().models.generate_content(
        model='gemini-2.0-flash',
        contents=query,
        config=types.GenerateContentConfig(
            max_output_tokens=200,
            temperature=0.5
        ))
    return response.text

def translate(text, lang_code):
    return text

qa_chain = model()

st.set_page_config(page_title="Gemini Chatbot", layout="wide", page_icon='⚕️')


LANGUAGES = {
    'English': 'en',
    'Français': 'fr',
    'Español': 'es',
    'Deutsch': 'de',
    'Nederlands': 'nl'
}

selected_language = st.sidebar.selectbox('Select Language', options=list(LANGUAGES.keys()))


st.markdown("<h1 style='text-align: center;'>DiagnosMe 🧬</h1>", unsafe_allow_html=True)
st.divider()

st.markdown("<br><br>", unsafe_allow_html=True)


if "history" not in st.session_state:
    st.session_state.history = []

if st.session_state.history:
    for item in st.session_state.history:
        message(item['query'], is_user=True, key=f"user_{item['query']}")
        message(item['answer'], is_user=False, key=f"bot_{item['answer']}")

query = st.chat_input("Type your question here...", key="query")

if query:
    with st.spinner("Finding the answer..."):
        answer = qa_chain.run(query)
        st.session_state.history.append({"query": query, "answer": answer})
        message(query, is_user=True, key=f"user_{query}")
        message(answer, is_user=False, key=f"bot_{answer}")
