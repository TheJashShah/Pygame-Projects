import pygame

class Text:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.font = pygame.font.Font("Pygame-Projects/Cellular-Automata/assets/font.ttf", 25)

        self.color = (255, 255, 255)

    def draw(self, win):

        text = self.font.render(format(self.value), True, self.color)
        win.blit(text, (self.x, self.y))