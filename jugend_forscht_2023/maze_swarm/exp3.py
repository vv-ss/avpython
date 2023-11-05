import time

from grid import *
from robot import *
from maze_generator import *


ui_enabled = False
repeat = 200
x = 10
y = 10
# dijkstra enabled
for full_battery in list(range(x+y-2, 2*x*y-(x+y), 20)):
    reached_target = 0
    not_reached_target = 0
    for repetition in range(repeat):
        g = Grid(x, y, 60, 60, 4, [200, 100, 200, 100], 50, 1)
        mg = MazeGenerator(g)
        g.connected_list = mg.prim_algorithmus()

        r1 = Robot(g, 'lhs', (0, 0), (g.cells_y - 1, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/mouse.png'), 180, full_battery, g.pink, 1, dijkstra_disabled=False)
        r2 = Robot(g, 'lhs', (0, g.cells_x - 1), (g.cells_y - 1, 0), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/snail.png'), -90, full_battery, g.gruen, 2, dijkstra_disabled=False)
        r3 = Robot(g, 'lhs', (g.cells_y - 1, g.cells_x - 1), (0, 0), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/giraffe.png'), -90, full_battery, g.gelb, 3, dijkstra_disabled=False)
        r4 = Robot(g, 'lhs', (g.cells_y - 1, 0), (0, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/dog.png'), 90, full_battery, g.schwarz, 4, dijkstra_disabled=False)
        robots = [r1, r2, r3, r4]
        no_action = []
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
                time.sleep(0.1)

        #print(r1.map)
        #print(r1.dijkstra(0, x * y - y - 1))

    print('DIJKSTRA ENABLED: maze size =', x, '*', y, '| full_battery =', full_battery, '| reached_target =', reached_target, '| not_reached_target =', not_reached_target, '| reached target(%) =', reached_target * 100 / (reached_target + not_reached_target), '| repeat =', repeat)

print('\n')
# dijkstra disabled
for full_battery in list(range(x+y-2, 2*x*y-(x+y), 20)):
    reached_target = 0
    not_reached_target = 0
    for repetition in range(repeat):
        g = Grid(x, y, 60, 60, 4, [200, 100, 200, 100], 50, 1)
        mg = MazeGenerator(g)
        r1 = Robot(g, 'lhs', (0, 0), (g.cells_y - 1, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/mouse.png'), 180, full_battery, g.pink, 1, dijkstra_disabled=True)
        r2 = Robot(g, 'lhs', (0, g.cells_x - 1), (g.cells_y - 1, 0), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/snail.png'), -90, full_battery, g.gruen, 2, dijkstra_disabled=True)
        r3 = Robot(g, 'lhs', (g.cells_y - 1, g.cells_x - 1), (0, 0), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/giraffe.png'), -90, full_battery, g.gelb, 3, dijkstra_disabled=True)
        r4 = Robot(g, 'lhs', (g.cells_y - 1, 0), (0, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/dog.png'), 90, full_battery, g.schwarz, 4, dijkstra_disabled=True)
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
                time.sleep(0.1)

        #print(r1.map)
        #print(r1.dijkstra(0, x * y - y - 1))

    print('DIJKSTRA DISABLED: maze size =', x, '*', y, '| full_battery =', full_battery, '| reached_target =', reached_target, '| not_reached_target =', not_reached_target, '| reached target(%) =', reached_target * 100 / (reached_target + not_reached_target), '| repeat =', repeat)


print('done')
input()
