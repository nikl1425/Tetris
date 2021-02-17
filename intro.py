import pygame


class intro:
    def __init__(self, screen, width, height):
        self.state = "intro"
        self.screen = screen
        self.width = width
        self.height = height
        self.background = pygame.draw.rect(screen, "black", (0, 0, self.width, self.height))

    def render(self):
        pass

    def update(self):
        pass