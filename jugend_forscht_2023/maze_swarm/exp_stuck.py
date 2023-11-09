import time

from grid import *
from jugend_forscht_2023.maze_swarm import utils
from robot import *
from maze_generator import *

ui_enabled = True


for x, y in [(5*i, 5*i) for i in range(5, 6)]:
    batteries = []
    reached_target = 0
    not_reached_target = 0
    for repetition in range(1):
        full_battery = x*y//25 - 2
        g = utils.initialize_grid(x, y, remove_walls=0, num_chargers=20)
        r1, r2, r3, r4 = utils.initialize_robots(g, full_battery=full_battery)
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
            if robots[0].batteries:
                time.sleep(0.1)

        print(r1.map)
        print(r1.dijkstra(0, x*y-y-1))

    print('maze size =', x, y, 'reached_target =', reached_target, 'not_reached_target =', not_reached_target)


print('done')
input()
