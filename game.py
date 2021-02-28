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


        for y in range(grid_height):
            for x in range(grid_width):
                grid_start = x + gameWidth // 3
                rect = pygame.Rect((x*self.blocks.size) + grid_start, y*self.blocks.size, self.blocks.size, self.blocks.size)
                pygame.draw.rect(self.screen, (200, 200, 200,), rect, 1)


                for element in self.current_tetro:
                    try:
                        grid_start = element[0] + gameWidth // 3
                        pygame.draw.rect(self.screen, self.current_tetro_color,
                                        ((element[0]*self.blocks.size) + grid_start,
                                        element[1]*self.blocks.size,
                                        self.blocks.size,
                                        self.blocks.size))
                    except: print("PENDING NEW TETRO")


        pygame.display.flip()

    def update(self):
        global next_tetro
        for c in range(grid_width):
            column = []
            for r in range(grid_height):
                column.append(self.blocks.color)

            self.grid.append(column)

        for element in self.current_tetro:
            holder_list = []
            holder_list.append(element[1])



            if all(i == grid_height-1 for i in holder_list):
                element[1] += 0
                locked_positon.append(element[1])
                print(locked_positon)
                for locked_block in locked_positon:
                    try:
                        if int(element[1]) == int(locked_block) - 1:
                            element[1] += 0
                    except:
                        print("haha")
                        print(locked_block)
            else:
                element[1] += 1




        #print(self.grid, end=' ')



    def main(self):
        clock.tick(1)
        for event in pygame.event.get():
            self.event_handler(event)

        self.update()
        self.render()
