import pygame
import snake
import food
from util import Direction

# initialize speed
snake_speed = 2
clock = pygame.time.Clock()

# Window size
window_x = 800
window_y = 800

# defining colors
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
red = pygame.Color(255, 0, 0)


def game_over():
    pygame.display.flip()
    pygame.quit()
    quit()


# Main Function
# Initialising pygame
pygame.init()

# Initialise game window
game_window = pygame.display.set_mode((window_x, window_y))

snake = snake.Snake(window_x, window_y)
food = food.Food(window_x, window_y)

is_running = True

while is_running:
    # handling key events
    # pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.turn(Direction.UP)
            if event.key == pygame.K_DOWN:
                snake.turn(Direction.DOWN)
            if event.key == pygame.K_LEFT:
                snake.turn(Direction.LEFT)
            if event.key == pygame.K_RIGHT:
                snake.turn(Direction.RIGHT)
            if event.key == pygame.K_1:
                is_running = False

    collision = snake.get_head_position() == food.position
    grow = False

    if collision:
        grow = True
        food.move_random_position(snake_pos=snake.positions)

    snake.move(grow=grow)

    game_window.fill(black)

    pygame.draw.rect(
        game_window, red, pygame.Rect(
            food.position.x*100, food.position.y*100, 100, 100))

    for curr in snake.positions:
        pygame.draw.rect(
            game_window, green, pygame.Rect(
                curr.x*100, curr.y*100, 100, 100))

    pygame.display.update()
    clock.tick(snake_speed)
