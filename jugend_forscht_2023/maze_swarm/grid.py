import pygame
import random


class Grid:
    def __init__(self, cells_x, cells_y, num_chargers):
        self.cells_x = cells_x
        self.cells_y = cells_y
        self.cell_number = self.cells_x * self.cells_y
        self.connected_list = [[] for _ in range(self.cell_number)]
        if num_chargers == 1:
            self.chargers = [self.cells_y // 2 * self.cells_x + self.cells_x // 2]
        else:
            self.chargers = random.sample(range(1, self.cells_x * self.cells_y), num_chargers)


    def get_id(self, coordinates):
        return coordinates[0] * self.cells_x + coordinates[1]

    def umrechnen(self, id):
        return id // self.cells_x, id % self.cells_x

    def search_neighbor(self, cell):
        (reihe, spalte) = self.umrechnen(cell)
        neighbor = [(reihe - 1, spalte), (reihe, spalte + 1), (reihe + 1, spalte), (reihe, spalte - 1)]
        return [self.get_id((r, s)) for (r, s) in neighbor if 0 <= r < self.cells_y and 0 <= s < self.cells_x]


