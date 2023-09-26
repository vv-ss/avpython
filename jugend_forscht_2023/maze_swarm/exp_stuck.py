import time

from grid import *
from robot import *
from maze_solver import *
from maze_generator import *

ui_enabled = True


for x, y in [(5*i, 5*i) for i in range(5, 6)]:
    batteries = []
    reached_target = 0
    not_reached_target = 0
    for repetition in range(1):
        full_battery = x*y//25 - 2
        g = Grid(x, y, 60, 60, 4, [200, 100, 200, 100], 50, 20)
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
        no_action = []
        g.connected_list = mg.prim_algorithmus()
        if ui_enabled:
            g.draw_maze(g.connected_list)
            pygame.display.flip()

        while len(no_action) != len(robots):
            if ui_enabled:
                g.draw_maze(g.connected_list)
            for robot in [r for r in robots if r not in no_action]:
                a = robot.action()
                if a == 'reached_target':
                    no_action.append(robot)
                    reached_target += 1
                if a == 'battery_empty':
                    no_action.append(robot)
                    not_reached_target += 1
                if ui_enabled:
                    robot.draw_path()
                    robot.update_position()
            if ui_enabled:
                pygame.display.flip()
            if robots[0].batteries:
                time.sleep(1)

        print(r1.map)
        print(r1.dijkstra(0, x*y-y-1))

    print('maze size =', x, y, 'reached_target =', reached_target, 'not_reached_target =', not_reached_target)


print('done')
input()
