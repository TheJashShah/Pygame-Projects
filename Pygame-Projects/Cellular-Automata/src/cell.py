import pygame

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width, self.height = 15, 15
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.dead = True
        self.black_color = (0, 0, 0)
        self.white_color = (255, 255, 255)

    def draw(self, win):

        if self.dead:
            color = self.black_color
        else:
            color = self.white_color

        pygame.draw.rect(win, (240, 240, 240), pygame.Rect(self.x - 1, self.y - 1, self.width + 2, self.height + 2), 1, 1, 1, 1)
        pygame.draw.rect(win, color, self.rect)
       