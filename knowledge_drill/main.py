import pygame
import sys
import time

from knowledge_drill.ui.constants import WIDTH, HEIGHT, WHITE
from knowledge_drill.ui.renderers.topic_entry import render_topic_prompt

from knowledge_drill.models.question import MultipleChoiceQuestion
from knowledge_drill.drill.new_question import new_question

from knowledge_drill.vector_database.insert import insert

from knowledge_drill.setup import setup

# Initialize Pygame
pygame.init()


# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Button:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, pygame.Rect(self.x, self.y, WIDTH-10, 50))
        text = FONT.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x, self.y))

def render_multiple_choice(question):
    # Draw the question
    text = FONT.render(question.question, True, WHITE)
    screen.blit(text, (0, 0))

    # Draw buttons for each choice
    for i, choice in enumerate(question.choices):
        button = Button(str(i)+'. '+choice, 0, (i+1)*60)
        button.draw(screen)

    return [Button(choice, 0, (i+1)*60) for i, choice in enumerate(question.choices)]

def render_generating(screen):
    screen.fill((0, 0, 0))  # Clear the screen
    font = pygame.font.Font(None, 36)  # Create a font object
    text = font.render("Generating new question...", True, (255, 255, 255))  # Create a text surface
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))  # Center the text
    pygame.display.flip()  # Update the display

def render_feedback(screen, is_correct):
    # Clear the screen
    screen.fill((0, 0, 0))

    # Create a font object
    font = pygame.font.Font(None, 36)

    # Create the feedback surface
    if is_correct:
        feedback = font.render("Correct!", True, (0, 255, 0))  # Green text
    else:
        feedback = font.render("Incorrect!", True, (255, 0, 0))  # Red text

    # Draw the feedback
    screen.blit(feedback, (WIDTH // 2 - feedback.get_width() // 2, HEIGHT // 2 - feedback.get_height() // 2))

    pygame.display.flip()  # Update the display
    time.sleep(2)

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        render_feedback(screen, True)
        return True
    else:
        render_feedback(screen, False)
        return False
# Game loop

move_on = False

topic = render_topic_prompt(screen)
FONT = pygame.font.Font(None, 36)

setup(topic)

render_generating(screen)
question, fact = new_question(topic, MultipleChoiceQuestion)
buttons = render_multiple_choice(question)
print(f'Fact: {fact}')
print(f'Question: {question}')
while True:
    screen.fill((0, 0, 0))
    render_multiple_choice(question)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                move_on = check_answer(0, question.correct_answer_index)
            elif event.key == pygame.K_2:
                move_on = check_answer(1, question.correct_answer_index)
            elif event.key == pygame.K_3:
                move_on = check_answer(2, question.correct_answer_index)
            elif event.key == pygame.K_4:
                move_on = check_answer(3, question.correct_answer_index)
            # ...add more elifs if there are more than 4 choices

    if move_on:
        insert(topic, fact)
        render_generating(screen)

        question, fact = new_question(topic, MultipleChoiceQuestion)

        move_on = False

        print(f'Fact: {fact}')
        print(f'Question: {question}')
