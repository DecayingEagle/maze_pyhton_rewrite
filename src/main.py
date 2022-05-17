from time import sleep
import pygame
import random

from game import Grid

WIDTH = HEIGHT = 700 # Window size
GRID_SIZE = 5

grid = Grid(GRID_SIZE)

def draw():
        for i in range (grid.grid_size + 2):
            for j in range (grid.grid_size + 2):

# TODO: Fix the bug where if the width and height are not divisible by the grid array size, the window will have lines that are not supposed to be there

                if grid.grid_arr[j][i] == 0:
                    # Background
                    pygame.draw.rect(win, (100, 100, 100), (j * WIDTH / (grid.grid_size + 2), i * HEIGHT / (grid.grid_size + 2), WIDTH / (grid.grid_size + 2), HEIGHT / (grid.grid_size + 2)))
                elif grid.grid_arr[i][j] == 1:
                    # Wall
                    pygame.draw.rect(win, (0, 0, 0), (j * WIDTH / (grid.grid_size + 2), i * HEIGHT / (grid.grid_size + 2), WIDTH / (grid.grid_size + 2), HEIGHT / (grid.grid_size + 2)))
                elif grid.grid_arr[i][j] == 2:
                    # Current position
                    pygame.draw.rect(win, (255, 0, 0), (j * WIDTH / (grid.grid_size + 2), i * HEIGHT / (grid.grid_size + 2), WIDTH / (grid.grid_size + 2), HEIGHT / (grid.grid_size + 2)))
                elif grid.grid_arr[i][j] == 3:
                    # Start position
                    pygame.draw.rect(win, (0, 255, 0), (j * WIDTH / (grid.grid_size + 2), i * HEIGHT / (grid.grid_size + 2), WIDTH / (grid.grid_size + 2), HEIGHT / (grid.grid_size + 2)))
                elif grid.grid_arr[i][j] == 4:
                    # End position
                    pygame.draw.rect(win, (0, 0, 255), (j * WIDTH / (grid.grid_size + 2), i * HEIGHT / (grid.grid_size + 2), WIDTH / (grid.grid_size + 2), HEIGHT / (grid.grid_size + 2)))
                pygame.display.update()

def loop():
    n = 0 # Number of iterations
    run = True
    while run:
        n += 1
        grid.generate()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    pygame.draw.rect(win,(0,0,255),(120,120,400,240))

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")

grid.pre_gen()
draw()
loop()
pygame.quit()
quit()
