import pygame

gameX = 100
gameY = 0
gameWidth = 400
gameHeight = 400
grid_width = 10
grid_height = 10

class Game:
    def __init__(self, screen, width, height):
        self.state = "intro"
        self.screen = screen
        self.running = False
        self.width = width
        self.height = height
        self.game_window = pygame.Rect(gameX, gameY, gameWidth, gameHeight)
        self.background = pygame.image.load("assets/game_background.png")
        self.grid = []

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    def render(self):
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, "black", self.game_window)

        for y in range(grid_width):
            for x in range(grid_height):
                pygame.draw.rect(self.screen, (255,255,255), (x, y, 30,30))

        pygame.display.flip()

    def update(self):
        for c in range(grid_width):
            column = []
            for r in range(grid_height):
                column.append('#')
            self.grid.append(column)
        print(self.grid)

    def main(self):
        for event in pygame.event.get():
            self.event_handler(event)

        self.update()
        self.render()
