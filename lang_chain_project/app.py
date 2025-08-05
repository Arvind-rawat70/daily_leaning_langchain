from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

## chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpfull assiastant,Please resopnd to the question asked"),
        ("user", "Question: {question}")
    ]
)

## streamlit framework
st.title("langchain demo woth llama2")
input_text = st.text_input("what is the question asked ")

##Ollama LLama2 model
llm = Ollama(model = "gemma:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))