import pygame
from block import Block
import time
from collections import deque
import numpy as np
from copy import deepcopy
from itertools import groupby

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



def iterate_through_locked_position(locked_pos_list):
    for element in locked_pos_list:
        rect, color = element
        for i in rect:
            locked_list.append(i)



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
            if event.key == pygame.K_s:
                for element in self.current_tetro:
                    element[1] += 1
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

        #print("lockedlist: ", self.locked_tetro)
        #print("lockedrect ", self.locked_tetro_list_rect)

        for element in self.locked_tetro:
            rect_list, color = element
            for elements in rect_list:
                pygame.draw.rect(self.screen, color, (elements[0] * self.blocks.size + grid_start,
                                   elements[1] * self.blocks.size,
                                   self.blocks.size - 1,
                                   self.blocks.size - 1))


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
        pass


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
        #print(self.tetro.shape)
        for i in locked_element:
            for inner_element in i:
                for rects in self.current_tetro:
                    if rects[1] >= inner_element[1] - 1:
                        if rects[0] == inner_element[0]:
                            hit_bottom = True

        for i in self.locked_tetro:
            r, c = i
            for e in r:
                print("comp: ", e )
                x = e[0]
                y = e[1] + 1
                new_e = [x, y]
                print("new: ", [x,y])
                if new_e not in [item for item in r] and e[1] < 19:
                    e[1] += 1




        if hit_bottom:
            #print("currentbeforelocked" +str(self.current_tetro))
            locked_tetro_set = (self.current_tetro, self.current_tetro_color)
            self.locked_tetro.append(locked_tetro_set)
            self.current_tetro, self.current_tetro_color = self.tetro.create_block()

    def get_points(self):
        check_list = []
        for element in self.locked_tetro:
            rect, color = element
            check_list.extend(rect)
        row_list = []
        for i in range(grid_height):
            column_list = []
            for element in check_list:
                x, y = element
                if y == i:
                    column_list.append(element)
            row_list.append(column_list)

        completed_rows = []
        check = False
        for element in row_list:
            if len(element) == 10:
                completed_rows = element
                check = all(item in check_list for item in completed_rows)

        if check is True:
            print("CHECKED" "----------------------------------------------------------------------")
            locked = []
           # print("locked tetrolist :", self.locked_tetro)
            for i in range(len(self.locked_tetro)):
                rect, color = self.locked_tetro[i]
                #print("locked rect: ", rect)
                list3 = [item for item in rect if item not in completed_rows]
                #print("list3 :" , list3)
                locked.append((list3, color))
            #print("locked: ", locked)

            self.locked_tetro = locked
            return self.locked_tetro




    def update(self):
        global next_tetro
        self.create_grid()
        self.tetro_movement()
        self.create_locked_tetros()
        self.create_tetros()
        self.get_points()

    def main(self):
        clock.tick(3)
        for event in pygame.event.get():
            self.event_handler(event)

        self.update()
        self.render()
