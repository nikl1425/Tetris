import pygame


class Game:
    def __init__(self, screen, width, height):
        self.state = "intro"
        self.screen = screen
        self.running = False
        self.width = width
        self.height = height
        self.background = pygame.draw.rect(screen, "grey", (0, 0, self.width, self.height))

    def event_handler(self, event):
        pass

    def render(self):
        pygame.draw.rect(self.screen, "grey", (0, 0, self.width, self.height))
        pygame.display.flip()

    def update(self):
        pass

    def main(self):
        for event in pygame.event.get():
            self.event_handler(event)

        self.update()
        self.render()