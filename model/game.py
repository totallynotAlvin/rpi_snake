# importing libraries
import pygame


# initialize speed
snake_speed = 15
clock = pygame.time.Clock()

# Window size
window_x = 800
window_y = 800

# defining colors
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


def game_over():
    pygame.display.flip()
    pygame.quit()
    quit()


# Main Function
# Initialising pygame
pygame.init()

# Initialise game window
game_window = pygame.display.set_mode((window_x, window_y))

snake_position = [100, 50]
snake_body = [[100, 100], [90, 100], [80, 100], [70, 100]]

direction = 'RIGHT'
change_to = direction
is_running = True

while is_running:
    # handling key events
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_1:
                is_running = False
# Checks whether the input is illegal
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

# Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    game_window.fill(black)
    snake_body.insert(0, list(snake_position))
    snake_body.pop()

    for pos in snake_body:
        pygame.draw.rect(
            game_window, green, pygame.Rect(
                pos[0], pos[1], 10, 10))

    pygame.display.update()
    clock.tick(snake_speed)