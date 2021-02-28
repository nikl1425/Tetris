import pygame
from collections import defaultdict


def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

class Block:

    L = ['.#..',
         '.#..',
         '.##.']

    def __init__(self, size):
        self.size = size
        self.color = 0
        self.rotation = 0
        self.x = []
        self.y = []




    def convert_shape_format(self):
        positions = []
        format = self.L

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '#':
                    positions.append(list((j, i)))
                    print(positions)

        return positions











blob = Block(29)

blob.convert_shape_format()

