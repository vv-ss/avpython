def shortest_path_by_hand(path):
    coordinates = path[0]
    visited = []
    double_visited = []
    shortest_path = [coordinates]
    for new_coordinates in path[1:]:
        if (coordinates, new_coordinates) not in visited:
            visited.append((new_coordinates, coordinates))
        else:
            double_visited.append((coordinates, new_coordinates))
        coordinates = new_coordinates
    for connection in visited:
        if connection not in double_visited:
            shortest_path.append((connection[0]))
    return double_visited, shortest_path


class MazeSolver:
    def __init__(self, grid, algo):
        self.UP, self.RIGHT, self.DOWN, self.LEFT = range(4)
        self.grid = grid
        self.algorithm = algo

    def get_neighbors(self, coordinates, sight_direction):
        (row, col) = (coordinates[0], coordinates[1])
        neighbors = []
        if sight_direction == self.UP:
            if self.grid.get_id((row - 1, col)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row - 1, col)))
            if self.grid.get_id((row, col + 1)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row, col + 1)))
            if self.grid.get_id((row, col - 1)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row, col - 1)))

        if sight_direction == self.DOWN:
            if self.grid.get_id((row + 1, col)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row + 1, col)))
            if self.grid.get_id((row, col + 1)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row, col + 1)))
            if self.grid.get_id((row, col - 1)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row, col - 1)))

        if sight_direction == self.RIGHT:
            if self.grid.get_id((row, col + 1)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row, col + 1)))
            if self.grid.get_id((row - 1, col)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row - 1, col)))
            if self.grid.get_id((row + 1, col)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row + 1, col)))

        if sight_direction == self.LEFT:
            if self.grid.get_id((row, col - 1)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row, col - 1)))
            if self.grid.get_id((row - 1, col)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row - 1, col)))
            if self.grid.get_id((row + 1, col)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                neighbors.append(self.grid.get_id((row + 1, col)))
        return neighbors

    def move(self, coordinates, sight_direction):
        (row, col) = (coordinates[0], coordinates[1])
        if sight_direction == self.UP:
            if self.grid.get_id((row - 1, col)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                if row != 0:
                    return row - 1, col
                return coordinates
            else:
                return coordinates
        if sight_direction == self.DOWN:
            if self.grid.get_id((row + 1, col)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                if row != self.grid.cells_y - 1:
                    return row + 1, col
                return coordinates
            else:
                return coordinates
        if sight_direction == self.RIGHT:
            if self.grid.get_id((row, col + 1)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                if col != self.grid.cells_x - 1:
                    return row, col + 1
                return coordinates
            else:
                return coordinates
        if sight_direction == self.LEFT:
            if self.grid.get_id((row, col - 1)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                if col != 0:
                    return row, col - 1
                return coordinates
            else:
                return coordinates

    def check_turn(self, position, sight_direction):
        if self.algorithm == 'lhs':
            new_sight_direction = (sight_direction - 1) % 4
            new_position = self.move(position, new_sight_direction)
            if new_position == position:
                return sight_direction, 0
            else:
                return new_sight_direction, -1
        if self.algorithm == 'rhs':
            new_sight_direction = (sight_direction + 1) % 4
            new_position = self.move(position, new_sight_direction)
            if new_position == position:
                return sight_direction, 0
            else:
                return new_sight_direction, 1

    def try_move_forward(self, position, sight_direction):
        if self.algorithm == 'lhs':
            new_position = self.move(position, sight_direction)
            if new_position == position:
                return position, (sight_direction + 1) % 4, 1
            else:
                return new_position, sight_direction, 0
        if self.algorithm == 'rhs':
            new_position = self.move(position, sight_direction)
            if new_position == position:
                return position, (sight_direction - 1) % 4, -1
            else:
                return new_position, sight_direction, 0
