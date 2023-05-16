
from langchain.prompts import PromptTemplate


from knowledge_drill.vector_database.retrieve import retrieve
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI


dumb_llm = ChatOpenAI(
    model_name = 'gpt-3.5-turbo'
)

template_query_fact = '''
What is one standalone fact about {topic}.

Keep it short.
'''

query_fact_prompt = PromptTemplate(
    template = template_query_fact,
    input_variables=['topic']
)

query_fact_extractor = LLMChain(
    llm = dumb_llm,
    prompt=query_fact_prompt
)

template_novel_fact = '''
What is one standalone fact about {topic}.

Make sure it is not present among these existing facts:
{existing_facts}
'''

novel_fact_prompt = PromptTemplate(
    template = template_novel_fact,
    input_variables = ['topic', 'existing_facts']
)

novel_fact_generator = LLMChain(
    llm = dumb_llm,
    prompt = novel_fact_prompt
)

def new_fact_for_topic(topic: str):

    query_fact = query_fact_extractor.predict(
        topic = topic
    )

    print(f'Query fact: {query_fact}')

    existing_facts = retrieve(topic, query_fact)

    print(f'Closest existing facts: {existing_facts}')

    novel_fact = novel_fact_generator.predict(
        topic = topic,
        existing_facts = existing_facts
    )

    return novel_fact


