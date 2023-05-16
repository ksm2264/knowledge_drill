from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel

from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from knowledge_drill.drill.new_fact import new_fact_for_topic

template = '''
Come up with a {question_type} that quizzes knowledge of {fact}. This is for a quiz about {topic}

Format like this:
{format_instructions}

'''

dumb_llm = ChatOpenAI(model_name = 'gpt-3.5-turbo')

# todo have this cross check in vector DB for established knowledge
def new_question(topic: str, question_type: BaseModel) -> BaseModel:

    fact = new_fact_for_topic(topic)

    question_parser = PydanticOutputParser(pydantic_object = question_type)

    prompt = PromptTemplate(
        template = template,
        input_variables = ['question_type', 'fact', 'topic'],
        partial_variables={'format_instructions':question_parser.get_format_instructions()}
    )

    question_extractor = LLMChain(llm = dumb_llm, prompt = prompt)

    question_type_str = question_type.__name__


    raw_response = question_extractor.predict(
        question_type = question_type_str,
        fact = fact,
        topic = topic
    )

    question = question_parser.parse(raw_response)

    return question, fact

