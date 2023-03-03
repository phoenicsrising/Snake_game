import pygame
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import math


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("My Snake Game")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Courier", 20)

    snake = Snake(screen.get_width(), screen.get_height())
    food = Food(screen.get_width(), screen.get_height())
    scoreboard = Scoreboard()

    game_over = False
    running = True
    start_prompt = True
    while running:
        if start_prompt:
            text = font.render("Press spacebar to start", True, (255, 255, 255))
            screen.blit(text, (
                screen.get_width() / 2 - text.get_width() / 2,
                screen.get_height() / 2 - text.get_height() / 2))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start_prompt = False
                        break
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                snake.up()
            if keys[pygame.K_DOWN]:
                snake.down()
            if keys[pygame.K_LEFT]:
                snake.left()
            if keys[pygame.K_RIGHT]:
                snake.right()

            snake.move()

            if math.hypot(snake.segments[0][0] - food.x, snake.segments[0][1] - food.y) < 20:
                food.refresh()
                snake.create_extra_segment()
                scoreboard.keep_score()

            for i in range(1, len(snake.segments)):
                if snake.segments[0] == snake.segments[i]:
                    game_over = True

            if game_over:
                text = font.render("Game Over! Your score is {}".format(scoreboard.score), True, (255, 255, 255))
                screen.blit(text, (
                    screen.get_width() / 2 - text.get_width() / 2,
                    screen.get_height() / 2 - text.get_height() / 2))
                text = font.render("Press space to play again or Esc to exit", True, (255, 255, 255))
                screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2,
                                   screen.get_height() / 2 - text.get_height() / 2 + text.get_height()))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        running = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            game_over = False
                            snake = Snake(screen.get_width(), screen.get_height())
                            food = Food(screen.get_width(), screen.get_height())
                            scoreboard.reset_score()
                            break  # add this line to break out of the loop

            else:
                screen.fill((0, 0, 0))
                food.draw(screen)
                for segment in snake.segments:
                    pygame.draw.rect(screen, (255, 255, 255), (segment[0], segment[1], 20, 20))
                scoreboard.display_score(screen)
                pygame.display.update()
                clock.tick(20)

    pygame.quit()


if __name__ == '__main__':
    main()


