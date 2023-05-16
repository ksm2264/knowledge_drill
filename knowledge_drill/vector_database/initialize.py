import faiss

from langchain.docstore import InMemoryDocstore
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

embedding_size = 1536 # Dimensions of the OpenAIEmbeddings
index = faiss.IndexFlatL2(embedding_size)
embeddings = OpenAIEmbeddings()
embedding_fn = embeddings.embed_query

def new_database_for_topic(topic: str):

    vectorstore = FAISS(embedding_fn, index, InMemoryDocstore({}), {})

    vectorstore.save_local(f'faiss_databases/{topic}')
