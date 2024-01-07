import sys
import time

sys.path.append('./')
from robot import *
from grid import *
from maze_generator import *
from ui import *
import pygame


def initialize_grid(width, height, remove_walls=0, num_chargers=0):
    g = Grid(width, height, num_chargers)
    mg = MazeGenerator(g)
    g.connected_list = mg.prim_algorithmus()
    if remove_walls > 0:
        g.connected_list = mg.remove_walls(mg.prim_algorithmus(), remove_walls)
    return g


def initialize_robots(g, full_battery, robots_algo=None, shortest_path=False, farthest=True):
    if robots_algo is None:
        robots_algo = ['lhs', 'lhs', 'rhs', 'lhs']
    if robots_algo == 'floofi':
        robots_algo = ['floofi', 'floofi', 'floofi', 'floofi']
    srcs = [(0, 0), (0, g.cells_x - 1), (g.cells_y - 1, g.cells_x - 1), (g.cells_y - 1, 0)]
    if farthest:
        targets = [(g.cells_y - 1 - y, g.cells_x - 1 - x) for (y, x) in srcs]
    else:
        targets = [(random.randint(0, g.cells_y - 1), random.randint(0, g.cells_x - 1)) for i in range(0, 4)]
    r1 = Robot(g, robots_algo[0], srcs[0], targets[0], 2, full_battery, 0, shortest_path)
    r2 = Robot(g, robots_algo[1], srcs[1], targets[1], 3, full_battery, 1, shortest_path)
    r3 = Robot(g, robots_algo[2], srcs[2], targets[2], 0, full_battery, 2, shortest_path)
    r4 = Robot(g, robots_algo[3], srcs[3], targets[3], 0, full_battery, 3, shortest_path)
    return [r1, r2, r3, r4]


def initialize_ui(g: Grid, robots, ff_demo=False):
    ui = UI(g, 50, 60, 60, 4, [200, 100, 200, 100], robots, ff_demo)
    ui.draw_maze()
    for robot in robots:
        ui.update_position(robot)
    pygame.display.flip()
    return ui


def get_share_map(robots):
    share_map = [set() for _ in range(max([len(r.map) for r in robots]))]
    for r in robots:
        for set_count in range(len(r.map)):
            share_map[set_count] = share_map[set_count].union(r.map[set_count])
    return share_map


def run_robots_battery_check(robots, ui):
    while True:
        reached_robots = [r for r in robots if r.has_reached_target]
        if len(reached_robots) == len(robots):
            break
        if ui:
            ui.draw_maze()

        for robot in robots:
            # IF THE ROBOT HAS ALREADY REACHED TARGET, MAKE IT WAIT TO HAVE CORRECT BATTERY CALCULATION
            robot.action(robot.position == robot.target)
            if ui:
                ui.draw_path(robot)
                ui.update_position(robot)
        if ui:
            pygame.display.flip()
            if ui.ff_demo:
                time.sleep(2)
            else:
                time.sleep(0.1)


def run_robots_reach_check(robots, ui, share_map=False):
    reached_robots = set()
    not_reached_robots = set()
    while len(not_reached_robots) + len(reached_robots) < len(robots):
        if ui:
            ui.draw_maze()
        for robot in robots:
            robot.action()
            if robot.position == robot.target:
                reached_robots.add(robot.id)
            if robot.battery_empty:
                if robot.id not in reached_robots:
                    not_reached_robots.add(robot.id)
            if ui:
                ui.draw_path(robot)
                ui.update_position(robot)
        if ui:
            pygame.display.flip()
            time.sleep(0.1)
        if share_map:
            for r in robots:
                r.map = get_share_map(robots)
    return len(reached_robots)


def run_robots_calculate_reward(robots, ui, timeout, share_map=False):
    reached_robots = set()
    not_reached_robots = set()
    time_elapsed = 0
    reward = 0
    while len(not_reached_robots) + len(reached_robots) < len(robots):
        if ui:
            ui.draw_maze()
        time_elapsed += 1
        for robot in robots:
            robot.action()
            if robot.position == robot.target and robot.id not in reached_robots:
                print("robot ", robot.id, " reached at time = ", time_elapsed)
                reached_robots.add(robot.id)
                reward += 10
                reward += timeout - time_elapsed
            if robot.battery_empty:
                if robot.id not in reached_robots and robot.id not in not_reached_robots:
                    not_reached_robots.add(robot.id)
                    reward -= 25
            if ui:
                ui.draw_path(robot)
                ui.update_position(robot)
        if ui:
            pygame.display.flip()
            time.sleep(0.1)
        if share_map:
            for r in robots:
                r.map = get_share_map(robots)
    return reward
