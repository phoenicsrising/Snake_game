import pygame

class Scoreboard:

    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Courier", 20)

    def keep_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def display_score(self, screen):
        score_text = self.font.render(f"Score: {self.score}", False, (255, 255, 255))
        screen.blit(score_text, (250, 0))
