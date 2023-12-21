import matplotlib.pyplot as plt
from jugend_forscht_2023.maze_swarm import utils

# Hier wird geschaut, wie viel Batterie die Roboter brauchen, um einen x·y großen Irrgarten zu durchqueren

ui_enabled = False
repeat = 500
full_battery = 10000
# FIRST CASE: DESTINATION IN OPPOSITE CORNER
for x, y in [(5*i, 5*i) for i in range(2, 41)]:
    battery_usage = []
    for i in range(repeat):
        g = utils.initialize_grid(x, y, ui_enabled, remove_walls=0)
        robots = utils.initialize_robots(g, full_battery=full_battery, farthest=True)
        utils.run_robots_battery_check(g, robots, ui_enabled)
        for robot in robots:
            battery_usage.append(full_battery - robot.battery)

    print('maze size =', x, '*', y, '| minimum battery usage =', min(battery_usage), '| maximum battery usage =', max(battery_usage), '| average battery usage =', sum(battery_usage) / len(battery_usage), '| repeat =', repeat)
    #plt.hist(battery_usage, 200)
    #plt.show()

# SECOND CASE: DESTINATION AT RANDOM POSITION
for x, y in [(5*i, 5*i) for i in range(2, 41)]:
    battery_usage = []
    for i in range(repeat):
        g = utils.initialize_grid(x, y, ui_enabled, remove_walls=0)
        robots = utils.initialize_robots(g, full_battery=full_battery, farthest=False)
        utils.run_robots_battery_check(g, robots, ui_enabled)
        for robot in robots:
            battery_usage.append(full_battery - robot.battery)

    print('maze size =', x, '*', y, '| minimum battery usage =', min(battery_usage), '| maximum battery usage =', max(battery_usage), '| average battery usage =', sum(battery_usage) / len(battery_usage), '| repeat =', repeat)
    #plt.hist(battery_usage, 200)
    #plt.show()

