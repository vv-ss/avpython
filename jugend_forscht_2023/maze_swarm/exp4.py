import time

from grid import *
from jugend_forscht_2023.maze_swarm import utils
from robot import *
from maze_generator import *

ui_enabled = False
repeat = 100


def get_share_map(robots):
    share_map = [set() for _ in range(max([len(r.map) for r in robots]))]
    for r in robots:
        for set_count in range(len(r.map)):
            share_map[set_count] = share_map[set_count].union(r.map[set_count])
    return share_map


# dijkstra enabled
for x, y in [(5 * i, 5 * i) for i in range(3, 9)]:
    reached_target = 0
    not_reached_target = 0
    for repetition in range(repeat):
        full_battery = x * y - 1
        g = utils.initialize_grid(x, y, remove_walls=0, num_chargers=1)
        r1, r2, r3, r4 = utils.initialize_robots(g, full_battery = full_battery, dijkstra_disabled=False)
        robots = [r1, r2, r3, r4]
        no_action = []

        if ui_enabled:
            g.draw_maze(g.connected_list)
            pygame.display.flip()

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
                    not_reached_target += 1
                if ui_enabled:
                    robot.draw_path()
                    robot.update_position()
            if ui_enabled:
                pygame.display.flip()

            #print('r1', r1.map)
            #print('r2', r2.map)
            #print('r3', r3.map)
            #print('r4', r4.map)
            #print('share_map:', get_share_map(robots))
            for r in robots:
                r.map = get_share_map(robots)

        #print(r1.dijkstra(0, x * y - y - 1))

    print('DIJKSTRA ENABLED: maze size =', x, '*', y, '| reached_target =', reached_target, '| not_reached_target =', not_reached_target, '| reached target(%) =', reached_target * 100 / (reached_target + not_reached_target), '| repeat =', repeat)

print('\n')


print('done')
input()
