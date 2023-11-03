import pygame


class Robot:
    def __init__(self, grid, solver, start_point, target, robot_x, robot_y, robot, set_direction, battery, color,
                 id, double_color=None, dijkstra_disabled=True):
        self.UP, self.RIGHT, self.DOWN, self.LEFT = range(4)
        self.sight_direction = self.UP
        self.grid = grid
        self.solver = solver
        self.position = start_point
        self.path = [self.position]
        self.map = [set() for _ in range(self.grid.cell_number)]
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
        self.dijkstra_disabled = dijkstra_disabled

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
        if self.dijkstra_disabled:
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

    def action(self):
        # if there is a path to target and it is within reach, go there directly

        # if reached target or battery is empty, then return accordingly
        if self.position == self.target:
            self.turn_angle = 0
            return 'reached_target'
        if self.battery == 0:
            self.turn_angle = 0
            return 'battery_empty'

        if self.dijkstra_path:
            self.position = self.dijkstra_path.pop(0)
            self.battery -= 1
            if self.grid.get_id(self.position) in self.grid.chargers:
                self.battery = self.full_battery
            return

        nearest_battery_path, nearest_battery_distance = self.find_nearest_battery()
        if nearest_battery_path and nearest_battery_distance >= self.battery - 2 and not self.dijkstra_active:
            self.dijkstra_path = nearest_battery_path[1:-1] + nearest_battery_path[::-1]
            # print(self.dijkstra_path)
            self.dijkstra_active = True
            self.position = self.dijkstra_path.pop(0)
            self.battery -= 1
            if self.grid.get_id(self.position) in self.grid.chargers:
                self.battery = self.full_battery
            return

        to_target = self.dijkstra(self.grid.get_id(self.position), self.grid.get_id(self.target))
        #print('robot id', self.id, to_target)
        if to_target:
            self.dijkstra_path = to_target
            return

        # if moved in last move, first try to turn left if there is no wall there
        if self.last_moved:
            self.last_moved = False
            (self.sight_direction, self.turn_angle) = self.solver.check_turn(self.position, self.sight_direction)
            # if turn_angle is zero, robot found a wall on the left side, if not then the robot turned left and
            # action is complete
            if self.turn_angle == 0:
                pre_pos = self.position
                self.position, self.sight_direction, self.turn_angle = self.solver.try_move_forward(self.position,
                                                                                                    self.sight_direction)
                # if turn_angle is zero, robot could move forward, update map and battery
                # if turn_angle is not zero, robot turns right and the action is complete
                if self.turn_angle == 0:
                    self.last_moved = True
                    self.store_map(pre_pos)
                    self.battery -= 1
                    self.dijkstra_active = False
                    if self.grid.get_id(self.position) in self.grid.chargers:
                        self.batteries.append(self.grid.get_id(self.position))
                        self.battery = self.full_battery
                    self.path.append(self.position)
        # if did not move in last move, try to move forward
        else:
            pre_pos = self.position
            self.position, self.sight_direction, self.turn_angle = self.solver.try_move_forward(self.position,
                                                                                                self.sight_direction)
            # if turn_angle is zero, robot could move forward, update map and battery
            # if turn_angle is not zero, robot turns right and the action is complete
            if self.turn_angle == 0:
                self.last_moved = True
                self.store_map(pre_pos)
                self.battery -= 1
                self.dijkstra_active = False
                if self.grid.get_id(self.position) in self.grid.chargers:
                    self.batteries.append(self.grid.get_id(self.position))
                    self.battery = self.full_battery
                self.path.append(self.position)

    # store_map is called only when entering a new cell - assume three side cameras and enter from fourth side
    def store_map(self, pre_pos=None):
        if self.visited[self.grid.get_id(self.position)]:
            return
        self.visited[self.grid.get_id(self.position)] = True
        neighbors = self.solver.get_neighbors(self.position, self.sight_direction)
        if pre_pos:
            neighbors.append(self.grid.get_id(pre_pos))
        for n in neighbors:
            self.map[self.grid.get_id(self.position)].add(n)
            self.map[n].add(self.grid.get_id(self.position))
        # print('added neighbors for', self.position, neighbors)
