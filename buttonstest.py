import pygame
import sys
from pygame.locals import *


x = 10
y = 10
width = 150
height = 200
from time import *
while True:
    surface = pygame.display.set_mode((800, 600))
    pygame.draw.rect(surface, (255,0,0), (x, y, width, height))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            if (x < pos[0] < x+width) and (y < pos[1] < y+height):
                print("Button clicked")

