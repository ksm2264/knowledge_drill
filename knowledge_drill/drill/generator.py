import numpy as np

from knowledge_drill.models.question import question_types
from knowledge_drill.drill.new_question import new_question

def new_random_question(topic):

    question_type = np.random.choice(question_types)

    question = new_question(topic, question_type)
     
    return question

if __name__ == '__main__':

    topic = input('Enter a topic:')

    while True:

        question = new_random_question(topic)

        print(question)

        input('Press Enter to continue')