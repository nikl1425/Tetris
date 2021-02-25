import pygame
from block import Block

gameX = 100
gameY = 0
gameWidth = 400
gameHeight = 400
grid_width = 10
grid_height = 20

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
        self.blocks = Block(20)

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    def render(self):
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, "black", self.game_window)

        for y in range(grid_height):
            for x in range(grid_width):
                grid_start = x + gameWidth // 3
                rect = pygame.Rect((x*self.blocks.size) + grid_start, y*self.blocks.size, self.blocks.size, self.blocks.size)
                pygame.draw.rect(self.screen, (200, 200, 200,), rect, 1)

        pygame.display.flip()

    def update(self):
        for c in range(grid_width):
            column = []
            for r in range(grid_height):
                column.append(self.blocks.color)
            self.grid.append(column)
        print(self.grid, end=' ')

    def main(self):
        for event in pygame.event.get():
            self.event_handler(event)

        self.update()
        self.render()
