import os

from knowledge_drill.vector_database.initialize import new_database_for_topic

def setup(topic: str):

    if not os.path.exists(f'faiss_databases/{topic}'):
        new_database_for_topic(topic)