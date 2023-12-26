import utils
import robot

class Game:
    def __init__(self, grid, full_battery):
        self.full_battery = full_battery
        self.timeout = full_battery * 2
        self.robots = utils.initialize_robots(grid, full_battery=full_battery, farthest=True)
        self.reached_robots = []
        self.empty_robots = []

    def step(self, action):
        # action can take value of 0, 1, 2, 3.
        # action means how many robots are supposed to wait in a given move.
        reward = 0
        if self.timeout == 0:
            for r in self.robots:
                if not r.has_reached_target and r.id not in self.empty_robots:
                    reward -= 25
            return self.get_obs(), reward, False, True
        self.timeout -= 1
        if len(self.reached_robots) + len(self.empty_robots) == len(self.robots):
            return self.get_obs(), reward, True, True
        #self.robots.sort(key=lambda element: element.battery)
        for robot in self.robots:
            if action % 2 == 1:
                robot.action(True)
            else:
                robot.action(False)
                #print(robot.id, robot.turn_angle, robot.position)
                while robot.turn_angle != 0:
                    if robot.battery <= 0:
                        break
                    robot.action(False)
            if robot.has_reached_target and robot.id not in self.reached_robots:
                reward += 10
                #print("robot reached", robot.id, " reach set = ", self.reached_robots, " empty = ", self.empty_robots)
                self.reached_robots.append(robot.id)
            elif robot.battery_empty and robot.id not in self.reached_robots and robot.id not in self.empty_robots:
                self.empty_robots.append(robot.id)
                reward += -25
            action >>= 1
            # ALWAYS SHARE MAP!
        for r in self.robots:
            r.map = utils.get_share_map(self.robots)
        if len(self.reached_robots) + len(self.empty_robots) == len(self.robots):
            return self.get_obs(), reward, True, True
        else:
            return self.get_obs(), reward, False, False

    def reset(self, grid):
        self.robots = utils.initialize_robots(grid, full_battery=self.full_battery)
        self.reached_robots = []
        self.empty_robots = []
        self.timeout = self.full_battery * 2
        return self.get_obs()

    def get_obs(self):
        obs = []
        for r in self.robots:
            obs.append(r.position[0])
            obs.append(r.position[1])
            obs.append(r.battery)
        obs.append(len(self.reached_robots))
        obs.append(len(self.empty_robots))
        obs.append(self.timeout)
        return obs

    def close(self):
        self.robots = []
        self.empty_robots = []
        self.reached_robots = []
