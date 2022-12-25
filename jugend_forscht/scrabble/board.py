
import itertools
from itertools import repeat
import random
import pygame
from pygame.locals import *
black=(0,0,0)
darkblue=(0,0,210)
gold=(253, 218, 13)
darkgreen2=(50,110,100)
red= (255, 87, 51)
darkgreen=(0,30,10)
green = (0, 255, 0)
türkis=(64, 224, 208)
lightblue=(150,230,250)
purple=(128,0,128)
white=(250,249,246)
pygame.init()

width=2000
height=2000
margin=150
cell_width = (width-2*margin)/15

# Woerterbuch lesen
def read_dictionary(sprache):
    alle_woerter = set()
    #  Wir öffnen ein Wörterbuch von Deutsch oder Englisch
    if sprache == 'de':
        my_file = open("deutsches_Woerterbuch.txt", "r")
    else:
        my_file = open("englisches_Woerterbuch.txt", "r")
    # Benutze READLINE um ein Wort nachdem anderen zulesen
    myline = my_file.readline()
    while myline:
        alle_woerter.add(myline.strip().lower())
        myline = my_file.readline()
    my_file.close()
    return alle_woerter

# ein Sack voller Buchstaben
def create_bag(sprache):
    bag = list()
    if sprache == 'de':
        bag.extend(repeat('a', 5))
        bag.extend(repeat('b', 2))
        bag.extend(repeat('c', 2))
        bag.extend(repeat('d', 4))
        bag.extend(repeat('e', 15))
        bag.extend(repeat('f', 2))
        bag.extend(repeat('g', 3))
        bag.extend(repeat('h', 4))
        bag.extend(repeat('i', 6))
        bag.extend(repeat('j', 1))
        bag.extend(repeat('k', 2))
        bag.extend(repeat('l', 3))
        bag.extend(repeat('m', 4))
        bag.extend(repeat('n', 9))
        bag.extend(repeat('o', 3))
        bag.extend(repeat('p', 1))
        bag.extend(repeat('q', 1))
        bag.extend(repeat('r', 6))
        bag.extend(repeat('s', 7))
        bag.extend(repeat('t', 6))
        bag.extend(repeat('u', 6))
        bag.extend(repeat('v', 1))
        bag.extend(repeat('w', 1))
        bag.extend(repeat('x', 1))
        bag.extend(repeat('y', 1))
        bag.extend(repeat('z', 1))
        bag.extend(repeat('ä', 1))
        bag.extend(repeat('ö', 1))
        bag.extend(repeat('ü', 1))
        bag.extend(repeat('*', 2))
    # sprache = 'en'
    random.shuffle(bag)
    return bag


def get_seven_letters(bag):
    gestell = []
    for i in range(0,7):
        gestell.append(bag.pop())
    print('Hier sind deine sieben Buchstaben:', gestell)
    return gestell


def board_in_list():
    board=list()
    my_board = open("board.txt", 'r')
    line = my_board.readline()
    while line:
        board.append(line.strip().split(' '))
        line = my_board.readline()
    my_board.close()
    return board



def board_punkte(worttuple, d, board, tilesdict, direction):
    (wort, row, spalte) = worttuple
    points = 0
    if direction == 'right':
        total_times = 1
        s = spalte
        for buchstabe in wort:
            print("came with", buchstabe, d[buchstabe], row, s, board[row - 1][s - 1])
            if board[row - 1][s - 1] == '00':
                points = points + d[buchstabe]
            if board[row - 1][s - 1] == 'DL' and not (row - 1, s - 1) in tilesdict:
                points = points + (d[buchstabe] * 2)
            if board[row - 1][s - 1] == 'TL' and not (row - 1, s - 1) in tilesdict:
                points = points + (d[buchstabe] * 3)
            if board[row - 1][s - 1] == 'DW' and not (row - 1, s - 1) in tilesdict:
                points = points + d[buchstabe]
                total_times = 2
            if board[row - 1][s - 1] == 'TW' and not (row - 1, s - 1) in tilesdict:
                points = points + d[buchstabe]
                total_times = 3
            s += 1
        points *= total_times
    if diraction == 'down':
        total_times = 1
        r = row
        for buchstabe in wort:
            print("came with", buchstabe, r, spalte, board[r - 1][spalte - 1])
            if board[r - 1][spalte - 1] == '00':
                points = points + d[buchstabe]
            if board[r - 1][spalte - 1] == 'DL' and not (r - 1, spalte - 1) in tilesdict:
                points = points + (d[buchstabe] * 2)
            if board[r - 1][spalte - 1] == 'TL' and not (r - 1, spalte - 1) in tilesdict:
                points = points + (d[buchstabe] * 3)
            if board[r - 1][spalte - 1] == 'DW' and not (r - 1, spalte - 1) in tilesdict:
                points = points + d[buchstabe]
                total_times = 2
            if board[r - 1][spalte - 1] == 'TW' and not (r - 1, spalte - 1) in tilesdict:
                points = points + d[buchstabe]
                total_times = 3
            r += 1
        points *= total_times
    return points

def get_best_word(possible, d, board, tilesdict):
    max_points = 0
    for (wort, row, spalte) in possible:
        points = board_punkte((wort, row, spalte), d, board, tilesdict, valid_direction)
        if points > max_points:
            bestwort = wort
            tilerow = row
            tilespalte = spalte
            max_points = points
    return (bestwort, max_points, tilerow, tilespalte)


# Initializing surface
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tik Tak Toe by Aarav and Viyona')

font = pygame.font.Font('freesansbold.ttf', 100)
font2 = pygame.font.SysFont('bahnenschrift.ttf', 30)
font3 = pygame.font.SysFont('bahnenschrift.ttf', 45)


d = {'a': 1, 'ä': 6, 'b': 3, 'c': 4, 'd': 1, 'e': 1, 'f': 4, 'g': 2, 'h': 2, 'i': 1, 'j': 6, 'k': 4, 'l': 2, 'm': 3,
     'n': 1, 'o': 2, 'ö': 8, 'p': 4, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'ü' : 6, 'v': 6, 'w': 3, 'x': 8, 'y': 10, 'z': 3, '*' : 0}
def decide_color(m,n):
    red1=[(0,0),(0,7),(0,14),(7,0),(7,14),(14,0),(14,7),(14,14)]
    gold1=[(1,1),(2,2),(3,3),(4,4),(13,13),(12,12),(11,11),(10,10),(13,1),(12,2),(11,3),(10,4),(1,13),(2,12),(3,11),(4,10)]
    lightblue1=[(0,3),(0,11),(2,6),(2,8),(3,0),(3,7),(3,14),(6,2),(6,6),(6,8),(6,12),(7,3),(7,11),(8,2),(8,6),(8,8),(8,12),(11,0),(11,7),(11,14),(12,6),(12,8),(14,3),(14,11)]
    darkblue1=[(1,5),(1,9),(5,1),(5,5),(5,9),(5,13),(9,1),(9,5),(9,9),(9,13),(13,5),(13,9)]
    if (m,n) in red1:
        return red
    elif (m,n) in gold1:
        return gold
    elif (m,n) in lightblue1:
        return lightblue
    elif (m,n) in darkblue1:
        return darkblue
    elif (m,n)==(7,7):
        return purple
    else:
        return darkgreen2
def print_board():
    window.fill(darkgreen)
    for m in range(0,15):
        for n in range(0,15):
            pygame.draw.rect(window, decide_color(m,n), pygame.Rect(margin + n * cell_width, margin + m * cell_width, cell_width, cell_width))
            pygame.draw.rect(window, darkgreen, pygame.Rect(margin + n * cell_width, margin + m * cell_width, cell_width, cell_width), 3)
            pygame.display.flip()
            if decide_color(m,n)==purple:
                star = font.render('*', True, black)
                window.blit(star, (margin + n * cell_width + cell_width/4, margin + m * cell_width + cell_width/4))
            if decide_color(m, n) == gold:
                DW = font2.render('DW', True, black)
                window.blit(DW, (margin + n * cell_width + cell_width/4, margin + m * cell_width + cell_width/4))
                pygame.display.flip()
            if decide_color(m, n) == red:
                DW = font2.render('TW', True, black)
                window.blit(DW, (margin + n * cell_width + cell_width/4, margin + m * cell_width + cell_width/4))
                pygame.display.flip()
            if decide_color(m, n) == darkblue:
                DW = font2.render('TL', True, black)
                window.blit(DW, (margin + n * cell_width + cell_width/4, margin + m * cell_width + cell_width/4))
                pygame.display.flip()
            if decide_color(m, n) == lightblue:
                DW = font2.render('DL', True, black)
                window.blit(DW, (margin + n * cell_width + cell_width/4, margin + m * cell_width + cell_width/4))
                pygame.display.flip()

def print_gestell(gestell):
    margin2=10
    m=15
    n=4
    pygame.draw.rect(window, darkgreen2, pygame.Rect(margin + n * cell_width, margin + m * cell_width, cell_width * 7, cell_width))
    for i in gestell:
        pygame.draw.rect(window, white, pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2, cell_width - margin2 * 2, cell_width - margin2 * 2))
        pygame.draw.rect(window, black, pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2, cell_width - margin2 * 2, cell_width - margin2 * 2), 3)
        letter = font3.render(i.upper(), True, black)
        points = font3.render(str(d[i]), True, black)
        window.blit(letter, (margin + n * cell_width + margin2 + cell_width / 4, margin + m * cell_width + margin2 + cell_width / 4))
        window.blit(points, (margin + n * cell_width + margin2 + cell_width / 2, margin + m * cell_width + margin2 + cell_width / 2))
        n += 1
        pygame.display.flip()





def letters_on_board():
    margin2=10
    for kordinat in tilesdict:
        (m,n)=kordinat
        pygame.draw.rect(window, white, pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2, cell_width - margin2*2, cell_width - margin2*2))
        pygame.draw.rect(window, black, pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2, cell_width - margin2 * 2, cell_width - margin2 * 2),3)
        letter = font3.render((str(tilesdict[kordinat])).upper(), True, black)
        points = font3.render((str(d[tilesdict[kordinat]])), True, black)
        window.blit(letter, (margin + n * cell_width + margin2 + cell_width/4, margin + m * cell_width + margin2 + cell_width/4))
        window.blit(points, (margin + n * cell_width + margin2 + cell_width / 2, margin + m * cell_width + margin2 + cell_width / 2))
        pygame.display.flip()

def get_valid_words_2(row, spalte, valid_direction):
    possible=[]
    if valid_direction== 'right':
        start_spalte = spalte
        for buchstabe_auf_brett in wort_auf_brett:
            for lenght_of_word in range(1, 8):
                alle_kombinationen = list(itertools.permutations(gestell, lenght_of_word))
                for kombi in alle_kombinationen:
                    for x in range(lenght_of_word + 1):
                        #print(x)
                        start_row = row - x
                        kombi_list = list(kombi)
                        kombi_list.insert(x, buchstabe_auf_brett)
                        #print(kombi_list, kombi)
                        neu_wort = ''.join(kombi_list)
                        if neu_wort in alle_woerter:
                            possible.append((neu_wort, start_row, start_spalte))
            start_spalte+=1
    if valid_direction== 'down':
        start_row = row
        for buchstabe_auf_brett in wort_auf_brett:
            for lenght_of_word in range(1, 8):
                alle_kombinationen = list(itertools.permutations(gestell, lenght_of_word))
                for kombi in alle_kombinationen:
                    for x in range(lenght_of_word + 1):
                        #print(x)
                        start_spalte = spalte - x
                        kombi_list = list(kombi)
                        kombi_list.insert(x, buchstabe_auf_brett)
                        #print(kombi_list, kombi)
                        neu_wort = ''.join(kombi_list)
                        if neu_wort in alle_woerter:
                            possible.append((neu_wort, start_row, start_spalte))
            start_row+=1
    print(possible)
    return possible


print_board()
board = board_in_list()
alle_woerter = read_dictionary('de')
bag = create_bag('de')
gestell = get_seven_letters(bag)
print_gestell(gestell)

gestell_kordinat={(4,15) : gestell[0],
                  (5,15) : gestell[1],
                  (6,15) : gestell[2],
                  (7,15) : gestell[3],
                  (8,15) : gestell[4],
                  (9,15) : gestell[5],
                  (10,15) : gestell[6]}


print(gestell_kordinat)
#if gestell_touch() in gestell_kordinat:
 #   print(gestell_kordinat[gestell_touch()])
#else:
 #   print('a')
diraction = input('diraction:')
row = int(input('row:'))
spalte = int(input('spalte:'))
wort_auf_brett = input('Welches Wort liegt bereits auf dem Brett: ')


tilerow = row
tilespalte = spalte
tilesdict = {}
for buchstabe in wort_auf_brett:
    tilesdict[(tilerow, tilespalte)] = buchstabe
    if diraction == 'down':
        tilerow += 1
    else:
        tilespalte += 1

letters_on_board()

board = board_in_list()
if diraction == 'down':
    valid_direction = 'right'
else:
    valid_direction = 'down'

possible=get_valid_words_2(row, spalte, valid_direction)
print(possible[0])

(bestwort, max_points, tilerow, tilespalte) = get_best_word(possible, d, board, tilesdict)


print(bestwort, max_points, tilerow, tilespalte)

for buchstabe in bestwort:
    tilesdict[(tilerow, tilespalte)] = buchstabe
    if valid_direction == 'down':
        tilerow += 1
    else:
        tilespalte += 1

letters_on_board()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            column = x // cell_width - 1
            row = y // cell_width - 1
            print(row, column)
        else:
            pass

