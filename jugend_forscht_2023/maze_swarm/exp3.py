import time

from grid import *
from jugend_forscht_2023.maze_swarm import utils
from robot import *
from maze_generator import *


ui_enabled = False
repeat = 100
x = 10
y = 10
# dijkstra enabled
for full_battery in list(range(x+y-2, 2*x*y-(x+y), 20)):
    reached_target = 0
    not_reached_target = 0
    for repetition in range(repeat):
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
                time.sleep(0.1)

        #print(r1.map)
        #print(r1.dijkstra(0, x * y - y - 1))

    print('DIJKSTRA ENABLED: maze size =', x, '*', y, '| full_battery =', full_battery, '| reached_target =', reached_target, '| not_reached_target =', not_reached_target, '| reached target(%) =', reached_target * 100 / (reached_target + not_reached_target), '| repeat =', repeat)

print('\n')
# dijkstra disabled
for full_battery in list(range(x+y-2, 2*x*y-(x+y), 20)):
    reached_target = 0
    not_reached_target = 0
    for repetition in range(repeat):
        g = utils.initialize_grid(x, y, remove_walls=0, num_chargers=1)
        r1, r2, r3, r4 = utils.initialize_robots(g, full_battery = full_battery)
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
                time.sleep(0.1)

        #print(r1.map)
        #print(r1.dijkstra(0, x * y - y - 1))

    print('DIJKSTRA DISABLED: maze size =', x, '*', y, '| full_battery =', full_battery, '| reached_target =', reached_target, '| not_reached_target =', not_reached_target, '| reached target(%) =', reached_target * 100 / (reached_target + not_reached_target), '| repeat =', repeat)


print('done')
input()
