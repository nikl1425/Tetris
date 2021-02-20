import pygame



class intro:
    def __init__(self, screen, width, height):
        self.state = "intro"
        self.screen = screen
        self.running = True
        self.width = width
        self.height = height
        self.background = pygame.draw.rect(screen, "black", (0, 0, self.width, self.height))

    def event_handler(self, event):
        pass

    def render(self):
        print(self.state)
        pygame.draw.rect(self.screen, "black", (0, 0, self.width, self.height))
        pygame.display.flip()

    def update(self):
        pass

    def main(self):
        for event in pygame.event.get():
            self.event_handler(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "playing"
        self.update()
        self.render()
