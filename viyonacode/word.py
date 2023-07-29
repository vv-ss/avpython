import pygame
from pygame.locals import *
from shapes import *

width = 900
height = 900
cellwidth = width / 10
window = pygame.display.set_mode((width, height))

shapes = []

grey = (230, 230, 230)
lightblue = (5, 213, 250)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (50, 50, 255)
lila = (205, 110, 255)

pygame.init()
font1 = pygame.font.SysFont('freesansbold.ttf', 30)
font2 = pygame.font.SysFont('freesansbold.ttf', 50)
font3 = pygame.font.SysFont('freesansbold.ttf', 70)


def draw_user_interface():
    wall = cellwidth
    line_vertical = cellwidth
    line_horizontal = cellwidth / 2
    pygame.display.set_caption('Word by Viyona')
    window.fill(white)
    for lines in range(0, 20):
        pygame.draw.line(window, grey, (0, line_vertical), (width, line_vertical))
        line_vertical += cellwidth / 2
    for lines in range(0, 20):
        pygame.draw.line(window, grey, (line_horizontal, cellwidth), (line_horizontal, height))
        line_horizontal += cellwidth / 2
    pygame.draw.line(window, lightblue, (0, cellwidth), (width, cellwidth))
    pygame.draw.line(window, lightblue, (0, 0), (width, 0))
    for line in range(0, 10):
        pygame.draw.line(window, lightblue, (wall, 0), (wall, cellwidth))
        wall += cellwidth
    pygame.draw.rect(window, lila, pygame.Rect(0, height - 100, width, 100))
    print_button('Rect', black, 5, 50, font1)
    print_button('Circle', black, cellwidth + 20, 50, font1)
    print_button('Triangle', black, cellwidth * 2 + 20, 50, font1)
    print_button('+', black, cellwidth * 3 + 20, 28, font3)
    print_button('-', black, cellwidth * 4 + 20, 28, font3)
    print_button('Color', black, cellwidth * 5 + 20, 50, font1)
    pygame.display.flip()


def redraw_shape(shape):
    if type(shape) == Rectangle:
        pygame.draw.rect(window, blue, pygame.Rect(shape.dijkstra_solved, shape.y, shape.width, shape.height))
    if type(shape) == Circle:
        pygame.draw.circle(window, blue, (shape.dijkstra_solved, shape.y), shape.r)
    if type(shape) == Triangle:
        pygame.draw.polygon(window, blue, ((shape.x1, shape.y1), (shape.x2, shape.y2), (shape.x3, shape.y3)))
    pygame.display.flip()

def create_shape(form):
    if form == 'rect':
        shape = Rectangle()
        pygame.draw.rect(window, blue, pygame.Rect(shape.x, shape.y, shape.width, shape.height))

    if form == 'circle':
        shape = Circle()
        pygame.draw.circle(window, blue, (shape.x, shape.y), shape.r)
    # if form == 'polygon':
    #    pygame.draw.polygon(window,blue,((600,700),(600,600),(750,550),(700,600),(700,700)))
    # if form == 'ellipse':
    #    pygame.draw.ellipse(window, blue,(550, 550, 600, 550), 650)

    if form == 'triangle':
        shape = Triangle()
        pygame.draw.polygon(window, blue, ((shape.x1, shape.y1), (shape.x2, shape.y2), (shape.x3, shape.y3)))
    pygame.display.flip()
    shapes.append(shape)


def print_button(text, farbe, x, y, font):
    text = font.render(text, True, farbe)
    window.blit(text, (x, y))
    pygame.display.flip()


def button_shape(x):
    if x == 0:
        create_shape('rect')
    if x == 1:
        create_shape('circle')
    if x == 2:
        create_shape('triangle')

    pygame.display.flip()


draw_user_interface()


print('came here2')


def select_shape(x, y):
    for i in shapes:
        print(i)
        if i.covers(x, y):
            print('hello')
            return i


s = None

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            if y < cellwidth:
                button_shape(x // cellwidth)
            else:
                print('came here')
                s = select_shape(x, y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if s is not None:
                    s.move('UP')
                    draw_user_interface()
                    redraw_shape(s)
            if event.key == pygame.K_DOWN:
                if s is not None:
                    s.move('DOWN')
                    draw_user_interface()
                    redraw_shape(s)
            if event.key == pygame.K_RIGHT:
                if s is not None:
                    s.move('RIGHT')
                    draw_user_interface()
                    redraw_shape(s)
            if event.key == pygame.K_LEFT:
                if s is not None:
                    s.move('LEFT')
                    draw_user_interface()
                    redraw_shape(s)
