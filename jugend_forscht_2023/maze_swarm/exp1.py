from grid import *
from robot import *
from maze_solver import *
from maze_generator import *
import matplotlib.pyplot as plt


ui_enabled = False
full_battery = 1000000
repeat = 1

for x, y in [(5*i, 5*i) for i in range(1, 41)]:
    battery_usage = []
    for i in range(repeat):
        g = Grid(x, y, 60, 60, 4, [200, 100, 200, 100], 50, 0)
        mg = MazeGenerator(g)
        s = MazeSolver(g, 'lhs')
        g.connected_list = mg.prim_algorithmus()

        r1 = Robot(g, s, (0, 0), (g.cells_y - 1, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/mouse.png'), 180, full_battery, g.pink, 1)
        r2 = Robot(g, s, (0, g.cells_x - 1), (g.cells_y - 1, 0), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/snail.png'), -90, full_battery, g.gruen, 2)
        r3 = Robot(g, s, (g.cells_y - 1, g.cells_x - 1), (0, 0), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/giraffe.png'), -90, full_battery, g.gelb, 3)
        r4 = Robot(g, s, (g.cells_y - 1, 0), (0, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/dog.png'), 90, full_battery, g.schwarz, 4)
        robots = [r1, r2, r3, r4]

        if ui_enabled:
            g.draw_maze(g.connected_list)
            pygame.display.flip()

        while r1.position != r1.target or r2.position != r2.target or r3.position != r3.target or r4.position != r4.target:
            if ui_enabled:
                g.draw_maze(g.connected_list)

            for robot in robots:
                robot.action()
                if ui_enabled:
                    robot.draw_path()
                    robot.update_position()
            if ui_enabled:
                pygame.display.flip()
        for robot in robots:
            battery_usage.append(full_battery - robot.battery)

    print('maze size =', x, '*', y, '| minimum battery usage =', min(battery_usage), '| maximum battery usage =', max(battery_usage), '| average battery usage =', sum(battery_usage) / len(battery_usage), '| repeat =', repeat)
    plt.hist(battery_usage, 200)
    plt.show()


print('done')
input()
