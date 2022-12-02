import pygame
from pygame.locals import *
darkgreen=(0,100,0)
green = (0, 255, 0)
tuerkis=(64, 224, 208)
orange = (255,165,0)
lightblue=(150,230,250)
purple=(128,0,128)
pygame.init()
font_style = pygame.font.SysFont("bahnschrift", 50)


width=1000
height=1000

X_img = pygame.image.load("red_x.jpg")
O_img = pygame.image.load("o_modified.png")
x_img = pygame.transform.scale(X_img, (80, 80))
o_img = pygame.transform.scale(O_img, (80, 80))
# Initializing surface
surface = pygame.display.set_mode((width,height))
surface.fill((50, 110, 100))
pygame.display.set_caption('Tik Tak Toe by Aarav and Viyona')

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('TicTacToe', True, green)
surface.blit(text, (425,20))
pygame.draw.rect(surface, (50,110,10), pygame.Rect(225,225,550,550))



def user_click():
    # get coordinates of mouse click
    x, y = pygame.mouse.get_pos()

    # get column of mouse click (1-3)
    if (x < width / 3):
        col = 1

    elif (x < width / 3 * 2):
        col = 2

    elif (x < width):
        col = 3

    else:
        col = None

    # get row of mouse click (1-3)
    if (y < height / 3):
        row = 1

    elif (y < height / 3 * 2):
        row = 2

    elif (y < height):
        row = 3

    else:
        row = None
    print(row, col)

def print_board():
    # Rechteck mitte links
    pygame.draw.rect(surface, lightblue, pygame.Rect(236, 416, 168, 168))
    pygame.draw.rect(surface, orange, pygame.Rect(230, 412, 176, 176), 10)

    # Rechteck mitte mitte
    pygame.draw.rect(surface, lightblue, pygame.Rect(416, 416, 168, 168))
    pygame.draw.rect(surface, orange, pygame.Rect(412, 412, 176, 176), 10)

    # Rechteck mitte rechts
    pygame.draw.rect(surface, lightblue, pygame.Rect(600, 416, 168, 168))
    pygame.draw.rect(surface, orange, pygame.Rect(594, 412, 176, 176), 10)

    # Rechteck oben links
    pygame.draw.rect(surface, lightblue, pygame.Rect(236, 234, 168, 168))
    pygame.draw.rect(surface, orange, pygame.Rect(230, 230, 176, 176), 10)

    # Rechteck oben mitte
    pygame.draw.rect(surface, lightblue, pygame.Rect(416, 234, 168, 168))
    pygame.draw.rect(surface, orange, pygame.Rect(412, 230, 176, 176), 10)

    # Rechteck oben rechts
    pygame.draw.rect(surface, lightblue, pygame.Rect(600, 234, 168, 168))
    pygame.draw.rect(surface, orange, pygame.Rect(594, 230, 176, 176), 10)

    # Rechteck unten links
    pygame.draw.rect(surface, lightblue, pygame.Rect(236, 598, 168, 168))
    pygame.draw.rect(surface, orange, pygame.Rect(230, 594, 176, 176), 10)

    # Rechteck unten mitte
    pygame.draw.rect(surface, lightblue, pygame.Rect(416, 598, 168, 168))
    pygame.draw.rect(surface, orange, pygame.Rect(412, 594, 176, 176), 10)

    # Rechteck unten rechts
    pygame.draw.rect(surface, lightblue, pygame.Rect(600, 598, 168, 168))
    pygame.draw.rect(surface, orange, pygame.Rect(594, 594, 176, 176), 10)


green_cover=pygame.draw.rect(surface,tuerkis,pygame.Rect(0,0,1000,1000))

question1=font_style.render('Do you want to play against easy or hard(e/h)?',True,purple)
surface.blit(question1, (50,490))
pygame.display.flip()

hardness_level = None
while True:
    if (hardness_level):
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                print("Key E has been pressed")
                hardness_level = 'Easy'
                break
            if event.key == pygame.K_h:
                hardness_level = 'Hard'
                print("Key H has been pressed")
                break


answer1=font_style.render("You chose " + hardness_level, True, darkgreen)
surface.blit(answer1, (50,540))
pygame.display.flip()

question=font_style.render('Do you want to play on 3x3 or 4x4 (3/4)?',True,purple)
surface.blit(question, (50,650))
pygame.display.flip()

board_size = None
while True:
    if (board_size):
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                print("Key 3 has been pressed")
                board_size = '3x3'
                break
            if event.key == pygame.K_4:
                board_size = '4x4'
                print("Key 4 has been pressed")
                break


answer=font_style.render("You chose " + board_size, True, darkgreen)
surface.blit(answer, (50,740))
pygame.display.flip()



# Ask next question
question2=font_style.render('Do you want to start(y/n)?',True,purple)
surface.blit(question2, (50,830))
pygame.display.flip()

start_player = None
while True:
    if (start_player):
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                print("Key Y has been pressed")
                start_player = 'Y'
                break
            if event.key == pygame.K_n:
                start_player = 'N'
                print("Key N has been pressed")
                break

print_board()
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            user_click()
        else:
            pass
