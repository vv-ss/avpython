import sys
sys.path.append('./')
import utils
import json
import time

load_number = 0
ui_enabled = True
num_chargers = 1
farthest = True
ff_demo = False
lhs_rhs_demo = False
share_map = True
step_time = 0.1
g = None

# IF LOAD NUMBER = 0
x = 10
y = 10
full_battery = 40
robots_algo = 'floofi'
remove_walls = 10
if load_number == 0 and robots_algo == 'floofi' and ff_demo:
    step_time = 1


def load_grid(maze_number):
    global full_battery, robots_algo
    mazes_file = open('maze_1.txt', 'r')
    lines = mazes_file.readlines()
    maze = lines[maze_number - 1].split(' | ')
    width, height = int(maze[0]), int(maze[1])
    robots_algo = maze[2]
    full_battery = int(maze[3])
    connected_list = json.loads(maze[4])
    return utils.generate_maze(width, height, connected_list, num_chargers)


def save_maze(g):
    width = g.cells_x
    height = g.cells_y
    cl = g.connected_list
    mazes_file = open('maze_1.txt', 'a')
    mazes_file.write(str(width) + ' | ' + str(height) + ' | ' + str(cl) + '\n')


if 0 < load_number < 27:
    g = load_grid(load_number)
else:
    g = utils.initialize_grid(x, y, remove_walls=remove_walls, num_chargers=num_chargers)

robots = utils.initialize_robots(g, full_battery=full_battery, farthest=farthest, robots_algo=robots_algo)
if ff_demo and robots_algo == 'floofi':
    robots = [robots[0]]
if lhs_rhs_demo and robots_algo == 'lhs_rhs':
    robots = [robots[0]]
ui = None
if ui_enabled:
    ui = utils.initialize_ui(g, robots, ff_demo=ff_demo)
    # time.sleep(100)
start = time.time()
utils.run_robots_reach_check(robots, ui, share_map=share_map, sleep_time=step_time)
print(time.time() - start)