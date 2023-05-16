

import faiss

from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

embedding_size = 1536 # Dimensions of the OpenAIEmbeddings
index = faiss.IndexFlatL2(embedding_size)
embeddings = OpenAIEmbeddings()


def retrieve(topic:str, fact: str) -> list[str]:
    
    db = FAISS.load_local(f'faiss_databases/{topic}', embeddings)

    closest_facts = db.similarity_search(fact)

    fact_strings = [doc.page_content for doc in closest_facts]

    return fact_strings