# importing the required libraries
import pygame as pg
import sys
import time
from pygame.locals import *

# initializing the pygame window
pg.init()

screen = pg.display.set_mode((100, 100), 0, 32)

# setting up a nametag for the
# game window
pg.display.set_caption("My Tic Tac Toe")


while (True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            # checking if key "A" was pressed
            if event.key == pg.K_a:
                print("Key A has been pressed")

            # checking if key "J" was pressed
            if event.key == pg.K_j:
                print("Key J has been pressed")
    pg.display.update()

# Show input as "Do you want to move first (Y/N)?"