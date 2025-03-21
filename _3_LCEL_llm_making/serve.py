''' 

Here we are deploying the model that we have made , we are using FAST Api to do it .


'''


from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes  


# load the env files 
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")



#  choose the model
model = ChatGroq(model = "Gemma2-9b-It" , groq_api_key = groq_api_key)



# 1. Create prompt Template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system' , system_template) ,
    ('user' , '{text}')
])



# initiate the parser 
parser = StrOutputParser()



# create chain
chain = prompt_template|model|parser



# App defination
app = FastAPI(

    title='Langchain Server' ,
    version='1.0' ,
    description=' A simple API server using langchain runnable interface'

)


# create the routes 
add_routes(
    app ,
    chain ,
    path = '/chain' 
)



if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app , host='127.0.0.1' , port=8000)



# http://localhost:8000/docs

















