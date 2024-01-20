import sys
sys.path.append('./')
import utils

# import matplotlib.pyplot as plt
# Hier wird geschaut, wie viel Batterie die Roboter brauchen, um einen x·y grossen Irrgarten zu durchqueren

ui_enabled = True
repeat = 1
full_battery = 1000


farthest = False
x = 10
y = 10
battery_usage = []
for i in range(repeat):
    g = utils.initialize_grid(x, y, remove_walls=10)
    robots = utils.initialize_robots(g, full_battery=full_battery, farthest=farthest)
    ui = None
    if ui_enabled:
        ui = utils.initialize_ui(g, robots)
    utils.run_robots_battery_check(robots, ui)
    for robot in robots:
        battery_usage.append(full_battery - robot.battery)


