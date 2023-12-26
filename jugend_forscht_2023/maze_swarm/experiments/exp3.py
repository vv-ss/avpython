import sys
sys.path.append('./')
import utils

ui_enabled = True
repeat = 500
x = 15
y = 15

# shortest path to battery disabled
for full_battery in list(range(x + y - 2, 2 * x * y - (x + y), 20)):
    total_reached_target = 0
    total_not_reached_target = 0
    for repetition in range(repeat):
        g = utils.initialize_grid(x, y, remove_walls=0, num_chargers=1)
        robots = utils.initialize_robots(g, full_battery=full_battery)
        ui = None
        if ui_enabled:
            ui = utils.initialize_ui(g, robots)
        reached_target = utils.run_robots_reach_check(robots, ui)
        total_reached_target += reached_target
        total_not_reached_target += (len(robots) - reached_target)

        # print(r1.map)
        # print(r1.dijkstra(0, x * y - y - 1))

    print('DIJKSTRA DISABLED: maze size =', x, '*', y, '| full_battery =', full_battery, '| reached_target =',
          total_reached_target, '| not_reached_target =', total_not_reached_target, '| reached target(%) =',
          total_reached_target * 100 / (total_reached_target + total_not_reached_target), '| repeat =', repeat)

print('\n')

# shortest path to battery enabled
for full_battery in list(range(x + y - 2, 2 * x * y - (x + y), 20)):
    total_reached_target = 0
    total_not_reached_target = 0
    for repetition in range(repeat):
        g = utils.initialize_grid(x, y, remove_walls=0, num_chargers=1)
        robots = utils.initialize_robots(g, full_battery=full_battery, shortest_path=True)
        ui = None
        if ui_enabled:
            ui = utils.initialize_ui(g, robots)
        reached_target = utils.run_robots_reach_check(robots, ui)
        total_reached_target += reached_target
        total_not_reached_target += (len(robots) - reached_target)

    print('DIJKSTRA ENABLED: maze size =', x, '*', y, '| full_battery =', full_battery, '| reached_target =',
          total_reached_target, '| not_reached_target =', total_not_reached_target, '| reached target(%) =',
          total_reached_target * 100 / (total_reached_target + total_not_reached_target), '| repeat =', repeat)

print('done')
input()
