import time
import matplotlib.pyplot as plt
from jugend_forscht_2023.maze_swarm import utils
import pygame

ui_enabled = True

repeat = 100
full_battery = 10000
for x, y in [(5*i, 5*i) for i in range(2, 41)]:
    battery_usage = []
    for i in range(repeat):
        g = utils.initialize_grid(x, y, remove_walls=0)
        r1, r2, r3, r4 = utils.initialize_robots(g, full_battery = full_battery)

        if ui_enabled:
            g.draw_maze(g.connected_list)
            pygame.display.flip()

        while r1.position != r1.target or r2.position != r2.target or r3.position != r3.target or r4.position != r4.target:
            if ui_enabled:
                g.draw_maze(g.connected_list)

            for robot in [r1, r2, r3, r4]:
                robot.action()
                if ui_enabled:
                    robot.draw_path()
                    robot.update_position()
            if ui_enabled:
                pygame.display.flip()
                time.sleep(0.1)
        for robot in [r1, r2, r3, r4]:
            battery_usage.append(full_battery - robot.battery)

    print('maze size =', x, '*', y, '| minimum battery usage =', min(battery_usage), '| maximum battery usage =', max(battery_usage), '| average battery usage =', sum(battery_usage) / len(battery_usage), '| repeat =', repeat)
    plt.hist(battery_usage, 200)
    plt.show()


print('done')
input()
