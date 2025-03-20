# export all the env variables 

import os 
from dotenv import load_dotenv
from langchain_community.llms import Ollama 

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser




load_dotenv()
# For Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')


# Prompt Template 

prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Please respond to the question asked.\n\nUser: {question}"
)



# Streamlit Framework

st.title("Langchain Demo with Lamma2")
input_text = st.text_input("Enter your question here" ) 


# Call the Ollma model 
llm = Ollama(model = "gemma:2b")             # google open source model 
output_parser = StrOutputParser()    # to show the output on desired value

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))




''' 

NOTE: The ollma model has inbuilt tracking system which is eventually free of cost . 
      So in the runnable sequence , it will show the steps or the tracking of the model from where it is running .

'''






