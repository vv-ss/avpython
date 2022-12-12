import time

import pygame
from pygame.locals import *
import random

Wert_dict = {}
com_move_first = True

# Welche Zuege kann der Spieler ziehen
def next_players_state(n):
    moves = []
    for i in range(0, len(n)):
        if n[i] == '0':
            x = list(n)
            x[i] = '2'
            moves.append(''.join(x))
    return moves

# Welche Zuege kann der Computer ziehen
def next_com_state(n):
    next_states = []
    for i in range(0, len(n)):
        if n[i] == '0':
            x = list(n)
            x[i] = '1'
            next_states.append(''.join(x))
    return next_states

# Unentschieden
def draw(n):
    if is_player_end_state(n) or is_com_end_state(n) or '0' in n:
        return False
    else:
        return True

# Positionen, wie die Lage aussehen koennte, wenn der Spieler gewinnt
def is_player_end_state(n):
    if len(n) == 9:
        if n[0] == n[3] == n[6] == '2':
            player_win = True
        elif n[1] == n[4] == n[7] == '2':
            player_win = True
        elif n[2] == n[5] == n[8] == '2':
            player_win = True
        elif n[0] == n[1] == n[2] == '2':
            player_win = True
        elif n[3] == n[4] == n[5] == '2':
            player_win = True
        elif n[6] == n[7] == n[8] == '2':
            player_win = True
        elif n[0] == n[4] == n[8] == '2':
            player_win = True
        elif n[2] == n[4] == n[6] == '2':
            player_win = True
        else:
            player_win = False
    if len(n) == 16:
        if n[0] == n[4] == n[8] == n[12] == '2':
            player_win = True
        elif n[1] == n[5] == n[9] == n[13] == '2':
            player_win = True
        elif n[2] == n[6] == n[10] == n[14] == '2':
            player_win = True
        elif n[3] == n[7] == n[11] == n[15] == '2':
            player_win = True
        elif n[0] == n[1] == n[2] == n[3] == '2':
            player_win = True
        elif n[4] == n[5] == n[6] == n[7] == '2':
            player_win = True
        elif n[8] == n[9] == n[10] == n[11] == '2':
            player_win = True
        elif n[12] == n[13] == n[14] == n[15] == '2':
            player_win = True
        elif n[0] == n[5] == n[10] == n[15] == '2':
            player_win = True
        elif n[3] == n[6] == n[9] == n[12] == '2':
            player_win = True
        else:
            player_win = False
    return player_win


# Positionen, wie die Lage aussehen koennte, wenn der Computer gewinnt
def is_com_end_state(n):
   if len(n) == 9:
       if n[0] == n[3] == n[6] == '1':
           computer_win = True
       elif n[1] == n[4] == n[7] == '1':
           computer_win = True
       elif n[2] == n[5] == n[8] == '1':
           computer_win = True
       elif n[0] == n[1] == n[2] == '1':
           computer_win = True
       elif n[3] == n[4] == n[5] == '1':
           computer_win = True
       elif n[6] == n[7] == n[8] == '1':
           computer_win = True
       elif n[0] == n[4] == n[8] == '1':
           computer_win = True
       elif n[2] == n[4] == n[6] == '1':
           computer_win = True
       else:
           computer_win = False
       return computer_win
   if len(n) == 16:
       if n[0] == n[4] == n[8] == n[12] == '1':
           computer_win = True
       elif n[1] == n[5] == n[9] == n[13] == '1':
           computer_win = True
       elif n[2] == n[6] == n[10] == n[14] == '1':
           computer_win = True
       elif n[3] == n[7] == n[11] == n[15] == '1':
           computer_win = True
       elif n[0] == n[1] == n[2] == n[3] == '1':
           computer_win = True
       elif n[4] == n[5] == n[6] == n[7] == '1':
           computer_win = True
       elif n[8] == n[9] == n[10] == n[11] == '1':
           computer_win = True
       elif n[12] == n[13] == n[14] == n[15] == '1':
           computer_win = True
       elif n[0] == n[5] == n[10] == n[15] == '1':
           computer_win = True
       elif n[3] == n[6] == n[9] == n[12] == '1':
           computer_win = True
       else:
           computer_win = False
       return computer_win
# Ist der Computer dran?
def com_turn(state):
    X = 0
    O = 0
    for i in state:
        if i == '1':
            O += 1
        if i == '2':
            X += 1
    if O == X:
        if com_move_first:
            return True
        else:
            return False
    else:
        if not com_move_first:
            return True
        else:
            return False

# Wir geben jedem moeglichem Zug einen Wert
def get_wert(state):
    #print("Came to get_wert for ", state)
    if state in Wert_dict:
        return Wert_dict[state]
    #print("Wert not found in dict for ", state)
    if is_com_end_state(state):
        return 100
    if is_player_end_state(state):
        return -100
    if draw(state):
        return 0
    alle_werte = []
    state_wert = 0
    if com_turn(state):
        for i in next_com_state(state):
            alle_werte.append(get_wert(i))
        state_wert = max(alle_werte)
    else:
        for i in next_players_state(state):
            alle_werte.append(get_wert(i))
        state_wert = min(alle_werte)
    Wert_dict[state] = state_wert
    return state_wert

# In welches Kaestchen soll der Computer ziehen?
def com_move(state):
    #print("Came to com_move with ", state)
    next_states = next_com_state(state)
    next_best_state = next_states[0]
    next_best_wert = get_wert(next_best_state)
    for i in next_states:
        wert = get_wert(i)
        if wert > next_best_wert:
            next_best_wert = wert
            next_best_state = i
    for i in range(0, len(state)):
        if state[i] != next_best_state[i]:
            return i

# Der Computer zieht einen beliebigen Zug, sodass der Spieler auch gewinnen kann(einfachere Spielvariante)
def com_random_move(state):
    while True:
        x = random.randint(0, len(state)-1)
        if state[x] == '0':
            return x

# # Es wird nach jedem Zug die Brettlage besimmt
# def convert_state_to_board(state, i):
#     if state[i] == '0':
#         return ' '
#     if state[i] == '1':
#         return 'O'
#     if state[i] == '2':
#         return 'X'
#
# # 3x3 Brett
# def printBoard3(state):
#     print('__ __ __ __ __')
#     print('|', convert_state_to_board(state, 0), '|', convert_state_to_board(state, 1), '|',
#           convert_state_to_board(state, 2), '|')
#     print('__ __ __ __ __')
#     print('|', convert_state_to_board(state, 3), '|', convert_state_to_board(state, 4), '|',
#           convert_state_to_board(state, 5), '|')
#     print('__ __ __ __ __')
#     print('|', convert_state_to_board(state, 6), '|', convert_state_to_board(state, 7), '|',
#           convert_state_to_board(state, 8), '|')
#     print('__ __ __ __ __')
#
# # 4x4 Brett
# def printBoard4(state):
#     print('__ __ __ __ __ __')
#     print('|', convert_state_to_board(state, 0), '|', convert_state_to_board(state, 1), '|',
#           convert_state_to_board(state, 2), '|', convert_state_to_board(state, 3), '|')
#     print('__ __ __ __ __ __')
#     print('|', convert_state_to_board(state, 4), '|', convert_state_to_board(state, 5), '|',
#           convert_state_to_board(state, 6), '|', convert_state_to_board(state, 7), '|')
#     print('__ __ __ __ __ __')
#     print('|', convert_state_to_board(state, 8), '|', convert_state_to_board(state, 9), '|',
#           convert_state_to_board(state, 10), '|', convert_state_to_board(state, 11), '|')
#     print('__ __ __ __ __ __')
#     print('|', convert_state_to_board(state, 12), '|', convert_state_to_board(state, 13), '|',
#           convert_state_to_board(state, 14), '|', convert_state_to_board(state, 15), '|')



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



def user_click():
    # get coordinates of mouse click

    # font = pygame.font.Font('freesansbold.ttf', 32)
    x, y = pygame.mouse.get_pos()

    column = x//cell_width
    row = y//cell_width
    return (row, column)

def print_board(size):
    margin = 40
    surface = pygame.display.set_mode((size* cell_width, size*cell_width))
    surface.fill((50, 110, 100))
    pygame.display.set_caption('Tik Tak Toe by Aarav and Viyona')
    for n in range(1, size):
        # senkrecht
        pygame.draw.rect(window, lightblue, pygame.Rect(n*cell_width, margin, 5, size*cell_width - 2*margin))
        # waagerecht
        pygame.draw.rect(window, lightblue, pygame.Rect(margin, n * cell_width, size * cell_width - 2*margin, 5))

    text = font.render('TicTacToe', True, green)
    surface.blit(text, (size*cell_width/2-75,2))
    return surface








green_cover=pygame.draw.rect(window,tuerkis,pygame.Rect(0,0,1000,1000))

question1=font_style.render('Do you want to play against easy or hard(e/h)?',True,purple)
window.blit(question1, (50,490))
pygame.display.flip()

computer_stufe = None
while True:
    if (computer_stufe):
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                print("Key E has been pressed")
                computer_stufe = 'Easy'
                break
            if event.key == pygame.K_h:
                computer_stufe = 'Hard'
                print("Key H has been pressed")
                break


answer1=font_style.render("You chose " + computer_stufe, True, darkgreen)
window.blit(answer1, (50,540))
pygame.display.flip()

question=font_style.render('Do you want to play on 3x3 or 4x4 (3/4)?',True,purple)
window.blit(question, (50,650))
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
                board_size = 3
                break
            if event.key == pygame.K_4:
                board_size = 4
                print("Key 4 has been pressed")
                break


answer=font_style.render("You chose " + str(board_size) + 'x' + str(board_size), True, darkgreen)
window.blit(answer, (50,740))
pygame.display.flip()



# Ask next question
question2=font_style.render('Do you want to start(y/n)?',True,purple)
window.blit(question2, (50,830))
pygame.display.flip()

start_player = None
while True:
    if start_player:
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

def game():
    global com_move_first
    if start_player == 'Y':
        com_move_first = False
    surface = print_board(board_size)
    pygame.display.flip()
    state = '0'*(board_size*board_size)
    while True:
        if draw(state):
            print("IT WAS A DRAW!!!!!!!!!!!!!!")
            time.sleep(20)
            break
        if is_com_end_state(state):
            print("COMPUTER WON!!!!")
            time.sleep(20)
            break
        if is_player_end_state(state):
            print("PLAYER WON!!!!")
            time.sleep(20)
            break
        if com_turn(state):
            if computer_stufe == 'Hard':
                zeros = 0
                for i in range(0, board_size*board_size):
                    if state[i] == '0':
                        zeros = zeros + 1
                if zeros > 12:
                    move = com_random_move(state)
                else:
                    move = com_move(state)
            else:
                move = com_random_move(state)
            row = move // board_size
            column = move % board_size
            surface.blit(o_img, (cell_width * column + cell_width / 3, cell_width * row + cell_width / 3))
            pygame.display.update()
            state_list = list(state)
            state_list[move] = '1'
            state = ''.join(state_list)
        else:
            # Player turn
            moved = False
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        (row, column) = user_click()
                        if state[row*board_size + column] != '0':
                            break
                        print(row, column)
                        surface.blit(x_img, (cell_width * column + cell_width / 3, cell_width * row + cell_width / 3))
                        pygame.display.update()
                        moved = True
                        break
                    else:
                        pass
                if moved:
                    state_list = list(state)
                    state_list[row*board_size + column] = '2'
                    state = ''.join(state_list)
                    break



game()
