import sys
import time

import pygame

sys.path.append('./')
import utils
import tensorflow as tf
from tensorflow import keras

GAME_ACTIONS = 4

tf.keras.backend.set_floatx('float32')
HIDDEN_STATES = 16

'''
We will use 2 Neural Networks for the algorithm implementation.
Note that can be also implemented as one single network sharing the same weights that will produce two outputs.
Also, often there is the usage of a CNN (Convolutional Neural Network) architecture in order to deal with the dynamic pixels of the game directly.
'''


class PolicyP(keras.Model):
    '''
    The Policy Neural Network will approximate the MCTS policy for the choice of nodes, given a State of the game.
    '''

    def __init__(self):
        super(PolicyP, self).__init__()

        self.dense1 = keras.layers.Dense(HIDDEN_STATES,
                                         activation='relu',
                                         kernel_initializer=keras.initializers.he_normal(),
                                         name='dense_1')

        self.dense2 = keras.layers.Dense(HIDDEN_STATES,
                                         activation='relu',
                                         kernel_initializer=keras.initializers.he_normal(),
                                         name='dense_2')

        self.p_out = keras.layers.Dense(GAME_ACTIONS,
                                        activation='softmax',
                                        kernel_initializer=keras.initializers.he_normal(),
                                        name='p_out')

    def call(self, input):
        x = self.dense1(input)
        x = self.dense2(x)
        x = self.p_out(x)

        return x


ui_enabled = True
num_chargers = 1
farthest = True
share_map = True
step_time = 0.1
g = None

# IF LOAD NUMBER = 0
x = 10
y = 10
full_battery = x * y
low_battery = full_battery / 4
robots_algo = 'lhs_rhs'
remove_walls = 10


def get_obs(robots, time_elapsed):
    obs = []
    for r in robots:
        # obs.append(r.position[0])
        # obs.append(r.position[1])
        obs.append(r.battery / r.full_battery)
    obs.append(time_elapsed / 100)
    return obs


def run_robots_alpha_zero(robots, ui, sleep_time):
    reached_robots = set()
    not_reached_robots = set()
    reward = 0
    policy_p = PolicyP()
    policy_p.compile(optimizer=keras.optimizers.Adam(),
                     loss=tf.keras.losses.CategoricalCrossentropy(),
                     metrics=[tf.keras.metrics.CategoricalCrossentropy()])
    policy_p.load_weights('policy')
    time_elapsed = 0

    while len(not_reached_robots) + len(reached_robots) < len(robots):
        if ui:
            ui.draw_maze()
        state = get_obs(robots, time_elapsed)
        action = policy_p(state)
        time_elapsed += 1
        for robot in robots:
            if robot.id == 0 and (action == 0 or action == 2):
                robot.action(True)
            elif robot.id == 1 and (action == 0 or action == 1):
                robot.action(True)
            else:
                robot.action(False)
                while robot.turn_angle != 0:
                    if robot.battery <= 0:
                        break
            if robot.position == robot.target and robot.id not in reached_robots:
                print("robot ", robot.id, " reached at time = ", time_elapsed)
                reached_robots.add(robot.id)
            if robot.battery_empty:
                if robot.id not in reached_robots and robot.id not in not_reached_robots:
                    not_reached_robots.add(robot.id)
            if ui:
                ui.draw_path(robot)
                ui.update_position(robot)
        if ui:
            pygame.display.flip()
            time.sleep(sleep_time)
        for r in robots:
            r.map = utils.get_share_map(robots)
    return reward


g = utils.initialize_grid(x, y, remove_walls=remove_walls, num_chargers=num_chargers)
robots = utils.initialize_robots(g, full_battery=full_battery, farthest=farthest, robots_algo=robots_algo)
robots[0].battery = low_battery
robots[1].battery = low_battery

ui = utils.initialize_ui(g, robots)
start = time.time()
run_robots_alpha_zero(robots, ui, sleep_time=step_time)
print(time.time() - start)

