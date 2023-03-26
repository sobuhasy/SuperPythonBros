import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("SuperPythonBros")

BG_COLOR = (168, 241, 245)
WIDTH, HEIGHT = 1000, 800
FPS = 45
PLAYER_VEL = 4

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)