import pygame

class Button:
    def __init__(self, x, y, width, height, color, hover_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = (x, y, width, height)
        self.color = color
        self.hover_color = hover_color


    def draw(self, window):
        mouse_PosX, mouse_PosY = pygame.mouse.get_pos()
        pygame.draw.rect(window, self.color, self.size)
        if self.x < mouse_PosX < (self.x + self.width) and self.y < mouse_PosY < (self.y + self.height):
            pygame.draw.rect(window, self.hover_color, self.size)




