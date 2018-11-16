import pygame

class Bit:

    def __init__(self, x, y, fall, display):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.fall = fall
        self.size = (1, 1)
        self.display = display

    def tick(self):
        if self.fall:
            self.dy += 1
        self.x += self.dx
        self.y += self.dy

    def show(self):
        pygame.draw.rect(self.display, (255,255,255), [self.x, self.y, self.size[0], self.size[1]])
