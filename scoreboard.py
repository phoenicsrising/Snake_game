import pygame

def get_highscore():
    with open("highscore.txt", "r") as file:
        content = int(file.read())
        highscore = content
        return highscore


def write_to_highscore_file(score):
        with open("highscore.txt", mode="w") as file:
            file.write(str(score))


class Scoreboard:

    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Courier", 20)

    def keep_score(self):
        self.score += 1
        if self.score > get_highscore():
            write_to_highscore_file(self.score)
        get_highscore()
    def reset_score(self):
        self.score = 0


    def display_score(self, screen):
        score_text = self.font.render(f"Score: {self.score}  High Score: {get_highscore()}", False, (255, 255, 255))
        screen.blit(score_text, (250, 0))
