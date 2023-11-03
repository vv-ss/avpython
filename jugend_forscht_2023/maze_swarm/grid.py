import pygame
import random


class Grid:
    def __init__(self, cells_x, cells_y, cell_width, wall_height, wall_width, margin, font_size, num_chargers):
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.surface = None
        self.cells_x = cells_x
        self.cells_y = cells_y
        self.cell_width = cell_width
        self.board_width = self.cells_x * self.cell_width
        self.board_height = self.cells_y * self.cell_width
        self.cell_number = self.cells_x * self.cells_y
        self.connected_list = [[] for _ in range(self.cell_number)]
        self.margin_top = margin[0]
        self.margin_right = margin[1]
        self.margin_down = margin[2]
        self.margin_left = margin[3]

        # Ladestationen
        self.charger_image = pygame.transform.scale(pygame.image.load('img/battery_station.png'), (self.cell_width * 0.5,
                                                                                                   self.cell_width * 0.5))
        # self.chargers = random.sample(range(1, self.cells_x * self.cells_y), num_chargers)
        if num_chargers == 1:
            self.chargers = [self.cells_y // 2 * self.cells_x + self.cells_x // 2]
        else:
            self.chargers = random.sample(range(1, self.cells_x * self.cells_y), num_chargers)

        # Farben
        self.hellblau = (179, 250, 255)
        self.schwarz = (0, 0, 0)
        self.dunkelblau = (40, 60, 200)
        self.gelb = (253, 208, 23)
        self.gruen = (20, 200, 20)
        self.pink = (212, 17, 156)

        # Schriften
        pygame.init()
        self.font = pygame.font.SysFont("comicschrift", font_size)
        # Insert batteries at random cells

    def get_id(self, coordinates):
        return coordinates[0] * self.cells_x + coordinates[1]

    def umrechnen(self, id):
        return id // self.cells_x, id % self.cells_x

    def search_neighbor(self, kaestchen):
        (reihe, spalte) = self.umrechnen(kaestchen)
        neighbor = [(reihe - 1, spalte), (reihe, spalte + 1), (reihe + 1, spalte), (reihe, spalte - 1)]
        return [self.get_id((r, s)) for (r, s) in neighbor if 0 <= r < self.cells_y and 0 <= s < self.cells_x]

    def initialize_surface(self):
        # Fenster erstellen
        self.surface = pygame.display.set_mode((self.margin_left + self.margin_right + self.board_width, self.margin_top + self.margin_down + self.board_height))
        pygame.display.set_caption('random maze drawing by Aarav and Viyona')

    def draw_grid(self):
        # Gitter malen
        self.surface.fill(self.hellblau)
        for reihe in range(self.cells_y):
            for spalte in range(self.cells_x):
                pygame.draw.rect(self.surface, self.dunkelblau,
                                 pygame.Rect(spalte * self.cell_width + self.margin_left, reihe * self.cell_width +
                                             self.margin_top,
                                             self.cell_width, self.cell_width), 2)
                if self.get_id((reihe, spalte)) in self.chargers:
                    c = ((spalte + 0.5) * self.cell_width + self.margin_left,
                         (reihe + 0.5) * self.cell_width + self.margin_top)
                    self.surface.blit(self.charger_image, self.charger_image.get_rect(center=c))

    def draw_connections(self, cl):
        # Luecken einfuegen
        for erste in range(len(cl)):
            for zweite in cl[erste]:
                (r1, s1) = self.umrechnen(erste)
                (r2, s2) = self.umrechnen(zweite)
                if r1 == r2:
                    pygame.draw.rect(self.surface, self.hellblau, pygame.Rect(max(s1, s2) * self.cell_width
                                                                              - self.wall_width / 2 + self.margin_left, (r1 + 0.5) *
                                                                              self.cell_width - self.wall_height / 2 + self.margin_top,
                                                                              self.wall_width, self.wall_height))
                if s1 == s2:
                    pygame.draw.rect(self.surface, self.hellblau, pygame.Rect((s1 + 0.5) * self.cell_width -
                                                                              self.wall_height / 2 + self.margin_left, max(r1, r2)
                                                                              * self.cell_width - self.wall_width / 2 + self.margin_top,
                                                                              self.wall_height, self.wall_width))

    def draw_maze(self, cl):
        self.initialize_surface()
        self.draw_grid()
        self.draw_connections(cl)
