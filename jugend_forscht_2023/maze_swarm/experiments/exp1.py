import matplotlib.pyplot as plt
from jugend_forscht_2023.maze_swarm import utils

ui_enabled = True
repeat = 100
full_battery = 10000
for x, y in [(5*i, 5*i) for i in range(2, 41)]:
    battery_usage = []
    for i in range(repeat):
        g = utils.initialize_grid(x, y, remove_walls=0)
        robots = utils.initialize_robots(g, full_battery = full_battery)
        utils.run_robots_battery_check(g, robots, ui_enabled)
        for robot in robots:
            battery_usage.append(full_battery - robot.battery)

    print('maze size =', x, '*', y, '| minimum battery usage =', min(battery_usage), '| maximum battery usage =', max(battery_usage), '| average battery usage =', sum(battery_usage) / len(battery_usage), '| repeat =', repeat)
    plt.hist(battery_usage, 200)
    plt.show()

print('done')
input()
