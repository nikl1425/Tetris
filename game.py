import pygame


class Game:
    def __init__(self, screen, width, height):
        self.state = "playing"
        self.screen = screen
        self.width = width
        self.height = height
  #      self.background = pygame.draw.rect(screen, "black", (0, 0, self.width, self.height))

    def event_handler(self, event):
        pass

    def render(self):
        pass

    def update(self):
        pass

    def main(self):
        for event in pygame.event.get():
            self.event_handler(event)
        self.update()
        self.render()