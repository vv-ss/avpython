import pygame
from grid import *
from robot import *


class UI:
    def __init__(self, grid: Grid, font_size, cell_width, wall_height, wall_width, margin, robots):
        self.surface = None
        self.cell_width = cell_width
        self.wall_height = wall_height
        self.wall_width = wall_width
        self.grid = grid
        self.board_width = self.grid.cells_x * self.cell_width
        self.board_height = self.grid.cells_y * self.cell_width
        self.margin_top = margin[0]
        self.margin_right = margin[1]
        self.margin_down = margin[2]
        self.margin_left = margin[3]
        self.grid = grid
        # Ladestationen
        self.charger_image = pygame.transform.scale(pygame.image.load('img/battery_station.png'),
                                                    (self.cell_width * 0.5,
                                                     self.cell_width * 0.5))
        # self.chargers = random.sample(range(1, self.cells_x * self.cells_y), num_chargers)
        # Farben
        self.hellblau = (179, 250, 255)
        self.schwarz = (0, 0, 0)
        self.dunkelblau = (40, 60, 200)
        self.gelb = (253, 208, 23)
        self.gruen = (20, 200, 20)
        self.pink = (212, 17, 156)
        self.purple = (150, 30, 220)
        robot_img_start_direction = [0, 0, 180, 180]
        self.targets = [r.target for r in robots]
        self.target_imgs = [pygame.transform.scale(target_pic, (0.8 * cell_width, 0.8 * cell_width)) for target_pic
                            in [pygame.image.load('img/cheese.png'), pygame.image.load('img/leaf.png'),
                                pygame.image.load('img/banana.png'), pygame.image.load('img/bone.png')]]
        self.robot_imgs = [pygame.transform.scale(robot_pic, (0.8 * cell_width, 0.8 * cell_width)) for robot_pic
                           in [pygame.image.load('img/mouse.png'), pygame.image.load('img/snail.png'),
                               pygame.image.load('img/monkey.png'), pygame.image.load('img/dog.png')]]

        self.robots = [pygame.transform.rotate(self.robot_imgs[robot.id], robot_img_start_direction[robot.id]) for robot in robots]
        self.robot_path = [[robot.position] for robot in robots]
        self.robot_colors = [self.pink, self.gruen, self.gelb, self.purple]
        self.double_color = self.schwarz
        self.robot_margin = [self.cell_width * 0.2 * (r.id + 1) for r in robots]
        self.robot_score_x = [self.board_width * 0.2 * (r.id + 1) for r in robots]

        # Schriften
        pygame.init()
        self.font = pygame.font.SysFont("comicschrift", font_size)

    def initialize_surface(self):
        # Fenster erstellen
        self.surface = pygame.display.set_mode((self.margin_left + self.margin_right + self.board_width,
                                                self.margin_top + self.margin_down + self.board_height))
        pygame.display.set_caption('random maze drawing by Aarav and Viyona')

    def draw_grid(self):
        # Gitter malen
        self.surface.fill(self.hellblau)
        for reihe in range(self.grid.cells_y):
            for spalte in range(self.grid.cells_x):
                pygame.draw.rect(self.surface, self.dunkelblau,
                                 pygame.Rect(spalte * self.cell_width + self.margin_left, reihe * self.cell_width +
                                             self.margin_top,
                                             self.cell_width, self.cell_width), 2)
                if self.grid.get_id((reihe, spalte)) in self.grid.chargers:
                    c = ((spalte + 0.5) * self.cell_width + self.margin_left,
                         (reihe + 0.5) * self.cell_width + self.margin_top)
                    self.surface.blit(self.charger_image, self.charger_image.get_rect(center=c))

    def draw_targets(self):
        for i in range(len(self.targets)):
            tgt = ((self.targets[i][1] + 0.5) * self.cell_width + self.margin_left,
                   (self.targets[i][0] + 0.5) * self.cell_width + self.margin_top)
            self.surface.blit(self.target_imgs[i], self.target_imgs[i].get_rect(center=tgt))

    def draw_connections(self, cl):
        # Luecken einfuegen
        for erste in range(len(cl)):
            for zweite in cl[erste]:
                (r1, s1) = self.grid.umrechnen(erste)
                (r2, s2) = self.grid.umrechnen(zweite)
                if r1 == r2:
                    pygame.draw.rect(self.surface, self.hellblau, pygame.Rect(max(s1, s2) * self.cell_width
                                                                              - self.wall_width / 2 + self.margin_left,
                                                                              (r1 + 0.5) *
                                                                              self.cell_width - self.wall_height / 2 + self.margin_top,
                                                                              self.wall_width, self.wall_height))
                if s1 == s2:
                    pygame.draw.rect(self.surface, self.hellblau, pygame.Rect((s1 + 0.5) * self.cell_width -
                                                                              self.wall_height / 2 + self.margin_left,
                                                                              max(r1, r2)
                                                                              * self.cell_width - self.wall_width / 2 + self.margin_top,
                                                                              self.wall_height, self.wall_width))



    def draw_maze(self):
        self.initialize_surface()
        self.draw_grid()
        self.draw_connections(self.grid.connected_list)
        self.draw_targets()

    def update_position(self, robot):
        id = robot.id
        if robot.turn_angle == 0:
            self.robot_path[id].append(robot.position)
        c = ((robot.position[1] + 0.5) * self.cell_width + self.margin_left,
             (robot.position[0] + 0.5) * self.cell_width + self.margin_top)
        self.robots[id] = pygame.transform.rotate(self.robots[id], robot.turn_angle * -90)
        self.surface.blit(self.robots[id], self.robots[id].get_rect(center=c))
        text = self.font.render(str(robot.battery), True, self.schwarz)
        self.surface.blit(text, (self.robot_score_x[id], 10))
        if robot.id == 0:
            for reihe in range(self.grid.cells_y):
                for spalte in range(self.grid.cells_x):
                    text = self.font.render(str(robot.target_distances[(self.grid.get_id((reihe, spalte)))]), True,
                                            self.schwarz)
                    c = (spalte * self.cell_width + self.robot_margin[id] + self.margin_left,
                         reihe * self.cell_width + self.robot_margin[id] + self.margin_top)
                    self.surface.blit(text, c)

    def draw_path(self, robot: Robot):
        id = robot.id
        coordinates = self.robot_path[id][0]
        visited = []
        for new_coordinates in self.robot_path[id][1:]:
            if (coordinates, new_coordinates) not in visited:
                pygame.draw.line(self.surface, self.robot_colors[id],
                                 (coordinates[1] * self.cell_width + self.robot_margin[id] + self.margin_left,
                                  coordinates[0] * self.cell_width + self.robot_margin[id] + self.margin_top),
                                 (new_coordinates[1] * self.cell_width + self.robot_margin[id] + self.margin_left,
                                  new_coordinates[0] * self.cell_width + self.robot_margin[id] + self.margin_top),
                                 self.wall_width)
                visited.append((new_coordinates, coordinates))
            elif self.double_color:
                pygame.draw.line(self.surface, self.double_color,
                                 (coordinates[1] * self.cell_width + self.robot_margin[id] + self.margin_left,
                                  coordinates[0] * self.cell_width + self.robot_margin[id] + self.margin_top),
                                 (new_coordinates[1] * self.cell_width + self.robot_margin[id] + self.margin_left,
                                  new_coordinates[0] * self.cell_width + self.robot_margin[id] + self.margin_top),
                                 self.wall_width)

            coordinates = new_coordinates
