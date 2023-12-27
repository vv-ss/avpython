import sys
sys.path.append('./')
import utils

ui_enabled = False
repeat = 500

# dijkstra enabled
for x, y in [(5 * i, 5 * i) for i in range(3, 9)]:
    total_reached_target = 0
    total_not_reached_target = 0
    for repetition in range(repeat):
        full_battery = x * y * 2 // 4 - 1
        g = utils.initialize_grid(x, y, remove_walls=0, num_chargers=1)
        robots = utils.initialize_robots(g, full_battery=full_battery, shortest_path=True)
        ui = None
        if ui_enabled:
            ui = utils.initialize_ui(g, robots)
        reached_target = utils.run_robots_reach_check(robots, ui, share_map=True)
        total_reached_target += reached_target
        total_not_reached_target += (len(robots) - reached_target)

    print('DIJKSTRA ENABLED: maze size =', x, '*', y, '| reached_target =', total_reached_target, '| not_reached_target =', total_not_reached_target, '| reached target(%) =', total_reached_target * 100 / (total_reached_target + total_not_reached_target), '| repeat =', repeat)

print('\n')


print('done')
input()
