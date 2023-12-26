import sys

sys.path.append('./')
import utils

# Hier wird der Unterschied des Batterieverbrauches zwischen kürzeste-Weg-an und kürzeste-Weg-aus beobachtet

ui_enabled = True
repeat = 500

# shortest path to battery disabled
for x, y in [(5 * i, 5 * i) for i in range(2, 9)]:
    total_reached_target = 0
    total_not_reached_target = 0
    for repetition in range(repeat):
        full_battery = x * y - 1
        g = utils.initialize_grid(x, y, remove_walls=0, num_chargers=1)
        robots = utils.initialize_robots(g, full_battery=full_battery, farthest=True)
        ui = None
        if ui_enabled:
            ui = utils.initialize_ui(g, robots)
        reached_target = utils.run_robots_reach_check(robots, ui)
        total_reached_target += reached_target
        total_not_reached_target += (len(robots) - reached_target)

    print('DIJKSTRA DISABLED: maze size =', x, '*', y, '| reached_target =', total_reached_target,
          '| not_reached_target =', total_not_reached_target, '| reached target(%) =',
          total_reached_target * 100 / (total_reached_target + total_not_reached_target), '| repeat =', repeat)

print('\n')

# shortest path to battery enabled
for x, y in [(5 * i, 5 * i) for i in range(2, 9)]:
    total_reached_target = 0
    total_not_reached_target = 0
    for repetition in range(repeat):
        full_battery = x * y - 1
        g = utils.initialize_grid(x, y, ui_enabled, remove_walls=0, num_chargers=1)
        robots = utils.initialize_robots(g, full_battery=full_battery, shortest_path=True, farthest=True)
        ui = None
        if ui_enabled:
            ui = utils.initialize_ui(g, robots)
        reached_target = utils.run_robots_reach_check(robots, ui)
        total_reached_target += reached_target
        total_not_reached_target += (len(robots) - reached_target)

    print('DIJKSTRA ENABLED: maze size =', x, '*', y, '| reached_target =', total_reached_target,
          '| not_reached_target =', total_not_reached_target, '| reached target(%) =',
          total_reached_target * 100 / (total_reached_target + total_not_reached_target), '| repeat =', repeat)

print('done')
input()
