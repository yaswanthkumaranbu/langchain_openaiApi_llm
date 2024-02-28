import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

st.title('Demo on Langchain with OPENAI API')
input=st.text_input("Search the content:")

llm=OpenAI(temperature=0.8)

if(input):
    st.write(llm(input))