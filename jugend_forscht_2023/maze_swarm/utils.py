from robot import *
from grid import *
from maze_generator import *
import pygame


def initialize_grid(width, height, remove_walls=0, num_chargers=0):
    g = Grid(width, height, 60, 60, 4, [200, 100, 200, 100], 50, num_chargers)
    mg = MazeGenerator(g)
    g.connected_list = mg.prim_algorithmus()
    if remove_walls > 0:
        g.connected_list = mg.remove_walls(mg.prim_algorithmus(), remove_walls)
    return g


def initialize_robots(g, full_battery, dijkstra_disabled=True):
    r1 = Robot(g, 'lhs', (0, 0), (g.cells_y - 1, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
               pygame.image.load('img/mouse.png'), 2, 0, full_battery, g.pink, 1, dijkstra_disabled)
    r2 = Robot(g, 'lhs', (0, g.cells_x - 1), (g.cells_y - 1, 0), g.cell_width * 0.8, g.cell_width * 0.8,
               pygame.image.load('img/snail.png'), 3, 0, full_battery, g.gruen, 2, dijkstra_disabled)
    r3 = Robot(g, 'rhs', (g.cells_y - 1, g.cells_x - 1), (0, 0), g.cell_width * 0.8, g.cell_width * 0.8,
               pygame.image.load('img/giraffe.png'), 0, -90, full_battery, g.gelb, 3, dijkstra_disabled)
    r4 = Robot(g, 'lhs', (g.cells_y - 1, 0), (0, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
               pygame.image.load('img/dog.png'), 0, 90, full_battery, g.schwarz, 4, dijkstra_disabled)
    return r1, r2, r3, r4

