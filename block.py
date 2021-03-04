import pygame
from collections import defaultdict
from random import randrange


def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


class Block:

    L = ['.#..',
         '.#..',
         '.##.',
         '....']
    T = ['....',
         '###.',
         '.#..',
         '....']
    I = ['#...',
         '#...',
         '#...',
         '#...']
    O = ['....',
         '.##.',
         '.##.',
         '....']
    S = ['....',
         '..##',
         '.##.',
         '....']

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
        self.color = self.black
        self.rotation = 0


    def convert_shape_format(self, form):
        positions = []

        for i, line in enumerate(form):
            row = list(line)
            for j, column in enumerate(row):
                if column == '#':
                    positions.append(list((j, i)))
                    #print(positions)

        return positions

    def next_block(self):
        random_int = randrange(0, 5)
        picked_shape = self.shapes[random_int]
        index = self.shapes.index(picked_shape)
        picked_color = self.shape_colors[index]
        return picked_color, picked_shape

    def create_block(self):
        block_color, current_block = self.next_block()
        current_block = self.convert_shape_format(current_block)
        #print(current_block)

        return current_block, block_color





blob = Block(29)

blob.create_block()

