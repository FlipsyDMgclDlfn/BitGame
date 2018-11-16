import pygame
from Bits.Bit import *

black = (0,0,0)
white = (255,255,255)


def main():
    pygame.init()
    GameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption("BitGame")
    clock = pygame.time.Clock()
    gameOver = False
    down = False

    bits = []

    while not gameOver:
        GameDisplay.fill((0,0,0))
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                down = True
            if event.type == pygame.MOUSEBUTTONUP:
                down = False
        if down:
            bits += [Bit(mouse[0], mouse[1], True, GameDisplay)]

        for bit in bits:
                bit.show()
                bit.tick()



        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()



