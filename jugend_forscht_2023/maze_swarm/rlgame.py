import utils

class Game:
    def __init__(self, x, y, ui_enabled, full_battery):
        self.grid = utils.initialize_grid(x, y, ui_enabled, remove_walls=0)
        self.robots = utils.initialize_robots(self.grid, full_battery=full_battery, farthest=True)

