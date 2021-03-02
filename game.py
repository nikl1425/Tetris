import pygame
from block import Block

gameX = 100
gameY = 0
gameWidth = 400
gameHeight = 400
grid_width = 10
grid_height = 20
tetro = Block(20)
clock = pygame.time.Clock()
locked_positon = []
grid_start = gameWidth // 3




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
        self.tetro_list = []
        self.locked_positions = []
        self.blocks = Block(20)
        self.current_tetro, self.current_tetro_color = tetro.create_block()

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_s:
                print("clicked")

    def render(self):
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, "black", self.game_window)

        for i in self.grid:
            pygame.draw.rect(self.screen, (200, 200, 200), i, 1)

        for j in self.tetro_list:
            pygame.draw.rect(self.screen, self.current_tetro_color, j)

        for element in self.locked_positions:
            rect_list, color = element
            for rect in rect_list:
                pygame.draw.rect(self.screen, color, rect)





        pygame.display.flip()

    def create_grid(self):
        for y in range(grid_height):
            for x in range(grid_width):
                rect = pygame.Rect((x*self.blocks.size) + grid_start, y*self.blocks.size, self.blocks.size, self.blocks.size)
                self.grid.append(rect)

    def create_tetros(self):
        self.tetro_list = []
        for element in self.current_tetro:
            rect = pygame.Rect(element[0] * self.blocks.size + grid_start,
                              element[1] * self.blocks.size,
                              self.blocks.size,
                              self.blocks.size)
            self.tetro_list.append(rect)

    def tetro_movement(self):
        for element in self.current_tetro:
            if element[1] >= 19:
                element[1] += 0
                this_set = (self.tetro_list, self.current_tetro_color)
                self.locked_positions.append(this_set)
                self.current_tetro, self.current_tetro_color = tetro.create_block()
            else:
                element[1] += 1

    def update(self):
        global next_tetro
        self.create_grid()
        self.tetro_movement()
        self.create_tetros()
        #print('tetrolist ' + str(self.tetro_list))
        #print(self.current_tetro)
        print(self.locked_positions)
        #print('gridlist ' + str(self.grid))


    def main(self):
        clock.tick(1)
        for event in pygame.event.get():
            self.event_handler(event)

        self.update()
        self.render()
