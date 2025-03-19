import requests
import streamlit as st

def get_llama_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

def get_gemma_response(input_text):
    response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an essay on (Using llama 3.2)")
input_text1=st.text_input("Write a poem on (Using Gemma 3)")

if input_text:
    st.write(get_llama_response(input_text))

if input_text1:
    st.write(get_gemma_response(input_text1))