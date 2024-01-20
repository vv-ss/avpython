import random
import time

import pygame


class MazeGenerator:
    def __init__(self, grid):
        self.grid = grid
        self.starting_point = None

    def search_visited_neighbors(self, position, visited):
        neighbors = self.grid.search_neighbor(position)
        return [neighbor for neighbor in neighbors if neighbor in visited]

    def search_unvisited_neighbors(self, position, visited):
        neighbors = self.grid.search_neighbor(position)
        return [neighbor for neighbor in neighbors if neighbor not in visited]

    def prim_algorithmus(self):
        self.starting_point = random.randint(0, self.grid.cell_number - 1)
        visited = [self.starting_point]
        frontier = self.grid.search_neighbor(self.starting_point)
        cl = [[] for _ in range(self.grid.cell_number)]
        while frontier:
            position = frontier.pop(random.randint(0, len(frontier) - 1))
            if position in visited:
                continue
            visited_neighbors = self.search_visited_neighbors(position, visited)
            random_cell = random.choice(visited_neighbors)
            cl[position].append(random_cell)
            cl[random_cell].append(position)
            visited.append(position)
            resulting_neighbors = self.search_unvisited_neighbors(position, visited)
            if resulting_neighbors:
                frontier.extend(resulting_neighbors)
        return cl

    def wall_removable(self, c1, c2, cl):
        if abs(c2 - c1) == 1:
            if c1 >= self.grid.cells_x:
                if c1 - self.grid.cells_x in cl[c1]:
                    if c2 - self.grid.cells_x in cl[c2]:
                        if c1 - self.grid.cells_x in cl[c2 - self.grid.cells_x]:
                            return False
            if c1 <= self.grid.cell_number - self.grid.cells_x:
                if c1 + self.grid.cells_x in cl[c1]:
                    if c2 + self.grid.cells_x in cl[c2]:
                        if c1 + self.grid.cells_x in cl[c2 + self.grid.cells_x]:
                            return False
            return True
        if abs(c2 - c1) == self.grid.cells_x:
            if c1 % self.grid.cells_x != 0:
                if c1 - 1 in cl[c1]:
                    if c2 - 1 in cl[c2]:
                        if c1 - 1 in cl[c2 - 1]:
                            #print('reached here')
                            return False
            if c1 % self.grid.cells_x != self.grid.cells_x - 1:
                if c1 + 1 in cl[c1]:
                    if c2 + 1 in cl[c2]:
                        if c1 + 1 in cl[c2 + 1]:
                            return False
            return True

    def remove_walls(self, cl, remove_number):
        while remove_number:
            c1 = random.randint(0, len(cl)-1)
            neighbours = self.grid.search_neighbor(c1)
            unconnected_cells = [n for n in neighbours if n not in cl[c1]]
            if not unconnected_cells:
                continue
            c2 = random.choice(unconnected_cells)
            if self.wall_removable(c1, c2, cl):
                remove_number -= 1
                cl[c1].append(c2)
                cl[c2].append(c1)
                #print('removed the two cells', c1, c2)
        return cl
