import random
import pygame


class Food:

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.refresh()

    def refresh(self):
        self.x = random.randint(0, self.screen_width)
        self.y = random.randint(0, self.screen_height)

    def draw(self, screen):
        food_diameter = 7
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), food_diameter)
