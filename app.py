import streamlit as st
from src.ingestion import load_data
from src.embedding import embedding
from src.model import  model
import os


def main():
    st.header("Chat with Docs")
    with st.sidebar:
        OPENAI_API_KEY = st.text_input("Enter your OPENAI_API_KEY:")
        if st.button("Enter"):
            os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
            st.session_state.api_key_provided = True
        if 'api_key_provided' in st.session_state and st.session_state.api_key_provided:
            SAVE_DIR = "uploaded_files"
            os.makedirs(SAVE_DIR, exist_ok=True) 
            uploaded_files = st.file_uploader("Please upload your documents", type=["txt", "pdf", "docx"], accept_multiple_files=True)
            if uploaded_files:
                for uploaded_file in uploaded_files:
                    
                    st.write(f"**File name:** {uploaded_file.name}")
                    
                    with open(os.path.join(SAVE_DIR, uploaded_file.name), "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    st.success(f"File saved to {os.path.join(SAVE_DIR, uploaded_file.name)}")

    if 'api_key_provided' in st.session_state and st.session_state.api_key_provided:            
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
