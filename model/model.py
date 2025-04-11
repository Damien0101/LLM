from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
import json
import pickle



with open('api_key.json') as f:
    API_KEY = json.load(f)['API_KEY']

with open('data/data.txt', 'r') as f:
    state_of_the_union = f.read()

def model(API_KEY=API_KEY, state_of_the_union=state_of_the_union):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=200,
        add_start_index=True)

    chunks = splitter.split_text(state_of_the_union)

    vectors = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=API_KEY)

    vector_store = Chroma.from_texts(texts=chunks, embedding=vectors)

    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=API_KEY)

    qa_chain = RetrievalQA.from_chain_type(
        llm=model,
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )
    return qa_chain
















# split data: chunk
# vectorized
# put vectors in db
# generate resp: QAchain

