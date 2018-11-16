import pygame

class Bit:

    def __init__(self, x, y, fall, display, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.fall = fall
        self.size = (1, 1)
        self.display = display
        self.color = color
        self.moved = False

    def tick(self, bits):
        bits[self.x][self.y] = None
        if self.fall:
            self.dy += 1
        self.x += self.dx
        self.y += self.dy
        if self.y >= 600 - self.size[1]:
            self.y = 600 - self.size[1]
            self.dy = 0
            if self.x < 0:
                self.x = 0
                self.dx = 0
            if self.x > 800 - self.size[0]:
                self.x = 800 - self.size[0]
                self.dx = 0

        while bits[self.x][self.y] is not None:
            self.y -= 1
            self.dy = 0

        bits[self.x][self.y] = self




    def show(self):
        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.size[0], self.size[1]])
