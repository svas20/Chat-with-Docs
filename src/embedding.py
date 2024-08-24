from llama_index.core import VectorStoreIndex

from llama_index.core import Settings

from llama_index.core.node_parser import SentenceSplitter

from llama_index.embeddings.openai import OpenAIEmbedding

import sys
from exception import customexception
from logger import logging

def embedding(doc_list):
        try:
            logging.info("loading embedding models")
            Settings.embed_model = OpenAIEmbedding( model="text-embedding-3-small", embed_batch_size=100)
            Settings.node_parser=SentenceSplitter(chunk_size=512,chunk_overlap=20)
            logging.info("Indexing  the documents")
            Index=VectorStoreIndex.from_documents(doc_list,embed_model=Settings.embed_model,node_parser=Settings.node_parser)
            Index.storage_context.persist()
            return Index
        except Exception as e:
            raise customexception(e,sys)

    