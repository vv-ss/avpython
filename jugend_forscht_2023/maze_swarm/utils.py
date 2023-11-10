from jugend_forscht_2023.maze_swarm.robot import *
from jugend_forscht_2023.maze_swarm.grid import *
from jugend_forscht_2023.maze_swarm.maze_generator import *
import pygame


def initialize_grid(width, height, ui_enabled=False, remove_walls=0, num_chargers=0):
    g = Grid(width, height, 60, 60, 4, [200, 100, 200, 100], 50, num_chargers)
    mg = MazeGenerator(g)
    g.connected_list = mg.prim_algorithmus()
    if remove_walls > 0:
        g.connected_list = mg.remove_walls(mg.prim_algorithmus(), remove_walls)
    if ui_enabled:
        g.draw_maze(g.connected_list)
        pygame.display.flip()
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

def get_share_map(robots):
    share_map = [set() for _ in range(max([len(r.map) for r in robots]))]
    for r in robots:
        for set_count in range(len(r.map)):
            share_map[set_count] = share_map[set_count].union(r.map[set_count])
    return share_map


def run_robots_battery_check(g, robots, ui_enabled=False, share_map=False):
    while True:
        reached_robots = [r for r in robots if r.position == r.target]
        if len(reached_robots) == len(robots):
            break
        if ui_enabled:
            g.draw_maze(g.connected_list)

        for robot in robots:
            robot.action()
            if ui_enabled:
                robot.draw_path()
                robot.update_position()
        if ui_enabled:
            pygame.display.flip()
            time.sleep(0.1)


def run_robots_reach_check(g, robots, ui_enabled=False, share_map=False):
    no_action = []
    reached_target = 0
    not_reached_target = 0
    while len(no_action) != len(robots):
        if ui_enabled:
            g.draw_maze(g.connected_list)
        for robot in [r for r in robots if r not in no_action]:
            a = robot.action()
            if a == 'reached_target':
                no_action.append(robot)
                reached_target += 1
            if a == 'battery_empty':
                no_action.append(robot)
            if ui_enabled:
                robot.draw_path()
                robot.update_position()
        if ui_enabled:
            pygame.display.flip()
        if share_map:
            for r in robots:
                r.map = get_share_map(robots)
    return reached_target
