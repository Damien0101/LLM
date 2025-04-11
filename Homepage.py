import streamlit as st
from google import genai
from google.genai import types
import json



with open('api_key.json') as f:
    API_KEY = json.load(f)['API_KEY']

client = genai.Client(api_key=API_KEY)


def gen_prompt():
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=query,
        config=types.GenerateContentConfig(
            max_output_tokens=500,
            temperature=0.5
        ))
    return response.text



st.set_page_config(page_title="Gemini Chatbot", layout="wide", page_icon='⚕️')


LANGUAGES = {
    'English': 'en',
    'Français': 'fr',
    'Español': 'es',
    'Deutsch': 'de',
    'Nederlands': 'nl'
}

selected_language = st.sidebar.selectbox('Select Language', options=list(LANGUAGES.keys()))

def translate(text, lang_code):
    return text




st.markdown("<h1 style='text-align: center;'>DiagnosMe 🧑‍⚕️</h1>", unsafe_allow_html=True)
st.divider()

st.markdown("<br><br>", unsafe_allow_html=True)


if "history" not in st.session_state:
    st.session_state.history = []

chatbox = st.empty()


if st.session_state.history:
    for item in st.session_state.history:
        st.chat_message(name="user", avatar="👤", is_user=True).markdown(f"{item['query']}")
        st.chat_message(name="bot", avatar="🧠").markdown(f"{item['answer']}")

query = st.chat_input("Type your question here...", key="query")

if query:
    with st.spinner("Finding the answer..."):
        answer = gen_prompt()
        st.session_state.history.append({"query": query, "answer": answer})
        st.chat_message(name="user", avatar="👤").markdown(f"{query}")
        st.chat_message(name="bot", avatar="🧠").markdown(f"{answer}")






user = '🤒'