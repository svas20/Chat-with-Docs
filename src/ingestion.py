from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging
import os

def load_data():
    try:
        logging.info("data loading started")
        folder_path = os.path.abspath("uploaded_files")
        loader = SimpleDirectoryReader(folder_path)
        documents=loader.load_data()
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.info("exception in loading data")
        raise customexception(e,sys)
    

        
