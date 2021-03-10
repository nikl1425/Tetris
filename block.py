import pygame
from collections import defaultdict
from random import randrange
from operator import add

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

L = [['.#..',
      '.#..',
      '.##.',
      '....'],
     ['....',
      '###.',
      '#...',
      '....'],
     ['.##.',
      '..#.',
      '..#.',
      '....'],
     ['....',
      '...#',
      '.###',
      '....']]
T = [['....',
      '###.',
      '.#..',
      '....'],
     ['.#..',
      '##..',
      '.#..',
      '....'],
     ['....',
      '.#..',
      '###.',
      '....'],
     ['.#..',
      '.##.',
      '.#..',
      '....']]
I = [['#...',
      '#...',
      '#...',
      '#...'],
     ['....',
      '####',
      '....',
      '....']]
O = [['....',
      '.##.',
      '.##.',
      '....']]
S = [['....',
      '..##',
      '.##.',
      '....'],
     ['.#..',
      '.##.',
      '..#.',
      '....']]

class Block:
    # Colors
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (51, 255, 51)
    pink = (204, 0, 204)
    yellow = (255, 255, 0)

    shapes = [L, T, I, O, S]
    shape_colors = [red, blue, green, pink, yellow]

    def __init__(self, size):
        self.size = size # make this as tuple
        self.rotation = 0
        self.currentblock = []
        self.pos = []
        self.shape = []


    def convert_shape_format(self, form):
        positions = []
        formats = form[self.rotation % len(form)]

        for i, line in enumerate(formats):
            row = list(line)
            for j, column in enumerate(row):
                if column == '#':
                    positions.append(list((j+3, i-4)))
                    self.pos = positions
        return positions

    def next_block(self):
        random_int = randrange(0, 5)
        picked_shape = self.shapes[random_int]
        index = self.shapes.index(picked_shape)
        self.shape = self.shapes[random_int]
        picked_color = self.shape_colors[index]
        return picked_color, picked_shape

    def create_block(self):
        block_color, self.current_block = self.next_block()
        current_block = self.convert_shape_format(self.shape)
        print("current - start: " , current_block)
        return current_block, block_color

    def rotate_block(self, shape):
        new_shape = self.convert_shape_format(self.current_block)
        x_values_in_shape = [x for (x,_) in (l for l in shape)]
        y_values_in_shape = [y for (_, y) in (i for i in shape)]
        x_low = self.my_min(x_values_in_shape)
        y_low = self.my_min(y_values_in_shape)
        new_list = []
        for element in new_shape:
            x, y = element
            x = x + x_low
            y = y + y_low
            new_list.append([x,y])
        return new_list


    def my_min(self, sequence):
        """return the minimum element of sequence"""
        low = sequence[0]  # need to start with some value
        for i in sequence:
            if i < low:
                low = i
        return low











