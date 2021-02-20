import pygame
from button import Button


class intro:
    def __init__(self, screen, width, height):
        self.state = "intro"
        self.screen = screen
        self.running = True
        self.width = width
        self.height = height
        self.background = pygame.image.load("assets/intro_background.png")
        self.start_game = Button(200, 200, 50, 20, "red", "blue")

    def event_handler(self, event):
        mouseX, mouseY = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        if self.start_game.check_hover():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.state = "playing"

    def render(self):
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.screen.blit(self.background, (0, 0))
        self.start_game.draw(self.screen)
        pygame.display.flip()

    def change_state(self):
        print("hi")

    def main(self):
        for event in pygame.event.get():
            self.event_handler(event)

        self.render()
