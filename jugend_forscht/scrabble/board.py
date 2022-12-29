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
darkgreen3 = (50,120,100)
darkgreen=(0,30,10)
green = (0, 255, 0)
türkis=(64, 224, 208)
lightblue=(150,230,250)
purple=(128,0,128)
white=(250,249,246)
yellow=(255, 238, 170)
lightpink=(255, 210, 120)
pygame.init()
pygame.display.init()
pygame.font.init()

factor = 1
highlighted_row = 0
highlighted_column=0
highlighted_tile=0
width=2000//factor
height=2000//factor
margin=150//factor
cell_width = (width-2*margin)/15
margin2=10

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


def get_letters(bag, num, gestell):
    for i in range(0,num):
        gestell.append(bag.pop())
    print('Hier sind deine sieben Buchstaben:', gestell)



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
            if board[row][s] == '00':
                points = points + d[buchstabe]
            if board[row][s] == 'DL' and not (row, s) in tilesdict:
                points = points + (d[buchstabe] * 2)
            if board[row][s] == 'TL' and not (row, s) in tilesdict:
                points = points + (d[buchstabe] * 3)
            if board[row][s] == 'DW' and not (row, s) in tilesdict:
                points = points + d[buchstabe]
                total_times = 2
            if board[row][s] == 'TW' and not (row, s) in tilesdict:
                points = points + d[buchstabe]
                total_times = 3
            s += 1
        points *= total_times
    if direction == 'down':
        total_times = 1
        r = row
        for buchstabe in wort:
            print("came with", buchstabe, d[buchstabe], r, spalte, board[r][spalte])
            if board[r][spalte] == '00':
                points = points + d[buchstabe]
            if board[r][spalte] == 'DL' and not (r, spalte) in tilesdict:
                points = points + (d[buchstabe] * 2)
            if board[r][spalte] == 'TL' and not (r, spalte) in tilesdict:
                points = points + (d[buchstabe] * 3)
            if board[r][spalte] == 'DW' and not (r, spalte) in tilesdict:
                points = points + d[buchstabe]
                total_times = 2
            if board[r][spalte] == 'TW' and not (r, spalte) in tilesdict:
                points = points + d[buchstabe]
                total_times = 3
            r += 1
        points *= total_times
    print ("Word ", wort, " has points ", points)
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

font = pygame.font.Font('freesansbold.ttf', 100//factor)
font2 = pygame.font.SysFont('bahnenschrift.ttf', 30//factor)
font3 = pygame.font.SysFont('bahnenschrift.ttf', 45//factor)
font4 = pygame.font.SysFont('bahnenschrift.ttf', 30//factor)

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

def paint_tile(m,n):
    pygame.draw.rect(window, decide_color(m, n),
                     pygame.Rect(margin + n * cell_width, margin + m * cell_width, cell_width, cell_width))
    pygame.draw.rect(window, darkgreen,
                     pygame.Rect(margin + n * cell_width, margin + m * cell_width, cell_width, cell_width), 3)
    if decide_color(m, n) == purple:
        star = font.render('*', True, black)
        window.blit(star, (margin + n * cell_width + cell_width / 4, margin + m * cell_width + cell_width / 4))
    if decide_color(m, n) == gold:
        DW = font2.render('DW', True, black)
        window.blit(DW, (margin + n * cell_width + cell_width / 4, margin + m * cell_width + cell_width / 4))
    if decide_color(m, n) == red:
        DW = font2.render('TW', True, black)
        window.blit(DW, (margin + n * cell_width + cell_width / 4, margin + m * cell_width + cell_width / 4))
    if decide_color(m, n) == darkblue:
        DW = font2.render('TL', True, black)
        window.blit(DW, (margin + n * cell_width + cell_width / 4, margin + m * cell_width + cell_width / 4))
    if decide_color(m, n) == lightblue:
        DW = font2.render('DL', True, black)
        window.blit(DW, (margin + n * cell_width + cell_width / 4, margin + m * cell_width + cell_width / 4))

def print_board():
    window.fill(darkgreen)
    for m in range(0,15):
        for n in range(0,15):
            paint_tile(m,n)
    pygame.display.flip()

def print_gestell(gestell):
    margin2=10//factor
    m=15
    n=0
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

def remove_from_gestell(m,n):
    margin2 = 10//factor
    pygame.draw.rect(window, darkgreen2,
                     pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2,
                                 cell_width - margin2 * 2, cell_width - margin2 * 2))
    #pygame.draw.rect(window, black,
    #                 pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2,
    #                             cell_width - margin2 * 2, cell_width - margin2 * 2), 3)
    pygame.display.flip()


def highlight_gestell_helper(color1, color2, m, n, i):
    margin2 = 10//factor
    pygame.draw.rect(window, color1,
                     pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2,
                                 cell_width - margin2 * 2, cell_width - margin2 * 2))
    pygame.draw.rect(window, color2,
                     pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2,
                                 cell_width - margin2 * 2, cell_width - margin2 * 2), 3)
    letter = font3.render(i.upper(), True, black)
    points = font3.render(str(d[i]), True, black)
    window.blit(letter, (
        margin + n * cell_width + margin2 + cell_width / 4, margin + m * cell_width + margin2 + cell_width / 4))
    window.blit(points, (
        margin + n * cell_width + margin2 + cell_width / 2, margin + m * cell_width + margin2 + cell_width / 2))
    pygame.display.flip()

def highlight_gestell(row, column, tile):
    global highlighted_row, highlighted_column, highlighted_tile
    if highlighted_row != 0:
        highlight_gestell_helper(white, black, highlighted_row, highlighted_column, highlighted_tile)
    highlight_gestell_helper(yellow, yellow, row, column, tile)
    highlighted_row = row
    highlighted_column = column
    highlighted_tile = tile

def paint_tile_with_letter(row,column, tile,color):
    margin2 = 10 // factor
    pygame.draw.rect(window, color,
                     pygame.Rect(margin + column * cell_width + margin2, margin + row * cell_width + margin2, cell_width - margin2 * 2, cell_width - margin2 * 2))
    pygame.draw.rect(window, black, pygame.Rect(margin + column * cell_width + margin2, margin + row * cell_width + margin2, cell_width - margin2 * 2, cell_width - margin2 * 2), 3)
    letter = font3.render(tile.upper(), True, black)
    points = font3.render((str(d[tile])), True, black)
    window.blit(letter, (
        margin + column * cell_width + margin2 + cell_width / 4, margin + row * cell_width + margin2 + cell_width / 4))
    window.blit(points, (
        margin + column * cell_width + margin2 + cell_width / 2, margin + row * cell_width + margin2 + cell_width / 2))
    pygame.display.flip()

def letters_on_board():
    margin2=10//factor
    for kordinat in tilesdict:
        (m,n)=kordinat
        pygame.draw.rect(window, white, pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2, cell_width - margin2*2, cell_width - margin2*2))
        pygame.draw.rect(window, black, pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2, cell_width - margin2 * 2, cell_width - margin2 * 2),3)
        letter = font3.render((str(tilesdict[kordinat])).upper(), True, black)
        points = font3.render((str(d[(tilesdict[kordinat]).lower()])), True, black)
        print("Came to letters_on_board", str(tilesdict[kordinat]), letter, points)
        window.blit(letter, (margin + n * cell_width + margin2 + cell_width/4, margin + m * cell_width + margin2 + cell_width/4))
        window.blit(points, (margin + n * cell_width + margin2 + cell_width / 2, margin + m * cell_width + margin2 + cell_width / 2))
    pygame.display.flip()

def print_button(m,n,text,color):
    pygame.draw.rect(window, color, pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2, cell_width, cell_width))
    pygame.draw.rect(window, black, pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2, cell_width, cell_width), 3)
    text = font4.render(text, True, black)
    window.blit(text, (
    margin + n * cell_width + margin2 + cell_width / 4, margin + m * cell_width + margin2 + cell_width / 4))
def print_player(m,n,scores,color):
    pygame.draw.rect(window, color, pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2, cell_width, cell_width))
    pygame.draw.rect(window, black, pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2, cell_width, cell_width), 3)
    text = font4.render("Player " + str(n+1), True, black)
    window.blit(text, (
    margin + n * cell_width + margin2 + cell_width / 4, margin + m * cell_width + margin2 + cell_width / 4))
    score = font4.render(str(scores[n]), True, black)
    window.blit(score, (
        margin + n * cell_width + margin2 + cell_width / 4, margin + m * cell_width + margin2 + 3 * cell_width / 4))
# def get_valid_words_2(row, spalte, valid_direction):
#     possible=[]
#     if valid_direction == 'down':
#         start_spalte = spalte
#         for buchstabe_auf_brett in wort_auf_brett:
#             for lenght_of_word in range(1, 8):
#                 alle_kombinationen = list(itertools.permutations(gestell, lenght_of_word))
#                 for kombi in alle_kombinationen:
#                     for x in range(lenght_of_word + 1):
#                         #print(x)
#                         start_row = row - x
#                         kombi_list = list(kombi)
#                         kombi_list.insert(x, buchstabe_auf_brett)
#                         #print(kombi_list, kombi)
#                         neu_wort = ''.join(kombi_list)
#                         if neu_wort in alle_woerter and lenght_of_word + row <= 16:
#                             possible.append((neu_wort, start_row, start_spalte))
#             start_spalte += 1
#     if valid_direction == 'right':
#         start_row = row
#         for buchstabe_auf_brett in wort_auf_brett:
#             for lenght_of_word in range(1, 8):
#                 alle_kombinationen = list(itertools.permutations(gestell, lenght_of_word))
#                 for kombi in alle_kombinationen:
#                     for x in range(lenght_of_word + 1):
#                         #print(x)
#                         start_spalte = spalte - x
#                         kombi_list = list(kombi)
#                         kombi_list.insert(x, buchstabe_auf_brett)
#                         #print(kombi_list, kombi)
#                         neu_wort = ''.join(kombi_list)
#                         if neu_wort in alle_woerter and lenght_of_word + spalte <= 16:
#                             possible.append((neu_wort, start_row, start_spalte))
#             start_row+=1
#     print(possible)
#     return possible

def print_message(str, color):
    m = -1.25
    n = 7
    pygame.draw.rect(window, color, pygame.Rect(margin + n * cell_width + margin2, margin + m * cell_width + margin2,
                                                cell_width * 4, cell_width))
    invalid = font3.render(str, True, black)
    window.blit(invalid, (margin + n * cell_width + margin2 + cell_width / 4, margin + m * cell_width + margin2 + cell_width / 4))
    pygame.display.flip()

def print_players(num_players, currentplayer):
    for i in range(num_players):
        if i == currentplayer:
            print_player(-1.25, i, scores, green)
        else:
            print_player(-1.25, i, scores, lightblue)


def neue_woerter_waagerecht(minrow, mincolumn, maxcolumn, currentm):
    woerter = []
    for c in range(mincolumn, maxcolumn+1):
        if (minrow, c) in tilesdict:
            continue
        minr=minrow
        maxr = minrow
        while minr > 0 and (minr-1, c) in tilesdict:
            minr = minr - 1
        while maxr <14 and (maxr+1, c) in tilesdict:
            maxr = maxr + 1
        if minr == maxr:
            continue
        str = ''
        for r in range(minr, maxr+1):
            if (r, c) in tilesdict:
                character = tilesdict[(r,c)]
            else:
                character = currentm[(r, c)]
            str = str + character
        woerter.append(str)
    while mincolumn > 0 and (minrow, mincolumn - 1) in tilesdict:
        mincolumn -= 1
    while maxcolumn < 14 and (minrow, maxcolumn + 1) in tilesdict:
        maxcolumn += 1
    str = ''
    for c in range(mincolumn, maxcolumn+1):
        if (minrow, c) in tilesdict:
            character = tilesdict[(minrow, c)]
        else:
            character = currentm[(minrow, c)]
        str = str + character
    woerter.append(str)
    return woerter

def neue_woerter_senkrecht(mincolumn, minrow, maxrow, currentm):
    woerter = []
    for r in range(minrow, maxrow+1):
        if (r, mincolumn) in tilesdict:
            continue
        minc=mincolumn
        maxc = mincolumn
        while minc > 0 and (r, minc - 1) in tilesdict:
            minc = minc - 1
        while maxc <14 and (r, maxc+1) in tilesdict:
            maxc = maxc + 1
        if minc == maxc:
            continue
        str = ''
        for c in range(minc, maxc+1):
            if (r, c) in tilesdict:
                character = tilesdict[(r,c)]
            else:
                character = currentm[(r, c)]
            str = str + character
        woerter.append(str)
    while minrow > 0 and (minrow - 1, mincolumn) in tilesdict:
        minrow -= 1
    while maxrow < 14 and (maxrow + 1, mincolumn) in tilesdict:
        maxrow += 1
    str = ''
    for r in range(minrow, maxrow+1):
        if (r, mincolumn) in tilesdict:
            character = tilesdict[(r, mincolumn)]
        else:
            character = currentm[(r, mincolumn)]
        str = str + character
    woerter.append(str)
    return woerter

def is_valid(currentmove):
    min_column = None
    max_column = None
    min_row = None
    max_row = None
    if currentmove == {}:
        return False
    for (r, c) in currentmove:
        if not min_row:
            min_row = max_row = r
            min_column = max_column = c
        if (r < min_row):
            min_row = r
        if (r > max_row):
            max_row = r
        if (c < min_column):
            min_column = c
        if (c > max_column):
            max_column = c
    if min_row != max_row and min_column != max_column:
        return False
    # Case where the user made an across word
    if min_row == max_row:
        for c in range(min_column, max_column + 1):
            if (min_row, c) not in tilesdict and (min_row, c) not in currentmove:
                return False

    # Case where the user made a down word
    if min_column == max_column:
        for r in range(min_row, max_row + 1):
            if (r, min_column) not in tilesdict and (r, min_column) not in currentmove:
                return False
    if min_row == max_row:
        woerter = neue_woerter_waagerecht(min_row, min_column, max_column, currentmove)
    elif min_column == max_column:
        woerter = neue_woerter_senkrecht(min_column, min_row, max_row, currentmove)
    print("Neue woerter => ", woerter)
    return True

num_players = 0
while not 2 <= num_players <= 4:
    num_players = int(input("Number of players (2-4):"))
currentplayer = 0
board = board_in_list()
alle_woerter = read_dictionary('de')
bag = create_bag('de')
gestell = []
scores = []
for player in range(num_players):
    gestell.append([])
    get_letters(bag, 7, gestell[player])
    scores.append(0)
# Schnittstelle
print_board()
print_button(15,11, "renew",lightblue)
print_button(15,12, "cancel",lightblue)
print_button(15,13, "confirm",lightblue)
print_button(-1.25,13, "show",lightblue)
print_button(-1.25,14, "hide",lightblue)
print_players(num_players, currentplayer)


print_gestell(gestell[currentplayer])

wort_auf_brett = "affe"
diraction = "down"
row = spalte = 3

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

# this function finds the possible words in other direction
# need to rewrite
#possible=get_valid_words_2(row, spalte, valid_direction)
#print(possible[0])

#(bestwort, max_points, tilerow, tilespalte) = get_best_word(possible, d, board, tilesdict)

#print(bestwort, max_points, tilerow, tilespalte)

#for buchstabe in bestwort:
#    tilesdict[(tilerow, tilespalte)] = buchstabe
#    if valid_direction == 'down':
#        tilerow += 1
#    else:
#        tilespalte += 1

letters_on_board()
currentmove={}
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x -= margin
            y -= margin
            column = int(x // cell_width)
            row = int(y // cell_width)
            # Fall wo Gestell gedrueckt wird
            if row == 15 and 0 <= column < len(gestell[currentplayer]):
                print(gestell[currentplayer][column])
                highlight_gestell(row, column, gestell[currentplayer][column])
            else:
                # Case where a board tile is pressed
                if highlighted_row>0 and 0 <= row < 15 and 0 <= column < 15 and (row, column) not in tilesdict and (row, column) not in currentmove:
                    currentmove[(row, column)]=highlighted_tile
                    print(highlighted_row)
                    paint_tile_with_letter(row,column, highlighted_tile, lightpink)
                    #remove_from_gestell(highlighted_row, highlighted_column)
                    gestell[currentplayer].pop(highlighted_column)
                    highlighted_row=0
                    highlighted_column=0
                    print_gestell(gestell[currentplayer])
                # Case where cancel is pressed
                if ((row, column)) == (15,12):
                    #print_board()
                    letters_on_board()
                    for (row, column) in currentmove:
                        paint_tile(row, column)
                        gestell[currentplayer].append(currentmove[(row, column)])
                    currentmove={}
                    print_gestell(gestell[currentplayer])
                # Case where renew is pressed
                if ((row, column)) == (15, 11):
                    # print_board()
                    letters_on_board()
                    for (row, column) in currentmove:
                        paint_tile(row, column)
                    currentmove = {}
                    print_gestell(gestell[currentplayer])
                    for gestell_letter in gestell[currentplayer]:
                        bag.append(gestell_letter)
                    random.shuffle(bag)
                    gestell[currentplayer] = []
                    get_letters(bag, 7, gestell[currentplayer])
                    print_gestell(gestell[currentplayer])
                    currentmove={}
                if ((row, column)) == (15, 13):
                    if is_valid(currentmove):
                        score = random.randint(5, 30)
                        print_message("Good move. You got " + str(score) + " points.", green)
                        get_letters(bag, 7 - len(gestell), gestell[currentplayer])
                        scores[currentplayer] += score
                        currentplayer = (currentplayer + 1) % num_players
                        print_players(num_players, currentplayer)
                        for i in range(len(gestell[currentplayer])):
                            remove_from_gestell(15, i)
                        for (row, column) in currentmove:
                            tilesdict[(row, column)] = currentmove[(row, column)]
                        letters_on_board()
                        currentmove = {}
                        # finally current_player += 1
                    else:
                        print_message("Invalid move", red)
                #if ((row, column)) == (-1, 12):
                #    show=gestell
                #    print_button(-1.25, 12, "player1", red)
                #    print_button(-1.25, 13, "player2", lightblue)
                #    pygame.display.flip()
                #if ((row, column)) == (-1, 13):
                #    show=gestell2
                #    print_button(-1.25, 12, "player1", lightblue)
                #    print_button(-1.25, 13, "player2", red)
                #    pygame.display.flip()
                if ((row, column)) == (-1, 13):
                    print_gestell(gestell[currentplayer])
                if ((row, column)) == (-1, 14):
                    for i in range(len(gestell[currentplayer])):
                        remove_from_gestell(15, i)
                #if 0 <= row < 15 and 0 <= column < 15:
                #    highlight_cell(row, co3lumn)
        else:
            pass