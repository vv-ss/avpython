import time

from grid import *
from robot import *
from maze_generator import *

ui_enabled = False
repeat = 100

# dijkstra enabled
for x, y in [(10 * i, 10 * i) for i in range(1, 9)]:
    reached_target = 0
    not_reached_target = 0
    for repetition in range(repeat):
        full_battery = x * y - 1
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

        #print(r1.map)
        #print(r1.dijkstra(0, x * y - y - 1))

    print('DIJKSTRA ENABLED: maze size =', x, '*', y, '| reached_target =', reached_target, '| not_reached_target =', not_reached_target, '| reached target(%) =', reached_target * 100 / (reached_target + not_reached_target), '| repeat =', repeat)

print('\n')
# dijkstra disabled
for x, y in [(10 * i, 10 * i) for i in range(1, 9)]:
    reached_target = 0
    not_reached_target = 0
    for repetition in range(repeat):
        full_battery = x * y - 1
        g = Grid(x, y, 60, 60, 4, [200, 100, 200, 100], 50, 1)
        mg = MazeGenerator(g)
        s = MazeSolver(g, 'lhs')
        r1 = Robot(g, s, (0, 0), (g.cells_y - 1, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/mouse.png'), 180, full_battery, g.pink, 1, dijkstra_disabled=True)
        r2 = Robot(g, s, (0, g.cells_x - 1), (g.cells_y - 1, 0), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/snail.png'), -90, full_battery, g.gruen, 2, dijkstra_disabled=True)
        r3 = Robot(g, s, (g.cells_y - 1, g.cells_x - 1), (0, 0), g.cell_width * 0.8, g.cell_width * 0.8,
                   pygame.image.load('img/giraffe.png'), -90, full_battery, g.gelb, 3, dijkstra_disabled=True)
        r4 = Robot(g, s, (g.cells_y - 1, 0), (0, g.cells_x - 1), g.cell_width * 0.8, g.cell_width * 0.8,
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

        #print(r1.map)
        #print(r1.dijkstra(0, x * y - y - 1))

    print('DIJKSTRA DISABLED: maze size =', x, '*', y, '| reached_target =', reached_target, '| not_reached_target =', not_reached_target, '| reached target(%) =', reached_target * 100 / (reached_target + not_reached_target), '| repeat =', repeat)


print('done')
input()
