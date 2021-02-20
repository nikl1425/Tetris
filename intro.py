import pygame



class intro:
    def __init__(self, screen, width, height):
        self.state = "intro"
        self.screen = screen
        self.running = True
        self.width = width
        self.height = height
        self.background = pygame.image.load("assets/intro_background.png")

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.state = "playing"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    def render(self):
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.screen.blit(self.background, (0,0))
        pygame.display.flip()

    def update(self):
        pass

    def main(self):
        for event in pygame.event.get():
            self.event_handler(event)



        self.update()
        self.render()
