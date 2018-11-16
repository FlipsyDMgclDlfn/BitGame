import pygame
from Bits.Bit import *

black = (0, 0, 0)
white = (255, 255, 255)


def main():
    pygame.init()
    GameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("BitGame")
    clock = pygame.time.Clock()
    gameOver = False
    down = False

    bits = []
    for i in range(0, 800):
        bits += [[]]
        for j in range(0, 600):
            bits[i] += [None]

    while not gameOver:
        GameDisplay.fill(black)
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                down = True
            if event.type == pygame.MOUSEBUTTONUP:
                down = False
        if down:
            if bits[mouse[0]][mouse[1]] is None:
                bits[mouse[0]][mouse[1]] = Bit(mouse[0], mouse[1], True, GameDisplay)
            #down = False

        for bitList in bits:
            for bit in bitList:
                if bit is not None:
                    if not bit.moved:
                        bit.show()
                        bit.tick(bits)
                        bit.moved = True
            for bit in bitList:
                if bit is not None:
                    bit.moved = False



        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()



