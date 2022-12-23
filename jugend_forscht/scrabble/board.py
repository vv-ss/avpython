import pygame

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
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tik Tak Toe by Aarav and Viyona')
cell_width = 200
font = pygame.font.Font('freesansbold.ttf', 32)

