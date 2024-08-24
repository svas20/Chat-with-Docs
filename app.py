import streamlit as st
from src.ingestion import load_data
from src.embedding import embedding
from src.model import  model



def main():
    st.header("Conversational Chatbot")
    user_query=st.text_input("Ask your Query")
    if st.button("submit"):
        with st.spinner("Processing"):
            doc_list=load_data()
            Index=embedding(doc_list)
            query_engine=model(Index)
            response=query_engine.query(user_query)
            st.write(response.response)

if  __name__ == "__main__":
    main()
