import pygame


class Button:
    pygame.font.init()
    font = pygame.font.SysFont('arial', 25)
    black = (0, 0, 0)

    def __init__(self, x, y, width, height, color, hover_color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = (x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text

    def draw(self, window):
        mouse_PosX, mouse_PosY = pygame.mouse.get_pos()
        pygame.draw.rect(window, self.color, self.size)
        if self.x < mouse_PosX < (self.x + self.width) and self.y < mouse_PosY < (self.y + self.height):
            pygame.draw.rect(window, self.hover_color, self.size)
        window.blit(self.font.render(self.text, True, self.black), (self.x, self.y))

    def check_hover(self):
        mouse_PosX, mouse_PosY = pygame.mouse.get_pos()
        if self.x < mouse_PosX < (self.x + self.width):
            if self.y < mouse_PosY < (self.y + self.height):
                return True
        return False


# print(pygame.font.get_fonts())



