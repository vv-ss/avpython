import pygame
from pygame.locals import *
import random

Wert_dict = {}
com_move_first = True
cell_width = 200

# Welche Züge kann der Spieler ziehen
def next_players_state(n):
    moves = []
    for i in range(0, len(n)):
        if n[i] == '0':
            x = list(n)
            x[i] = '2'
            moves.append(''.join(x))
    return moves

# Welche Züge kann der Computer ziehen
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

# Positionen, wie die Lage aussehen könnte, wenn der Spieler gewinnt
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
        return player_win
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


# Positionen, wie die Lage aussehen könnte, wenn der Computer gewinnt
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

# Wir geben jedem möglichem Zug einen Wert
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

# In welches Kästchen soll der Computer ziehen?
def com_move(state):
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

# Der Computer zieht einen beliebigen Zug, sodass der Spieler auch gewinnen kann(einfache Spielvariante)
def com_random_move(state):
    while True:
        x = random.randint(0, len(state)-1)
        if state[x] == '0':
            return x

# Farben, die später gebraucht werden
darkblue=(0,0,139)
gold=(253, 218, 13)
darkgreen2=(50,110,100)
red= (255, 87, 51)
darkgreen=(0,100,0)
green = (0, 255, 0)
türkis=(64, 224, 208)
orange = (255,165,0)
lightblue=(150,230,250)
purple=(128,0,128)
pygame.init()
# Schriften, die später gebraucht werden
font_style = pygame.font.SysFont("bahnschrift", 50)
font_style2 = pygame.font.SysFont("comicschrift", 100)

# Der Computer berechnet mithilfe der Kordinaten in welches Kästchen der Spieler ziehen möchte
def user_click():
    x, y = pygame.mouse.get_pos()
    column = x//cell_width
    row = y//cell_width
    return (row, column)

# Das Brett wird in der Größe 3/4 gemalt
def print_board(size):
    margin = 60
    surface = pygame.display.set_mode((size* cell_width, size*cell_width))
    surface.fill(red)
    pygame.display.set_caption('Tik Tak Toe by Aarav and Viyona')
    for n in range(1, size):
        # Striche, die senkrecht sind
        pygame.draw.rect(window, lightblue, pygame.Rect(n*cell_width, margin, 5, size*cell_width - 2*margin))
        # Striche,die waagerecht sind
        pygame.draw.rect(window, lightblue, pygame.Rect(margin, n * cell_width, size * cell_width - 2*margin, 5))

    text = font.render('TicTacToe', True, purple)
    surface.blit(text, (size*cell_width/2-75,2))
    return surface

# Der Hintergrund der Farben wird gemalt
width=1600
height=1000
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tik Tak Toe by Aarav and Viyona')
font = pygame.font.Font('freesansbold.ttf', 24)
green_cover=pygame.draw.rect(window,türkis,pygame.Rect(0,0,width,height))

# Computer frägt erste Frage
question1=font_style.render('Do you want to play against easy or hard(e/h)?',True,purple)
window.blit(question1, (50,200))
pygame.display.flip()

# Computer beobachtet bis der Spieler "e" oder "h"
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
# Computer schreibt die Antwort der ersten Frage darunter
answer1=font_style.render("You chose " + computer_stufe, True, darkgreen)
window.blit(answer1, (50,250))
pygame.display.flip()

# Computer frägt zweite Frage
question=font_style.render('Do you want to play on 3x3 or 4x4 (3/4)?',True,purple)
window.blit(question, (50,370))
pygame.display.flip()

# Computer beobachtet bis der Spieler "3" oder "4"
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

# Computer schreibt die Antwort der zweiten Frage darunter
answer=font_style.render("You chose " + str(board_size) + 'x' + str(board_size), True, darkgreen)
window.blit(answer, (50,420))
pygame.display.flip()

# Computer frägt dritte Frage
question2=font_style.render('Do you want to move first(y/n)?',True,purple)
window.blit(question2, (50,540))
pygame.display.flip()

# Computer beobachtet bis der Spieler "n" oder "y"
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

# So läuft das Spiel ab
def game():
    global com_move_first
    if start_player == 'Y':
        com_move_first = False
    surface = print_board(board_size)
    pygame.display.flip()
    state = '0'*(board_size*board_size)
    while True:
        # Wenn es Unentschieden ist oder jemand gewonnen hat, soll der Computer hinschreiben wie das Spiel geendet ist
        if draw(state):
            computerwin = font_style.render('DRAW!!!', True, purple)
            surface.blit(computerwin, (board_size * cell_width / 2 - 100, board_size * cell_width-60))
            pygame.display.flip()
            break
        if is_com_end_state(state):
            computerwin = font_style.render('COMPUTER WON!!!', True, purple)
            surface.blit(computerwin, (board_size*cell_width/2-175, board_size*cell_width-60))
            pygame.display.flip()
            break
        if is_player_end_state(state):
            computerwin = font_style.render('PLAYER WON!!!', True, purple)
            surface.blit(computerwin, (board_size * cell_width /2-175, board_size * cell_width -60))
            pygame.display.flip()
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
                # Der Computer malt
                move = com_random_move(state)
            row = move // board_size
            column = move % board_size
            Oletter = font_style2.render('O', True, darkblue)
            surface.blit(Oletter, (cell_width * column + cell_width / 3 + 10, cell_width * row + cell_width / 3 + 10))
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
                        Xletter=font_style2.render('X', True, gold)
                        surface.blit(Xletter, (cell_width * column + cell_width / 3 + 10, cell_width * row + cell_width / 3 + 10))
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

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            else:
                pass
game()
# christoph.buergis@gmail.com