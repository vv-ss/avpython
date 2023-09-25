import random


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
