from fastapi import FastAPI  
from langchain_openai import ChatOpenAI  
from langchain_core.prompts import ChatPromptTemplate  # Template engine for prompt construction
from langserve import add_routes  # Utility to automatically mount LangChain endpoints
import uvicorn  # ASGI server to run the FastAPI app
import os  
from langchain_community.llms import Ollama  # Ollama LLM integration
from dotenv import load_dotenv 


load_dotenv()

# Initialize FastAPI application with basic metadata
app = FastAPI(
    title="Langchain Server",        # Title displayed in autogenerated docs
    version="1.0",                   # API version
    description="A simple API Server"  
)

# Initialize two Ollama-backed language models
llm1 = Ollama(model="llama3.2:1b")  
llm2 = Ollama(model="gemma3:1b")    


prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)
prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5-year-old child with 100 words"
)

# Automatically mount a POST endpoint at /essay
# When called, it applies prompt1 to llm1 and returns generated essay
add_routes(
    app,
    prompt1 | llm1,    # Chain: template -> LLM
    path="/essay"    # URL path for essay generation
)

# Automatically mount a POST endpoint at /poem
# When called, it applies prompt2 to llm2 and returns generated poem
add_routes(
    app,
    prompt2 | llm2,    # Chain: template -> LLM
    path="/poem"     # URL path for poem generation
)

# Entry point: Run the FastAPI app with Uvicorn when script is executed directly
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",  
        port=8000         
    )
