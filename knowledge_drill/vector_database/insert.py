
import faiss

from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

embedding_size = 1536 # Dimensions of the OpenAIEmbeddings
index = faiss.IndexFlatL2(embedding_size)
embeddings = OpenAIEmbeddings()


def insert(topic:str, fact: str):
    
    db = FAISS.load_local(f'faiss_databases/{topic}', embeddings)

    db.add_texts(texts = [fact])

    db.save_local(f'faiss_databases/{topic}')