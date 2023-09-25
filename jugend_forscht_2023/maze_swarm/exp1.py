from grid import *
from robot import *
from maze_solver import *
from maze_generator import *

ui_enabled = False
full_battery = 10000

for x, y in [(5*i, 10*i) for i in range(1, 20)]:
    batteries = []
    for i in range(100*x):
        g = Grid(x, y, 60, 60, 4, [200, 100, 200, 100], 50, 0)
        mg = MazeGenerator(g)
        s = MazeSolver(g, 'lhs')
        r1 = Robot(g, s, (0, 0), (g.cells_y - 1, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/mouse.png'), 180, full_battery, g.pink, 1)
        r2 = Robot(g, s, (0, g.cells_x - 1), (g.cells_y - 1, 0), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/snail.png'), -90, full_battery, g.gruen, 2)
        r3 = Robot(g, s, (g.cells_y - 1, g.cells_x - 1), (0, 0), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/giraffe.png'), -90, full_battery, g.gelb, 3)
        r4 = Robot(g, s, (g.cells_y - 1, 0), (0, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/dog.png'), 90, full_battery, g.schwarz, 4)
        robots = [r1, r2, r3, r4]

        g.connected_list = mg.prim_algorithmus()
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
            batteries.append(full_battery - robot.battery)

    print('maze size =', x, y, 'minimum = ', min(batteries), 'maximum = ', max(batteries), 'average = ', sum(batteries)/len(batteries))

print('done')
input()
