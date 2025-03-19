from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)


##ollama llama2
llm1=Ollama(model="llama3.2:1b")
llm2=Ollama(model="gemma3:1b")
prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1|llm1,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm2,
    path="/poem"


)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)