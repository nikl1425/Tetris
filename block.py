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

    def convert_block(self):
        coordinates = []
        coordinates_dic = {}
        data_dict = defaultdict(list)
        for char in self.L:
            result = findOccurrences(char, '#')
            coordinates.append(result)
            print(coordinates)

        for index, element in enumerate(coordinates):
            if len(element) > 1:
                B, C = split_list(element)
                data_dict[index].append({index : B})
                data_dict[index].append({index : C})
            else:
                data_dict[index].append(index )

        print(data_dict.items())





blob = Block(29)

print(blob.convert_block())

