import sys
sys.path.append('./')
import utils
# import matplotlib.pyplot as plt
# Hier wird geschaut, wie viel Batterie die Roboter brauchen, um einen x·y grossen Irrgarten zu durchqueren

ui_enabled = False
repeat = 1000
full_battery = 10000
# FIRST CASE: DESTINATION IN OPPOSITE CORNER
for x, y in [(5*i, 5*i) for i in range(2, 21)]:
    battery_usage = []
    for i in range(repeat):
        g = utils.initialize_grid(x, y, remove_walls=0)
        robots = utils.initialize_robots(g, full_battery=full_battery, farthest=True)
        ui = None
        if ui_enabled:
            ui = utils.initialize_ui(g, robots)
        utils.run_robots_battery_check(robots, ui)
        for robot in robots:
            battery_usage.append(full_battery - robot.battery)

    print('maze size =', x, '*', y, '| minimum battery usage =', min(battery_usage), '| maximum battery usage =', max(battery_usage), '| average battery usage =', sum(battery_usage) / len(battery_usage), '| repeat =', repeat)
    #plt.hist(battery_usage, 200)
    #plt.show()

# SECOND CASE: DESTINATION AT RANDOM POSITION
for x, y in [(5*i, 5*i) for i in range(2, 21)]:
    battery_usage = []
    for i in range(repeat):
        g = utils.initialize_grid(x, y, ui_enabled, remove_walls=0)
        robots = utils.initialize_robots(g, full_battery=full_battery, farthest=False)
        ui = None
        if ui_enabled:
            ui = utils.initialize_ui(g, robots)
        utils.run_robots_battery_check(robots, ui)
        for robot in robots:
            battery_usage.append(full_battery - robot.battery)

    print('maze size =', x, '*', y, '| minimum battery usage =', min(battery_usage), '| maximum battery usage =', max(battery_usage), '| average battery usage =', sum(battery_usage) / len(battery_usage), '| repeat =', repeat)
    #plt.hist(battery_usage, 200)
    #plt.show()

