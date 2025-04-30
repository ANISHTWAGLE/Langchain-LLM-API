import requests   
import streamlit as st  

# Function to request an essay from the /essay endpoint
def get_llama_response(input_text: str) -> str:
    # Send POST request with JSON payload containing 'topic'
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input": {"topic": input_text}}
    )
    # Extract and return the 'output' field from the JSON response
    return response.json().get('output', '')

# Function to request a poem from the /poem endpoint
def get_gemma_response(input_text: str) -> str:
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={"input": {"topic": input_text}}
    )
    return response.json().get('output', '')


st.title('LangChain Demo with Llama & Gemma')


input_text = st.text_input(
    label="Write an essay on (using Llama 3.2)",
    help="Enter the topic for the essay."
)

input_text1 = st.text_input(
    label="Write a poem on (using Gemma 3)",
    help="Enter the topic for the poem."
)

# When essay input is provided, fetch and display the essay
if input_text:
    essay = get_llama_response(input_text)
    st.subheader("Generated Essay")
    st.write(essay)

# When poem input is provided, fetch and display the poem
if input_text1:
    poem = get_gemma_response(input_text1)
    st.subheader("Generated Poem")
    st.write(poem)
