import pygame

from knowledge_drill.ui.constants import WIDTH, HEIGHT

def render_topic_prompt(screen):
    # Clear the screen
    screen.fill((0, 0, 0))

    # Create a font object
    font = pygame.font.Font(None, 36)

    # Create the prompt surface
    prompt = font.render("Enter a topic:", True, (255, 255, 255))
    
    # Draw the prompt
    screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 - prompt.get_height() // 2 - 50))

    # Create a text box
    textbox = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2, 400, 50)
    pygame.draw.rect(screen, (255, 255, 255), textbox)

    pygame.display.flip()  # Update the display

    # Handle user input
    current_string = []
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:  # Remove the last character
                if len(current_string) > 0:
                    current_string.pop()
            elif event.key == pygame.K_RETURN:  # End input
                break
            else:  # Add a new character
                current_string.append(event.unicode)

        # Update the input surface
        input_text = font.render("".join(current_string), True, (0, 0, 0))

        # Redraw everything
        screen.fill((0, 0, 0))
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 - prompt.get_height() // 2 - 50))
        pygame.draw.rect(screen, (255, 255, 255), textbox)
        screen.blit(input_text, (textbox.x + 10, textbox.y + 10)) # Adjust the placement of text
        pygame.display.flip()

    return "".join(current_string)
