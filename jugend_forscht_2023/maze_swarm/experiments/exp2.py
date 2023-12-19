from jugend_forscht_2023.maze_swarm import utils
import pygame

# Hier wird der Unterschied des Batterieverbrauches zwischen kürzeste-Weg-an und kürzeste-Weg-aus beobachtet

ui_enabled = False
repeat = 100

# dijkstra disabled
for x, y in [(5 * i, 5 * i) for i in range(3, 9)]:
    total_reached_target = 0
    total_not_reached_target = 0
    for repetition in range(repeat):
        full_battery = x * y - 1
        g = utils.initialize_grid(x, y, remove_walls=0, num_chargers=1)
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
                    total_reached_target += 1
                if a == 'battery_empty':
                    no_action.append(robot)
                    total_not_reached_target += 1
                if ui_enabled:
                    robot.draw_path()
                    robot.update_position()
            if ui_enabled:
                pygame.display.flip()

        # print(r1.map)
        # print(r1.dijkstra(0, x * y - y - 1))

    print('DIJKSTRA DISABLED: maze size =', x, '*', y, '| reached_target =', total_reached_target,
          '| not_reached_target =', total_not_reached_target, '| reached target(%) =',
          total_reached_target * 100 / (total_reached_target + total_not_reached_target), '| repeat =', repeat)

print('\n')

# dijkstra enabled
for x, y in [(10 * i, 10 * i) for i in range(1, 9)]:
    total_reached_target = 0
    total_not_reached_target = 0
    for repetition in range(repeat):
        full_battery = x * y - 1
        g = utils.initialize_grid(x, y, remove_walls=0, num_chargers=1)
        robots = utils.initialize_robots(g, full_battery=full_battery, dijkstra_disabled=False)
        reached_target = utils.run_robots_reach_check(g, robots, ui_enabled)
        total_reached_target += reached_target
        total_not_reached_target += (len(robots) - reached_target)

    print('DIJKSTRA ENABLED: maze size =', x, '*', y, '| reached_target =', total_reached_target,
          '| not_reached_target =', total_not_reached_target, '| reached target(%) =',
          total_reached_target * 100 / (total_reached_target + total_not_reached_target), '| repeat =', repeat)

print('done')
input()
