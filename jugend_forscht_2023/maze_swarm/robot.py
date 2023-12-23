import pygame


class Robot:
    def __init__(self, grid, algo, start_point, target, robot_x, robot_y, robot, sight_direction,
                 set_direction, battery, color,
                 id, shortest_path_option, double_color=None):
        self.UP, self.RIGHT, self.DOWN, self.LEFT = range(4)
        self.sight_direction = sight_direction
        self.grid = grid
        self.algorithm = algo
        self.position = start_point
        self.path = [self.position]
        self.map = [set() for _ in range(self.grid.cell_number)]
        self.flood_fill_neighbours = [self.grid.search_neighbor(i) for i in range(self.grid.cell_number)]
        self.target_distances = [self.grid.cell_number for i in range(self.grid.cell_number)]
        self.visited = [False for _ in range(self.grid.cell_number)]
        self.batteries = []
        self.target = target
        self.robot_x = robot_x
        self.robot_y = robot_y
        self.set_direction = set_direction
        self.robot = pygame.transform.rotate(pygame.transform.scale
                                             (robot, (self.robot_x, self.robot_y)), self.set_direction)
        self.turn_angle = 0
        self.full_battery = battery
        self.battery = battery
        self.last_moved = False
        self.color = color
        self.double_color = double_color
        self.id = id
        self.margin = self.grid.cell_width * 0.2 * self.id
        self.score_x = self.grid.board_width * 0.2 * self.id
        self.store_map()
        self.dijkstra_path = []
        self.dijkstra_active = False
        self.shortest_path_option = shortest_path_option
        self.has_reached_target = False

    def dijkstra(self, start, end):
        shortest_path = []
        visited_dict = {}
        frontier = [start]
        running = True
        while running:
            if not frontier:
                return
            current = frontier.pop(0)
            for neighbor in self.map[current]:
                if neighbor not in visited_dict:
                    visited_dict[neighbor] = current
                    frontier.append(neighbor)
                    if neighbor == end:
                        cell = end
                        shortest_path.append(self.grid.umrechnen(cell))
                        while cell != start:
                            cell = visited_dict[cell]
                            shortest_path.append(self.grid.umrechnen(cell))
                        running = False
        shortest_path.reverse()
        return shortest_path

    def view_neighbors(self, coordinates, sight_direction):
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
            if self.grid.get_id((row - 1, col)) in self.map[self.grid.get_id((row, col))]:
                return row - 1, col
            else:
                return coordinates
        if sight_direction == self.DOWN:
            if self.grid.get_id((row + 1, col)) in self.map[self.grid.get_id((row, col))]:
                return row + 1, col
            else:
                return coordinates
        if sight_direction == self.RIGHT:
            if self.grid.get_id((row, col + 1)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                return row, col + 1
            else:
                return coordinates
        if sight_direction == self.LEFT:
            if self.grid.get_id((row, col - 1)) in self.grid.connected_list[self.grid.get_id((row, col))]:
                return row, col - 1
            else:
                return coordinates

    def check_turn(self, position, sight_direction):
        if self.algorithm == 'lhs':
            move_direction = (sight_direction - 1) % 4
            new_position = self.move(position, move_direction)
            if new_position == position:
                return sight_direction, 0
            else:
                return move_direction, -1
        if self.algorithm == 'rhs':
            move_direction = (sight_direction + 1) % 4
            new_position = self.move(position, move_direction)
            if new_position == position:
                return sight_direction, 0
            else:
                return move_direction, 1

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

    def update_position(self):
        c = ((self.position[1] + 0.5) * self.grid.cell_width + self.grid.margin_left,
             (self.position[0] + 0.5) * self.grid.cell_width + self.grid.margin_top)
        self.robot = pygame.transform.rotate(self.robot, self.turn_angle * -90)
        self.grid.surface.blit(self.robot, self.robot.get_rect(center=c))
        text = self.grid.font.render(str(self.battery), True, self.grid.schwarz)
        self.grid.surface.blit(text, (self.score_x, 10))

    def draw_path(self):
        coordinates = self.path[0]
        visited = []
        for new_coordinates in self.path[1:]:
            if (coordinates, new_coordinates) not in visited:
                pygame.draw.line(self.grid.surface, self.color,
                                 (coordinates[1] * self.grid.cell_width + self.margin + self.grid.margin_left,
                                  coordinates[0] * self.grid.cell_width + self.margin + self.grid.margin_top),
                                 (new_coordinates[1] * self.grid.cell_width + self.margin + self.grid.margin_left,
                                  new_coordinates[0] * self.grid.cell_width + self.margin + self.grid.margin_top),
                                 self.grid.wall_width)
                visited.append((new_coordinates, coordinates))
            elif self.double_color:
                pygame.draw.line(self.grid.surface, self.double_color,
                                 (coordinates[1] * self.grid.cell_width + self.margin + self.grid.margin_left,
                                  coordinates[0] * self.grid.cell_width + self.margin + self.grid.margin_top),
                                 (new_coordinates[1] * self.grid.cell_width + self.margin + self.grid.margin_left,
                                  new_coordinates[0] * self.grid.cell_width + self.margin + self.grid.margin_top),
                                 self.grid.wall_width)

            coordinates = new_coordinates

    def find_shortest_route_to_target(self):
        return self.dijkstra(self.position, self.target)

    def find_nearest_battery(self):
        if not self.shortest_path_option:
            return [], 0
        nearest_battery_path = []
        nearest_battery_distance = 1000000
        for b in self.batteries:
            path = self.dijkstra(self.grid.get_id(self.position), b)
            if path is not None:
                path_length = len(path) - 1
                if path_length < nearest_battery_distance:
                    nearest_battery_path = path
                    nearest_battery_distance = path_length
        # print("Robot ", self.id, " speaking ", nearest_battery_path)
        return nearest_battery_path, nearest_battery_distance

    def take_shortest_path_step(self):
        # if movement is in sight direction, pop from path and reduce battery
        # else change sight direction
        new_position = self.dijkstra_path[0]
        self.check_sight_direction(new_position)
        if self.turn_angle == 0:
            self.position = new_position
            self.dijkstra_path.pop(0)
            self.battery -= 1
            self.path.append(self.position)
            if self.grid.get_id(self.position) in self.grid.chargers:
                self.battery = self.full_battery
        return

    def move_wall_algorithm(self):
        # if moved in last move, first try to turn left if there is no wall there
        if self.last_moved:
            self.last_moved = False
            (self.sight_direction, self.turn_angle) = self.check_turn(self.position, self.sight_direction)
            # if turn_angle is zero, robot found a wall on the left side, if not then the robot turned left and
            # action is complete
            if self.turn_angle == 0:
                pre_pos = self.position
                self.position, self.sight_direction, self.turn_angle = self.try_move_forward(self.position,
                                                                                             self.sight_direction)
                # if turn_angle is zero, robot could move forward, update map and battery
                # if turn_angle is not zero, robot turns right and the action is complete
                if self.turn_angle == 0:
                    self.last_moved = True
                    self.store_map(pre_pos)
                    self.battery -= 1
                    if self.grid.get_id(self.position) in self.grid.chargers:
                        self.batteries.append(self.grid.get_id(self.position))
                        self.battery = self.full_battery
                    self.path.append(self.position)
        # if did not move in last move, try to move forward
        else:
            pre_pos = self.position
            self.position, self.sight_direction, self.turn_angle = self.try_move_forward(self.position,
                                                                                         self.sight_direction)
            # if turn_angle is zero, robot could move forward, update map and battery
            # if turn_angle is not zero, robot turns right and the action is complete
            if self.turn_angle == 0:
                self.last_moved = True
                self.store_map(pre_pos)
                self.battery -= 1
                if self.grid.get_id(self.position) in self.grid.chargers:
                    self.batteries.append(self.grid.get_id(self.position))
                    self.battery = self.full_battery
                self.path.append(self.position)

    def action(self, wait=False):
        # if there is a path to target and it is within reach, go there directly

        # if reached target or battery is empty, then return accordingly
        if self.position == self.target:
            if not self.has_reached_target:
                self.turn_angle = 0
                self.has_reached_target = True
                return 'reached_target'
        if wait:
            self.turn_angle = 0
            return

        if self.battery <= 0:
            self.turn_angle = 0
            return 'battery_empty'

        if self.dijkstra_path:
            self.dijkstra_active = True
            self.take_shortest_path_step()
            return

        nearest_battery_path, nearest_battery_distance = self.find_nearest_battery()
        if nearest_battery_path and nearest_battery_distance >= self.battery - 2 and not self.dijkstra_active:
            # print('going to nearest battery ... ', nearest_battery_path)
            self.dijkstra_path = nearest_battery_path[1:-1] + nearest_battery_path[::-1]
            self.take_shortest_path_step()
            return

        if not self.has_reached_target:
            shortest_path_to_target = self.dijkstra(self.grid.get_id(self.position), self.grid.get_id(self.target))
            # print('robot id', self.id, to_target)
            if shortest_path_to_target:
                self.dijkstra_path = shortest_path_to_target[1:]
                self.take_shortest_path_step()
                return
        self.move_wall_algorithm()

    def check_sight_direction(self, new_position):
        move_direction = self.sight_direction
        if self.position[1] > new_position[1]:
            move_direction = self.LEFT
        elif self.position[1] < new_position[1]:
            move_direction = self.RIGHT
        elif self.position[0] < new_position[0]:
            move_direction = self.DOWN
        elif self.position[0] > new_position[0]:
            move_direction = self.UP
        angle_difference = (move_direction - self.sight_direction + 4) % 4
        if angle_difference == 0:
            self.turn_angle = 0
            return
        if angle_difference == 1:
            self.sight_direction = (self.sight_direction + 1) % 4
            self.turn_angle = 1
        else:
            self.sight_direction = (self.sight_direction - 1) % 4
            self.turn_angle = -1

    # store_map is called only when entering a new cell - assume three side cameras and enter from fourth side
    def store_map(self, pre_pos=None):
        if self.visited[self.grid.get_id(self.position)]:
            return
        # THE FOLLOWING LINE MEANS THAT WHEN A NEW CELL IS EXPLORED, ALLOW TO AGAIN FOLLOW SHORTEST PATH TO BATTERY
        # IF WE DO NOT HAVE THIS ACTIVE LOGIC, WE GET STUCK IN A LOOP - TRY WITH REMOVING THE BELOW LINE AND THE
        # LINE THAT SETS DIJKSTRA_ACTIVE TO TRUE
        self.dijkstra_active = False
        self.visited[self.grid.get_id(self.position)] = True
        neighbors = self.view_neighbors(self.position, self.sight_direction)
        if pre_pos:
            neighbors.append(self.grid.get_id(pre_pos))
        for n in neighbors:
            self.map[self.grid.get_id(self.position)].add(n)
            self.map[n].add(self.grid.get_id(self.position))
        # print('added neighbors for', self.position, neighbors)

    def calculate_target_distance(self):
        frontier = [self.target]
        self.target_distances[self.target] = 0
        while frontier:
            process_cell = frontier.pop()
            process_cell_distance = self.target_distances[process_cell]
            for neighbour in self.flood_fill_neighbours[process_cell]:
                if self.target_distances[neighbour] > process_cell_distance + 1:
                    frontier.append(neighbour)
                    self.target_distances[neighbour] = process_cell_distance + 1

    def flood_fill_move(self):
        min_distance = self.grid.cell_number
        new_position = 0
        for i in self.flood_fill_neighbours[self.position]:
            if self.target_distances[i] < min_distance:
                new_position = i
                min_distance = self.target_distances[i]

        self.position = new_position
        self.update_position()

    def update_flood_fill_neighbours(self):
        if self.visited[self.grid.get_id(self.position)]:
            return
        self.visited[self.grid.get_id(self.position)] = True
        neighbors = self.view_neighbors(self.position, self.sight_direction)
        for i in self.flood_fill_neighbours[self.position]:
            if i not in neighbors:
                self.flood_fill_neighbours[self.position].remove(i)
                self.flood_fill_neighbours[i].remove(self.position)
