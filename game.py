import pygame
from block import Block
import time
from collections import deque
import numpy as np
from copy import deepcopy

gameX = 100
gameY = 0
gameWidth = 400
gameHeight = 400
grid_width = 10
grid_height = 20

clock = pygame.time.Clock()
locked_positon = []
grid_start = gameWidth // 3
locked_list = []
tetro2 = Block(20)


def iterate_through_locked_position(locked_pos_list):
    for element in locked_pos_list:
        rect, color = element
        for i in rect:
            locked_list.append(i)
            print("HEJ HEJ" + str(locked_list))


class tetromino(object):
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.rotation = 0



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
        self.tetro = Block(20)
        self.tetro_list = []
        self.locked_positions = deque([])
        self.locked_tetro = []
        self.blocks = Block(20)
        self.current_tetro, self.current_tetro_color = self.tetro.create_block()
        self.locked_tetro_list_rect = []
        self.locked_tetro_colors = []


    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_d:
                for element in self.current_tetro:
                    element[0] += 1
            if event.key == pygame.K_a:
                for element in self.current_tetro:
                    element[0] -= 1
                    element[1] += 0
            if event.key == pygame.K_SPACE:
                for element in self.current_tetro:
                    element[1] += 15
            if event.key == pygame.K_r:
                self.tetro.rotation += 1
                self.current_tetro = self.tetro.rotate_block(self.current_tetro)

    def render(self):
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, "black", self.game_window)

        for i in self.grid:
            pygame.draw.rect(self.screen, (200, 200, 200), i, 1)

        for j in self.tetro_list:
            pygame.draw.rect(self.screen, self.current_tetro_color, j)

            for element in self.locked_tetro_list_rect:
                rect, color = element
                pygame.draw.rect(self.screen, color, rect)

        pygame.display.flip()

    def create_grid(self):
        for y in range(grid_height):
            for x in range(grid_width):
                rect = pygame.Rect((x * self.blocks.size) + grid_start, y * self.blocks.size, self.blocks.size,
                                   self.blocks.size)
                self.grid.append(rect)

    def create_tetros(self):
        self.tetro_list = []
        for element in self.current_tetro:
            rect = pygame.Rect(element[0] * self.blocks.size + grid_start,
                               element[1] * self.blocks.size,
                               self.blocks.size,
                               self.blocks.size)
            self.tetro_list.append(rect)

    def create_locked_tetros(self):
        for element in self.locked_tetro:
            rect_list, color = element
            for elements in rect_list:
                rect = pygame.Rect(elements[0] * self.blocks.size + grid_start,
                                   elements[1] * self.blocks.size,
                                   self.blocks.size,
                                   self.blocks.size)
                this_set = (rect, color)
                self.locked_tetro_list_rect.append(this_set)
                self.locked_tetro_colors.append(color)

    def tetro_movement(self):
        hit_bottom = False
        if any(element >= 19 for (_, element) in self.current_tetro):
            hit_bottom = True
        else:
            for element in self.current_tetro:
                element[1] += 1

        locked_rects = []
        for element in self.locked_tetro:
            rect_list, color = element
            for rect in rect_list:
                locked_rects.append(rect)

        locked_element = []
        locked_element.extend([rects for (rects, _) in self.locked_tetro])
        print(self.tetro.shape)
        for i in locked_element:
            for inner_element in i:

                if any(rects[1] == inner_element[1] - 1 for rects in self.current_tetro) and any(
                        rects[0] == inner_element[0] for rects in self.current_tetro):
                    hit_bottom = True

        if hit_bottom:
            locked_tetro_set = (self.current_tetro, self.current_tetro_color)
            self.locked_tetro.append(locked_tetro_set)
            self.current_tetro, self.current_tetro_color = self.tetro.create_block()

    def update(self):
        global next_tetro
        self.create_grid()
        self.tetro_movement()
        self.create_locked_tetros()
        self.create_tetros()

    def main(self):
        clock.tick(1)
        for event in pygame.event.get():
            self.event_handler(event)

        self.update()
        self.render()
