import sys


sys.path.append('./')
import utils
# import matplotlib.pyplot as plt
# hier wird geschaut, wie viel Batterie die Roboter brauchen, um einen x·y grossen Irrgarten zu durchqueren

ui_enabled = False
repeat = 100
full_battery = 10000

demo=False
# FIRST CASE: DESTINATION IN RANDOM POSITION, PERFECT MAZE
for x, y in [(5 * i, 5 * i) for i in range(2, 9)]:
    battery_usage_ff = []
    for i in range(repeat):
        g = utils.initialize_grid(x, y, remove_walls=0)
        robots_ff = utils.initialize_robots(g, full_battery=full_battery, robots_algo='floofi', farthest=False)
        if demo:
            robots = [robots[0]]
        ui = None
        if ui_enabled:
            ui = utils.initialize_ui(g, robots_ff, False)
        utils.run_robots_battery_check(robots_ff, ui)
        for robot in robots_ff:
            battery_usage_ff.append(full_battery - robot.battery)

    print('FLOOD FILL maze size =', x, '*', y, '| minimum battery usage =', min(battery_usage_ff), '| maximum battery usage =',
          max(battery_usage_ff), '| average battery usage =', sum(battery_usage_ff) / len(battery_usage_ff), '| repeat =',
          repeat)

# SECOND CASE: DESTINATION AT RANDOM POSITION, 1/5 WALLS DOWN
for x, y in [(5 * i, 5 * i) for i in range(2, 9)]:
    battery_usage = []
    for i in range(repeat):
        g = utils.initialize_grid(x, y, remove_walls=x*y//5)
        robots = utils.initialize_robots(g, full_battery=full_battery, robots_algo='floofi', farthest=False)
        ui = None
        if ui_enabled:
            ui = utils.initialize_ui(g, robots)
        utils.run_robots_battery_check(robots, ui)
        for robot in robots:
            battery_usage.append(full_battery - robot.battery)

    print('maze size =', x, '*', y, '| minimum battery usage =', min(battery_usage), '| maximum battery usage =',
          max(battery_usage), '| average battery usage =', sum(battery_usage) / len(battery_usage), '| repeat =',
          repeat)

