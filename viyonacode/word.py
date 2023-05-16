import pygame
from pygame.locals import *
import * from shapes

width = 900
height = 900
cellwidth = width/10
window = pygame.display.set_mode((width, height))

rectwidth = 100
rectheight = 100

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
    line_horizontal = cellwidth/2
    pygame.display.set_caption('Word by Viyona')
    window.fill(white)
    for lines in range(0, 20):
        pygame.draw.line(window, grey,(0, line_vertical), (width, line_vertical))
        line_vertical += cellwidth/2
    for lines in range(0, 20):
        pygame.draw.line(window, grey,(line_horizontal, cellwidth), (line_horizontal, height))
        line_horizontal += cellwidth/2
    pygame.draw.line(window, lightblue,(0, cellwidth), (width, cellwidth))
    pygame.draw.line(window, lightblue, (0, 0), (width, 0))
    for line in range(0, 10):
        pygame.draw.line(window, lightblue, (wall, 0), (wall, cellwidth))
        wall += cellwidth
    pygame.draw.rect(window, lila, pygame.Rect(0, height - 100, width, 100))
    pygame.display.flip()

def shape(form):
    if form == 'rect':

        pygame.draw.rect(window, blue, pygame.Rect(450 - rectwidth/2, 450 - rectheight/2, rectwidth, rectheight))
    pygame.display.flip()
    if form == 'circle':
        pygame.draw.circle(window, blue,(450, 450), 100)
    #if form == 'polygon':
    #    pygame.draw.polygon(window,blue,((600,700),(600,600),(750,550),(700,600),(700,700)))
    #if form == 'ellipse':
    #    pygame.draw.ellipse(window, blue,(550, 550, 600, 550), 650)
    if form == 'triangle':
        pygame.draw.polygon(window,blue,((400,450),(500,450),(450,500)))
    pygame.display.flip()

def


def print_button(text,farbe,x,y,font):
    text = font.render(text, True, farbe)
    window.blit(text, (x, y))
    pygame.display.flip()

def button_shape(x,y):
    if (x,y) == (0, 0):
        print_button('Rect', black, 5, height - 50, font1)
        print_button('Triangle', black,cellwidth + 5, height - 50, font1)
        pygame.display.flip()


draw_user_interface()
shape('triangle')
print_button('Shape',black,5, 50,font1)
print_button('Color',black,cellwidth + 20, 50,font1)
print_button(' + ',black,cellwidth * 2 + 20, 28,font3)
print_button(' - ',black,cellwidth * 3 + 20, 28,font3)
print_button('Girth',black,cellwidth * 4 + 20, 50,font1)
print_button('Ecken',black,cellwidth * 5 + 20, 50,font1)
print_button('Line',black,cellwidth * 6 + 20, 50,font1)
print_button(' New ',black,cellwidth * 7 + 5, 50,font1)
print_button('Back ',black,cellwidth * 8 + 5, 50,font1)
print_button('Done ',black,cellwidth * 9 + 5, 50,font1)
print('came here2')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            y = y// 100
            x = x // 100
            print(x, y)
            button_shape(x,y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rect.move('UP')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                rect.move('DOWN')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect.move('RIGHT')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move('LEFT')