from llama_index.llms.openai import OpenAI

from llama_index.core import Settings


import sys
from exception import customexception
from logger import logging

def model(Index):
    try:
        logging.info("loading the model")
        Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)
        query_engine=Index.as_query_engine(llm=Settings.llm)
        return query_engine
    except Exception as e:
        raise customexception(e,sys)
    

