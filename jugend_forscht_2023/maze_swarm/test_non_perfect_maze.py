import pygame as pygame

from grid import *
from maze_generator import *

x, y = 20, 20
g = Grid(x, y, 60, 60, 4, [200, 100, 200, 100], 50, 0)
mg = MazeGenerator(g)
g.connected_list = mg.remove_walls(mg.prim_algorithmus(), 100)

g.draw_maze(g.connected_list)
pygame.display.flip()

input()
