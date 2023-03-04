import itertools
from itertools import repeat
import random
import pygame
from pygame.locals import *

# Farben, die später gebraucht werden
neonblau=(32, 210, 244)
schwarz=(0, 0, 0)
dunkelblau=(0, 0, 210)
gold=(253, 218, 13)
dunkelgrün2=(50, 110, 100)
rot= (255, 87, 51)
dunkelgrün3 = (50, 120, 100)
dunkelgrün=(0, 30, 10)
grün = (0, 255, 0)
türkis=(64, 224, 208)
hellblau=(150, 230, 250)
lila=(128, 0, 128)
weiß=(250, 249, 246)
gelb=(255, 238, 170)
pink=(255, 210, 120)
neongrün=(223,255,0)
pygame.init()
pygame.display.init()
pygame.font.init()

# Variabeln, die später gebraucht werden
bildschirm_größe = 3
markierte_reihe = 0
markierte_spalte=0
markierter_buchstabenstein= ' '
breite= 2400 // bildschirm_größe
höhe= 2400 // bildschirm_größe
abstand= 200 // bildschirm_größe
kästchen_größe = (breite - 2 * abstand) / 15
abstand2= 10 // bildschirm_größe

# Schriften, die später gebraucht werden
font = pygame.font.Font('freesansbold.ttf', 100 // bildschirm_größe)
font2 = pygame.font.SysFont('bahnenschrift.ttf', 50 // bildschirm_größe)
font3 = pygame.font.SysFont('bahnenschrift.ttf', 40 // bildschirm_größe)
font4 = pygame.font.SysFont('bahnenschrift.ttf', 100 // bildschirm_größe)

# Woerterbuch lesen
def wörterbuch_lesen(sprache):
    alle_wörter = set()
    # Der Computer öffnet ein Wörterbuch von Deutsch, Englisch oder Französisch
    if sprache == 'de':
        file = open("deutsches_woerterbuch.txt", "r", encoding='utf-8')
    if sprache == 'en':
        file = open("englisches_woerterbuch_us.txt", "r")
    if sprache == 'fr':
        file = open("franzoesisch_woerterbuch.txt", "r")
    zeile = file.readline()
    while zeile:
        alle_wörter.add(zeile.strip().lower())
        zeile = file.readline()
    file.close()
    return alle_wörter

# Säcke mit Buchstaben der verschieden Sprachen
def erstelle_beutel(sprache):
    beutel = list()
    if sprache == 'de':
        beutel.extend(repeat('a', 5))
        beutel.extend(repeat('b', 2))
        beutel.extend(repeat('c', 2))
        beutel.extend(repeat('d', 4))
        beutel.extend(repeat('e', 15))
        beutel.extend(repeat('f', 2))
        beutel.extend(repeat('g', 3))
        beutel.extend(repeat('h', 4))
        beutel.extend(repeat('i', 6))
        beutel.extend(repeat('j', 1))
        beutel.extend(repeat('k', 2))
        beutel.extend(repeat('l', 3))
        beutel.extend(repeat('m', 4))
        beutel.extend(repeat('n', 9))
        beutel.extend(repeat('o', 3))
        beutel.extend(repeat('p', 1))
        beutel.extend(repeat('q', 1))
        beutel.extend(repeat('r', 6))
        beutel.extend(repeat('s', 7))
        beutel.extend(repeat('t', 6))
        beutel.extend(repeat('u', 6))
        beutel.extend(repeat('v', 1))
        beutel.extend(repeat('w', 1))
        beutel.extend(repeat('x', 1))
        beutel.extend(repeat('y', 1))
        beutel.extend(repeat('z', 1))
        beutel.extend(repeat('ä', 1))
        beutel.extend(repeat('ö', 1))
        beutel.extend(repeat('ü', 1))
        beutel.extend(repeat('*', 2))
    if sprache == 'fr':
        beutel.extend(repeat('a', 9))
        beutel.extend(repeat('b', 2))
        beutel.extend(repeat('c', 2))
        beutel.extend(repeat('d', 3))
        beutel.extend(repeat('e', 15))
        beutel.extend(repeat('f', 2))
        beutel.extend(repeat('g', 2))
        beutel.extend(repeat('h', 2))
        beutel.extend(repeat('i', 8))
        beutel.extend(repeat('j', 1))
        beutel.extend(repeat('k', 1))
        beutel.extend(repeat('l', 5))
        beutel.extend(repeat('m', 3))
        beutel.extend(repeat('n', 6))
        beutel.extend(repeat('o', 6))
        beutel.extend(repeat('p', 2))
        beutel.extend(repeat('q', 1))
        beutel.extend(repeat('r', 6))
        beutel.extend(repeat('s', 6))
        beutel.extend(repeat('t', 6))
        beutel.extend(repeat('u', 6))
        beutel.extend(repeat('v', 2))
        beutel.extend(repeat('w', 1))
        beutel.extend(repeat('x', 1))
        beutel.extend(repeat('y', 1))
        beutel.extend(repeat('z', 1))
        beutel.extend(repeat('*', 2))
    if sprache == 'en':
        beutel.extend(repeat('a', 9))
        beutel.extend(repeat('b', 2))
        beutel.extend(repeat('c', 2))
        beutel.extend(repeat('d', 4))
        beutel.extend(repeat('e', 12))
        beutel.extend(repeat('f', 2))
        beutel.extend(repeat('g', 3))
        beutel.extend(repeat('h', 2))
        beutel.extend(repeat('i', 9))
        beutel.extend(repeat('j', 1))
        beutel.extend(repeat('k', 1))
        beutel.extend(repeat('l', 4))
        beutel.extend(repeat('m', 2))
        beutel.extend(repeat('n', 6))
        beutel.extend(repeat('o', 8))
        beutel.extend(repeat('p', 2))
        beutel.extend(repeat('q', 1))
        beutel.extend(repeat('r', 6))
        beutel.extend(repeat('s', 4))
        beutel.extend(repeat('t', 6))
        beutel.extend(repeat('u', 4))
        beutel.extend(repeat('v', 2))
        beutel.extend(repeat('w', 2))
        beutel.extend(repeat('x', 1))
        beutel.extend(repeat('y', 2))
        beutel.extend(repeat('z', 1))
        beutel.extend(repeat('*', 2))
    random.shuffle(beutel)
    return beutel

# Der Computer gibt die sieben Buchstaben
def fülle_ablagebank(beutel, anzahl, ablagebank):
    for i in range(0, anzahl):
        try:
            ablagebank.append(beutel.pop())
        except IndexError:
            return

# Informationen des Brettes aus einer Datei lesen und in eine Liste speichern
def erstelle_brettliste():
    brett=list()
    mein_brett = open("board.txt", 'r')
    line = mein_brett.readline()
    while line:
        brett.append(line.strip().split(' '))
        line = mein_brett.readline()
    mein_brett.close()
    return brett


# Berechnet Punkte mithilfe des Brettes,
# des entstandenen Wortes und der Positionen
def punkte_berechnen(worttuple, richtung, aktueller_zug):
    (wort, reihe, spalte) = worttuple
    punkte = 0
    if richtung == 'right':
        insgesamt = 1
        s = spalte
        for buchstabe in wort:
            buchstabe_auf_brett = ''
            if (reihe, s) in buchstabensteine_dictionary:
                buchstabe_auf_brett = buchstabensteine_dictionary[(reihe, s)][0]
            else:
                buchstabe_auf_brett = aktueller_zug[(reihe, s)][0]
            if board[reihe][s] == '00' or board[reihe][s] == '--':
                punkte = punkte + buchstaben_punkte[buchstabe_auf_brett]
            if board[reihe][s] == 'DL':
                if (reihe, s) in buchstabensteine_dictionary:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett])
                else:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett] * 2)
            if board[reihe][s] == 'TL':
                if (reihe, s) in buchstabensteine_dictionary:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett])
                else:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett] * 3)
            if board[reihe][s] == 'DW':
                punkte = punkte + buchstaben_punkte[buchstabe_auf_brett]
                if not (reihe, s) in buchstabensteine_dictionary:
                    insgesamt = 2
            if board[reihe][s] == 'TW':
                punkte = punkte + buchstaben_punkte[buchstabe_auf_brett]
                if not (reihe, s) in buchstabensteine_dictionary:
                    insgesamt = 3
            s += 1
        punkte *= insgesamt
    if richtung == 'down':
        insgesamt = 1
        r = reihe
        for buchstabe in wort:
            buchstabe_auf_brett = ''
            if (r, spalte) in buchstabensteine_dictionary:
                buchstabe_auf_brett = buchstabensteine_dictionary[(r, spalte)][0]
            else:
                buchstabe_auf_brett = aktueller_zug[(r, spalte)][0]
            print("came with", buchstabe_auf_brett, buchstaben_punkte[buchstabe_auf_brett], r, spalte, board[r][spalte])
            if board[r][spalte] == '00' or board[r][spalte] == '--':
                punkte = punkte + buchstaben_punkte[buchstabe_auf_brett]
            if board[r][spalte] == 'DL':
                if (r, spalte) in buchstabensteine_dictionary:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett])
                else:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett] * 2)
            if board[r][spalte] == 'TL':
                if (r, spalte) in buchstabensteine_dictionary:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett])
                else:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett] * 3)
            if board[r][spalte] == 'DW':
                punkte = punkte + buchstaben_punkte[buchstabe_auf_brett]
                if not (r, spalte) in buchstabensteine_dictionary:
                    insgesamt = 2
            if board[r][spalte] == 'TW':
                punkte = punkte + buchstaben_punkte[buchstabe_auf_brett]
                if not (r, spalte) in buchstabensteine_dictionary:
                    insgesamt = 3
            r += 1
        punkte *= insgesamt
    print("Word ", wort, " has points ", punkte)
    return punkte




# Fenster gestalten
fenster = pygame.display.set_mode((breite, höhe))
pygame.display.set_caption('Scrabblespiel von Aarav und Viyona')

# Buchstabenwerte
buchstaben_punkte = {}
def buchstaben_punkte_bestimmen(sprache):
    global buchstaben_punkte
    if sprache == 'de':
        buchstaben_punkte = {'a': 1, 'ä': 6, 'b': 3, 'c': 4, 'd': 1, 'e': 1, 'f': 4, 'g': 2, 'h': 2, 'i': 1, 'j': 6, 'k': 4, 'l': 2, 'm': 3,
     'n': 1, 'o': 2, 'ö': 8, 'p': 4, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'ü' : 6, 'v': 6, 'w': 3, 'x': 8, 'y': 10, 'z': 3, '*' : 0}
    if sprache == 'en':
        buchstaben_punkte = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
     'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*' : 0}
    if sprache == 'fr':
        buchstaben_punkte = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 10, 'l': 1, 'm': 2,
         'n': 1, 'o': 1, 'p': 3, 'q': 8, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 10, 'x': 10,
         'y': 10, 'z': 3, '*': 0}
# Die Brettfarbe wird entschieden
def farben_bestimmen(reihe, spalte):
    rot1=[(0,0),(0,7),(0,14),(7,0),(7,14),(14,0),(14,7),(14,14)]
    gold1=[(1,1),(2,2),(3,3),(4,4),(13,13),(12,12),(11,11),(10,10),(13,1),(12,2),(11,3),(10,4),(1,13),(2,12),(3,11),(4,10)]
    hellblau1=[(0,3),(0,11),(2,6),(2,8),(3,0),(3,7),(3,14),(6,2),(6,6),(6,8),(6,12),(7,3),(7,11),(8,2),(8,6),(8,8),(8,12),(11,0),(11,7),(11,14),(12,6),(12,8),(14,3),(14,11)]
    dunkelblau1=[(1,5),(1,9),(5,1),(5,5),(5,9),(5,13),(9,1),(9,5),(9,9),(9,13),(13,5),(13,9)]
    if (reihe, spalte) in rot1:
        return rot
    elif (reihe, spalte) in gold1:
        return gold
    elif (reihe, spalte) in hellblau1:
        return hellblau
    elif (reihe, spalte) in dunkelblau1:
        return dunkelblau
    elif (reihe, spalte)==(7, 7):
        return lila
    else:
        return dunkelgrün2

# Ein Kästchen gestalten
def kästchen_drucken(m, n):
    ##
    pygame.draw.rect(fenster, farben_bestimmen(m, n),
                     pygame.Rect(abstand + n * kästchen_größe, abstand + m * kästchen_größe, kästchen_größe, kästchen_größe))
    pygame.draw.rect(fenster, dunkelgrün,
                     pygame.Rect(abstand + n * kästchen_größe, abstand + m * kästchen_größe, kästchen_größe, kästchen_größe), 3)
    if farben_bestimmen(m, n) == lila:
        star = font.render('*', True, schwarz)
        fenster.blit(star, (abstand + n * kästchen_größe + kästchen_größe / 4, abstand + m * kästchen_größe + kästchen_größe / 4))
    if farben_bestimmen(m, n) == gold:
        DW = font2.render('DW', True, schwarz)
        fenster.blit(DW, (abstand + n * kästchen_größe + kästchen_größe / 4, abstand + m * kästchen_größe + kästchen_größe / 4))
    if farben_bestimmen(m, n) == rot:
        DW = font2.render('TW', True, schwarz)
        fenster.blit(DW, (abstand + n * kästchen_größe + kästchen_größe / 4, abstand + m * kästchen_größe + kästchen_größe / 4))
    if farben_bestimmen(m, n) == dunkelblau:
        DW = font2.render('TL', True, schwarz)
        fenster.blit(DW, (abstand + n * kästchen_größe + kästchen_größe / 4, abstand + m * kästchen_größe + kästchen_größe / 4))
    if farben_bestimmen(m, n) == hellblau:
        DW = font2.render('DL', True, schwarz)
        fenster.blit(DW, (abstand + n * kästchen_größe + kästchen_größe / 4, abstand + m * kästchen_größe + kästchen_größe / 4))

# Brett wird gedruckt
def print_board():
    fenster.fill(dunkelgrün)
    for m in range(0,15):
        for n in range(0,15):
            kästchen_drucken(m, n)
    pygame.display.flip()

# Ablagebank wird gedruckt
def print_gestell(gestell):
    m=15
    n=0
    pygame.draw.rect(fenster, dunkelgrün2, pygame.Rect(abstand + n * kästchen_größe, abstand + m * kästchen_größe, kästchen_größe * 7, kästchen_größe))
    for i in gestell:
        pygame.draw.rect(fenster, weiß, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2))
        pygame.draw.rect(fenster, schwarz, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2), 3)
        letter = font3.render(i.upper(), True, schwarz)
        points = font3.render(str(buchstaben_punkte[i[0]]), True, schwarz)
        fenster.blit(letter, (abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
        fenster.blit(points, (abstand + n * kästchen_größe + abstand2 + kästchen_größe / 2, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 2))
        n += 1
    pygame.display.flip()

# Einen Buchstaben von der Ablagebank entfernen
def remove_from_gestell(m,n):
    pygame.draw.rect(fenster, dunkelgrün2,
                     pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2,
                                 kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2))
    pygame.display.flip()

# Hilfe, um den angeklickten Buchstaben auf der Ablagebank zu markieren
def highlight_gestell_helper(color1, color2, m, n, i):
    pygame.draw.rect(fenster, color1,
                     pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2,
                                 kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2))
    pygame.draw.rect(fenster, color2,
                     pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2,
                                 kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2), 3)
    letter = font3.render(i.upper(), True, schwarz)
    points = font3.render(str(buchstaben_punkte[i[0]]), True, schwarz)
    fenster.blit(letter, (
        abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
    fenster.blit(points, (
        abstand + n * kästchen_größe + abstand2 + kästchen_größe / 2, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 2))
    pygame.display.flip()

# Den angeklickten Buchstaben auf der Ablagebank markieren
def highlight_gestell(row, column, tile):
    global markierte_reihe, markierte_spalte, markierter_buchstabenstein
    if markierte_reihe != 0:
        highlight_gestell_helper(weiß, schwarz, markierte_reihe, markierte_spalte, markierter_buchstabenstein)
    highlight_gestell_helper(gelb, gelb, row, column, tile)
    markierte_reihe = row
    markierte_spalte = column
    markierter_buchstabenstein = tile

# Einen Buchstaben auf dem Brett malen
def paint_tile_with_letter(row,column, tile,color):
    margin2 = 10 // bildschirm_größe
    pygame.draw.rect(fenster, color,
                     pygame.Rect(abstand + column * kästchen_größe + margin2, abstand + row * kästchen_größe + margin2, kästchen_größe - margin2 * 2, kästchen_größe - margin2 * 2))
    pygame.draw.rect(fenster, schwarz, pygame.Rect(abstand + column * kästchen_größe + margin2, abstand + row * kästchen_größe + margin2, kästchen_größe - margin2 * 2, kästchen_größe - margin2 * 2), 3)
    letter = font3.render(tile.upper(), True, schwarz)
    points = font3.render((str(buchstaben_punkte[tile[0]])), True, schwarz)
    fenster.blit(letter, (
        abstand + column * kästchen_größe + margin2 + kästchen_größe / 4, abstand + row * kästchen_größe + margin2 + kästchen_größe / 4))
    fenster.blit(points, (
        abstand + column * kästchen_größe + margin2 + kästchen_größe / 2, abstand + row * kästchen_größe + margin2 + kästchen_größe / 2))
    pygame.display.flip()

# Aktuelles Brett drucken
def letters_on_board():
    for kordinat in buchstabensteine_dictionary:
        (m,n)=kordinat
        pygame.draw.rect(fenster, weiß, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2))
        pygame.draw.rect(fenster, schwarz, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2), 3)
        letter = font3.render((str(buchstabensteine_dictionary[kordinat])).upper(), True, schwarz)
        points = font3.render((str(buchstaben_punkte[(buchstabensteine_dictionary[kordinat][0]).lower()])), True, schwarz)
        fenster.blit(letter, (abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
        fenster.blit(points, (abstand + n * kästchen_größe + abstand2 + kästchen_größe / 2, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 2))
    pygame.display.flip()

# Spielknöpfe drucken
def print_button(m,n,text,color):
    pygame.draw.rect(fenster, color, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe, kästchen_größe))
    pygame.draw.rect(fenster, schwarz, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe, kästchen_größe), 3)
    text = font3.render(text, True, schwarz)
    fenster.blit(text, (
        abstand + n * kästchen_größe + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
    pygame.display.flip()

# aktuellen Spieler anzeigen
def print_player(m,n,scores,color, is_computer_player):
    pygame.draw.rect(fenster, color, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe, kästchen_größe))
    pygame.draw.rect(fenster, schwarz, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe, kästchen_größe), 3)
    if is_computer_player:
        text = font2.render("COM", True, schwarz)
    else:
        text = font2.render("P" + str(n + 1), True, schwarz)
    fenster.blit(text, (
        abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
    score = font2.render(str(scores[n]), True, schwarz)
    fenster.blit(score, (
        abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + 3 * kästchen_größe / 5))
    pygame.display.flip()


# senkrechten Zug suchen
def find_move_senkrecht(minr, maxr, row, spalte, buchstabe, gestell):
    best_score = 0
    best_move = {}
    best_gestell_buchstaben = []
    bestword = ''
    #print("came in senkrecht", minr, maxr, row, spalte, buchstabe, gestell)
    max_characters_from_gestell = min(7, maxr - minr)
    for num_characters_from_gestell in range(1, max_characters_from_gestell + 1):
        alle_kombinationen = list(itertools.permutations(gestell, num_characters_from_gestell))
        for kombi in alle_kombinationen:
            # word can start from size of word above to one below the row
            for start_pos in range(row - num_characters_from_gestell, row + 1):
                buchstaben_list = list(kombi)
                # wenn das Wort ist nicht auf dem Brett
                if start_pos < minr or start_pos + num_characters_from_gestell > maxr:
                    continue
                buchstaben_list.insert(row - start_pos, buchstabe)
                word = ''.join(buchstaben_list)
                if word in alle_woerter:
                    print(word)
                    #Aktuelle Bewegung aus der Ablagebank definieren
                    move = {}
                    worttuple = (word, start_pos, spalte)
                    for i in buchstaben_list:
                        move[(start_pos, spalte)] = i
                        start_pos += 1
                    score = punkte_berechnen(worttuple, "down", move)
                    if len(move) == 8:
                        score +=50
                    print(score)
                    if score > best_score:
                        best_score = score
                        best_move = move
                        best_gestell_buchstaben = list(kombi)
                        bestword = word
    return best_move, best_score, best_gestell_buchstaben, bestword

# waagerechten Zug suchen
def find_move_waagerecht(row, column, minc, maxc, buchstabe, gestell):
    best_score = 0
    best_move = {}
    best_gestell_buchstabe = []
    bestword = ''
    #print("came in waagerecht", row, column, minc, maxc, buchstabe, gestell)
    max_characters_from_gestell = min(7, maxc - minc)
    for num_characters_from_gestell in range(1, max_characters_from_gestell + 1):
        alle_kombinationen = list(itertools.permutations(gestell, num_characters_from_gestell))
        for kombi in alle_kombinationen:
            # word can start from size of word above to one below the row
            # Wort kann von der Größe des Wortes über bis zu einer unter der Zeile beginnen
            for start_pos in range(column - num_characters_from_gestell, column + 1):
                buchstaben_list = list(kombi)
                if start_pos < minc or start_pos + num_characters_from_gestell > maxc:
                    continue
                buchstaben_list.insert(column - start_pos, buchstabe)
                word = ''.join(buchstaben_list)
                if word in alle_woerter:
                    print(word)
                    #Aktuelle Bewegung aus der Ablagebank definieren
                    move = {}
                    worttuple = (word, row, start_pos)
                    for i in buchstaben_list:
                        move[(row, start_pos)] = i
                        start_pos += 1
                    score = punkte_berechnen(worttuple, "right", move)
                    if len(move) == 8:
                        score +=50
                    print(score)
                    if score > best_score:
                        best_score = score
                        best_move = move
                        best_gestell_buchstabe = list(kombi)
                        bestword = word
    return best_move, best_score, best_gestell_buchstabe, bestword


# entgueltige Punkte berechnen
def get_final_scores(gestell_list, scores, player_empty_gestell):
    bonus = 0
    for i in range(len(gestell_list)):
        if gestell_list[i] != []:
            gestell_score = 0
            for buchstabe in gestell_list[i]:
                gestell_score += buchstaben_punkte[buchstabe]
            bonus += gestell_score
            scores[i] -= gestell_score
    if player_empty_gestell is not None:
        scores[player_empty_gestell] += bonus
    return scores

# Gewinner bestimmen
def get_winner(scores, computerplayer):
    max_score = 0
    winner = []
    for i in range(len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            winner = []
            if computerplayer and i == len(scores) - 1:
                winner.append("Computer")
            else:
                winner.append("Player " + str(i+1))
        elif scores[i] == max_score:
            if computerplayer and i == len(scores) - 1:
                winner.append("Computer")
            else:
                winner.append("Player " + str(i+1))
    return ','.join(winner)

def erste_computerzug(gestell):
    bestmove = {}
    bestscore = 0
    best_gestell_buchstabe = []
    bestword = ''
    for num_characters_from_gestell in range(1, 8):
        alle_kombinationen = list(itertools.permutations(gestell, num_characters_from_gestell))
        for kombi in alle_kombinationen:
            wort = ''.join(kombi)
            if wort in alle_woerter:
                reihe = 7
                spalte = 7
                print(wort)
                move = {}
                worttuple = (wort, reihe, spalte)
                for buchstaben in kombi:
                    move[(reihe, spalte)] = buchstaben
                    reihe = reihe + 1
                score = punkte_berechnen(worttuple, "down", move)
                if len(move) == 7:
                    score += 50
                print(score)
                if score > bestscore:
                    bestscore = score
                    bestmove = move
                    best_gestell_buchstabe = list(kombi)
    return bestmove, bestscore, best_gestell_buchstabe, bestword


# Computerzug
def computermove(tilesdict, gestell):
    bestmove = {}
    bestscore = 0
    best_gestell_buchstabe = []
    bestword = ''
    if tilesdict == {}:
        return erste_computerzug(gestell)
    for (r,s) in tilesdict:
        valid_direction = None
        # Spezialfall nur ein Buchstabe auf dem Brett
        if (r, s+1) not in tilesdict and (r, s-1) not in tilesdict and (r-1, s) not in tilesdict and (r+1, s) not in tilesdict:
            valid_direction = 'down'
        if (r,s + 1) in tilesdict or (r,s - 1) in tilesdict:
            if (r + 1, s) not in tilesdict and (r - 1, s) not in tilesdict:
                valid_direction = 'down'
        if (r + 1, s) in tilesdict or (r - 1, s) in tilesdict:
            if (r, s + 1) not in tilesdict and (r, s - 1) not in tilesdict:
                valid_direction = 'right'
        if valid_direction is None:
            continue
        if valid_direction == 'down':
            min_row = r
            max_row = r
            for i in range(1,8):
                if r - i < 0:
                    break
                if (r - i, s - 1) not in tilesdict and (r - i, s + 1) not in tilesdict and (r - i, s) not in tilesdict and (r - i - 1, s) not in tilesdict:
                    min_row -= 1
                else:
                    break
            for i in range(1, 8):
                if r + i > 14:
                    break
                if (r + i, s - 1) not in tilesdict and (r + i, s + 1) not in tilesdict and (r + i, s) not in tilesdict and (r + i + 1, s) not in tilesdict:
                    max_row += 1
                else:
                    break
            if min_row != max_row:
                (move, score, gb, word) = find_move_senkrecht(min_row, max_row, r, s, tilesdict[r,s], gestell)
                if score > bestscore:
                    bestscore = score
                    bestmove = move
                    best_gestell_buchstabe = gb
                    bestword = word
        if valid_direction == 'right':
            min_spalte = s
            max_spalte = s
            for i in range(1, 8):
                if s - i < 0:
                    break
                if (r - 1, s - i) not in tilesdict and (r + 1, s - i) not in tilesdict and (r, s - i) not in tilesdict and (r, s - i - 1) not in tilesdict:
                    min_spalte -= 1
                else:
                    break
            for i in range(1, 8):
                if s + i > 14:
                    break
                if (r - 1, s + i) not in tilesdict and (r + 1, s + i) not in tilesdict and (r, s + i) not in tilesdict  and (r, s + i + 1) not in tilesdict:
                    max_spalte += 1
                else:
                    break
            if min_spalte != max_spalte:
                (move, score, gb, word) = find_move_waagerecht(r, s, min_spalte, max_spalte, tilesdict[r, s], gestell)
                if score > bestscore:
                    bestscore = score
                    bestmove = move
                    best_gestell_buchstabe = gb
                    bestword = word
    return bestmove, bestscore, best_gestell_buchstabe, bestword

# Nachricht anzeigen
def print_message(str, color):
    m = -1.25
    n = 5
    pygame.draw.rect(fenster, color, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2,
                                                 kästchen_größe * 7, kästchen_größe))
    invalid = font2.render(str, True, schwarz)
    fenster.blit(invalid, (abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
    pygame.display.flip()

# Der Computer zeigt die Punkte an und markiert, wer dran ist
def print_players(num_players, currentplayer, computer_player):
    for i in range(num_players):
        is_computer_player = False
        if computer_player:
            if i == num_players - 1:
                is_computer_player = True
        if i == currentplayer:
            print_player(-1.25, i, scores, grün, is_computer_player)
        else:
            print_player(-1.25, i, scores, hellblau, is_computer_player)

# Der Computer sucht alle neuentstandenen Wörter,
# im Fall, dass das gebildete Wort waagerecht ist
def neue_woerter_waagerecht(minrow, mincolumn, maxcolumn, currentm):
    woerter = []
    for c in range(mincolumn, maxcolumn+1):
        if (minrow, c) in buchstabensteine_dictionary:
            continue
        minr=minrow
        maxr = minrow
        while minr > 0 and (minr-1, c) in buchstabensteine_dictionary:
            minr = minr - 1
        while maxr <14 and (maxr+1, c) in buchstabensteine_dictionary:
            maxr = maxr + 1
        if minr == maxr:
            continue
        str = ''
        for r in range(minr, maxr+1):
            if (r, c) in buchstabensteine_dictionary:
                character = buchstabensteine_dictionary[(r, c)]
            else:
                character = currentm[(r, c)]
            str = str + character
        woerter.append((str, minr, c, "down"))
    while mincolumn > 0 and (minrow, mincolumn - 1) in buchstabensteine_dictionary:
        mincolumn -= 1
    while maxcolumn < 14 and (minrow, maxcolumn + 1) in buchstabensteine_dictionary:
        maxcolumn += 1
    str = ''
    for c in range(mincolumn, maxcolumn+1):
        if (minrow, c) in buchstabensteine_dictionary:
            character = buchstabensteine_dictionary[(minrow, c)]
        else:
            character = currentm[(minrow, c)]
        str = str + character
    if len(str) > 1:
        woerter.append((str, minrow, mincolumn, "right"))
    return woerter

# Der Computer sucht alle neuentstandenen Wörter,
# im Fall, dass das gebildete Wort senkrecht ist
def neue_woerter_senkrecht(mincolumn, minrow, maxrow, currentm):
    woerter = []
    for r in range(minrow, maxrow+1):
        if (r, mincolumn) in buchstabensteine_dictionary:
            continue
        minc=mincolumn
        maxc = mincolumn
        while minc > 0 and (r, minc - 1) in buchstabensteine_dictionary:
            minc = minc - 1
        while maxc <14 and (r, maxc+1) in buchstabensteine_dictionary:
            maxc = maxc + 1
        if minc == maxc:
            continue
        str = ''
        for c in range(minc, maxc+1):
            if (r, c) in buchstabensteine_dictionary:
                character = buchstabensteine_dictionary[(r, c)]
            else:
                character = currentm[(r, c)]
            str = str + character
        woerter.append((str, r, minc, "right"))
    while minrow > 0 and (minrow - 1, mincolumn) in buchstabensteine_dictionary:
        minrow -= 1
    while maxrow < 14 and (maxrow + 1, mincolumn) in buchstabensteine_dictionary:
        maxrow += 1
    str = ''
    for r in range(minrow, maxrow+1):
        if (r, mincolumn) in buchstabensteine_dictionary:
            character = buchstabensteine_dictionary[(r, mincolumn)]
        else:
            character = currentm[(r, mincolumn)]
        str = str + character
    if len(str) > 1:
        woerter.append((str, minrow, mincolumn, "down"))
    return woerter

# Prüft, ob die neuentstandenen Wörter gültig sind
def alle_woerter_sind_gueltig(woerter, currentmove):
    score = 0
    falsche_woerter = []
    richtige_woerter = []
    for (w, r, c, direction) in woerter:
        w = w.lower().replace("*", "")
        if w not in alle_woerter:
            falsche_woerter.append(w)
        else:
            richtige_woerter.append(w)
            score += punkte_berechnen((w, r, c), direction, currentmove)
    print("score = ", score)
    if falsche_woerter != []:
        score = -1
    return falsche_woerter, richtige_woerter, score

# Welche Wörter sind entstanden
def neu_woerter_entstanden(currentmove):
    min_column = None
    max_column = None
    min_row = None
    max_row = None
    if currentmove == {}:
        return []
    for (r, c) in currentmove:
        if min_row is None:
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
        return []

    # Fall in dem der Spieler den ersten Zug zieht
    if buchstabensteine_dictionary == {}:
        if (7,7) not in currentmove:
            return []
        str = ''
        if min_row == max_row:
            for c in range(min_column, max_column + 1):
                str = str + currentmove[(min_row, c)]
            return [(str, min_row, min_column, "right")]
        else:
            for r in range(min_row, max_row + 1):
                str = str + currentmove[(r, min_column)]
            return [(str, min_row, min_column, "down")]
    # Fall schon etwas auf dem Brett liegt, in dem der Spieler ein queres Wort bildet
    if min_row == max_row:
        print("came to waagerecht")
        for c in range(min_column, max_column + 1):
            if (min_row, c) not in buchstabensteine_dictionary and (min_row, c) not in currentmove:
                return []
        woerter = neue_woerter_waagerecht(min_row, min_column, max_column, currentmove)

    # Fall in dem der Spieler ein senkrechtes Wort bildet
    elif min_column == max_column:
        print("came to senkrecht")
        for r in range(min_row, max_row + 1):
            if (r, min_column) not in buchstabensteine_dictionary and (r, min_column) not in currentmove:
                return []
        woerter = neue_woerter_senkrecht(min_column, min_row, max_row, currentmove)
    print("Neue woerter => ", woerter)
    # Sonderfall für Nicht-Erster Zug:
    if len(woerter) == 1:
        (wort, row, spalte, d) = woerter[0]
        if len(wort) == len(currentmove):
            print("far away word")
            return []
    if len(woerter) > 1:
        for (wort, row, spalte, d) in woerter:
            if len(wort) == 1:
                pass
                # remove word
    return woerter

# Computer frägt die dritte Frage
def add_computer_player():
    question1 = font4.render('Add computer player (y/n)?', True, neongrün)
    fenster.blit(question1, (50, 550))
    pygame.display.flip()

    # Computer beobachtet, ob der Spieler "y" oder "n" drückt
    computer_player = None
    while True:
        if computer_player is not None:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    print("Key y has been pressed")
                    return True
                if event.key == pygame.K_n:
                    print("Key n has been pressed")
                    return False

# Computer frägt die erste Frage
question1=font4.render('Number of human Players (1-4)?',True,neongrün)
fenster.blit(question1, (50, 200))
pygame.display.flip()

# Computer beobachtet ob der Spieler "2","3" oder "4" drückt
num_players = 0
super_mode = False
while True:
    if num_players!=0:
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("Key 1 has been pressed")
                num_players = 1
                break
            if event.key == pygame.K_2:
                print("Key 2 has been pressed")
                num_players = 2
                break
            if event.key == pygame.K_3:
                num_players = 3
                print("Key 3 has been pressed")
                break
            if event.key == pygame.K_4:
                num_players = 4
                print("Key 4 has been pressed")
            if event.key == pygame.K_0:
                num_players = 4
                super_mode = True
                print("Super Mode on :-) 4 Com")
                break
# Computer schreibt die Antwort der zweiten Frage darunter
if not super_mode:
    answer1= font4.render("You chose " + str(num_players), True, neonblau)
else:
    answer1 = font4.render("Super Mode On, 4 Computers playing!", True, neonblau)
fenster.blit(answer1, (50, 250))
pygame.display.flip()

# Computer frägt die zweite Frage
question1=font4.render('Language? (d für Deutsch, e for english, f pour francais)',True,neongrün)
fenster.blit(question1, (50, 350))
pygame.display.flip()

# Computer beobachtet bis der Spieler "d","e" oder "f" drückt
sprache = None
while True:
    if sprache:
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print("Key d has been pressed")
                sprache = 'de'
                break
            if event.key == pygame.K_e:
                print("Key e has been pressed")
                sprache = 'en'
                break
            if event.key == pygame.K_f:
                sprache = 'fr'
                print("Key f has been pressed")
                break
# Computer schreibt die Antwort der dritten Frage darunter
buchstaben_punkte_bestimmen(sprache)
answer1= font4.render("You chose " + sprache, True, neonblau)
fenster.blit(answer1, (50, 450))
pygame.display.flip()

# Wenn es 2/3 Spieler gibt frägt der Computer, ob man
# einen Computerspieler addieren möchte
computer_player = False
if 1 < num_players < 4 and not super_mode:
    computer_player = add_computer_player()
    if computer_player:
        num_players += 1

# Wenn es nur einen Spieler gibt, muss es einen Computer-Spieler geben
if num_players == 1:
    computer_player = True
    num_players = 2

print_board()
currentplayer = 0
board = erstelle_brettliste()

alle_woerter = wörterbuch_lesen(sprache)
bag = erstelle_beutel(sprache)
gestell = []
scores = []
for player in range(num_players):
    gestell.append([])
    fülle_ablagebank(bag, 7, gestell[player])
    scores.append(0)

# Zusätzlichen Tasten werden gedruckt
print_button(15, 10, "PASS", hellblau)
print_button(15, 11, "RENEW", hellblau)
print_button(15, 12, "BACK", hellblau)
print_button(15, 13, "DONE", hellblau)
print_button(-1.25, 13, "SHOW", hellblau)
print_button(-1.25, 14, "HIDE", hellblau)
print_players(num_players, currentplayer, computer_player)
buchstabensteine_dictionary = {}
letters_on_board()
pygame.display.update()

# Spielablauf
currentmove={}
if super_mode:
    buchstabensteine_dictionary[(7, 7)]= 'a'
print(gestell)
renew_is_active = False
renew_letters = []
passcount = 0

while True:
    if passcount >= 3 * num_players:
        get_final_scores(gestell, scores, None)
        x = get_winner(scores, computer_player)
        print_players(num_players, currentplayer, computer_player)
        print_message("Game over! Winner(s): " + x, gold)
        break
    for i in range(len(gestell)):
        if gestell[i] == [] and bag == []:
            get_final_scores(gestell, scores, i)
            x = get_winner(scores, computer_player)
            print_players(num_players, currentplayer, computer_player)
            print_message("Game over! Winner(s): " + x, gold)
            break
    if super_mode or (computer_player and currentplayer == num_players-1):
        (currentmove, score, gestell_buchstaben, word) = computermove(buchstabensteine_dictionary, gestell[currentplayer])
        print("Computer's move = ", currentmove, score, gestell[currentplayer])
        # Fall, wo der Computer nichts machen kann...
        if currentmove == {}:
            for gestell_letter in gestell[currentplayer]:
                bag.append(gestell_letter[0])
            random.shuffle(bag)
            gestell[currentplayer] = []
            fülle_ablagebank(bag, 7, gestell[currentplayer])
            print_message("Computer pass.", grün)
            passcount += 1
        else:
            passcount = 0
            for (row, column) in currentmove:
                buchstabensteine_dictionary[(row, column)] = currentmove[(row, column)]
            scores[currentplayer] += score
            for i in gestell_buchstaben:
                gestell[currentplayer].remove(i)
            fülle_ablagebank(bag, 7 - len(gestell[currentplayer]), gestell[currentplayer])
            # for (row, column) in currentmove:
            #    tilesdict[(row, column)] = currentmove[(row, column)]
            print_message("Computer moved " + word + " and got " + str(score) + " points.", grün)
        letters_on_board()
        currentmove = {}
        currentplayer = (currentplayer + 1) % num_players
        print_players(num_players, currentplayer, computer_player)
        # possible = get_valid_words_2(row, spalte, valid_direction)
        # (bestwort, max_points, tilerow, tilespalte) = get_best_word(possible, d, board, tilesdict)
        # print(bestwort)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            print(markierter_buchstabenstein, gestell[currentplayer][markierte_spalte])
            if markierter_buchstabenstein[0] == '*':
                if pygame.K_a <= event.key <= pygame.K_z:
                    gestell[currentplayer][markierte_spalte] = '*' + chr(ord('a') + event.key - pygame.K_a)
                    print("changing * to ", gestell[currentplayer][markierte_spalte])
                    highlight_gestell(row, column, gestell[currentplayer][column])
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x -= abstand
            y -= abstand
            column = int(x // kästchen_größe)
            row = int(y // kästchen_größe)
            # Fall, wo Ablagebank angeklickt wird
            if row == 15 and 0 <= column < len(gestell[currentplayer]):
                if not renew_is_active:
                    print(gestell[currentplayer][column])
                    highlight_gestell(row, column, gestell[currentplayer][column])
                    print_message((""), dunkelgrün)
                if renew_is_active:
                    highlight_gestell_helper(lila, lila, row, column, gestell[currentplayer][column])
                    renew_letters.append(gestell[currentplayer][column])
            else:
                # Fall, wo man einen Buchstaben auf das Brett überträgt
                if markierte_reihe>0 and 0 <= row < 15 and 0 <= column < 15 and (row, column) not in buchstabensteine_dictionary and (row, column) not in currentmove:
                    if markierter_buchstabenstein == '*':
                        print_message("Please assign Blanko before moving.", rot)
                        row = markierte_reihe
                        column = markierte_spalte
                        break
                    currentmove[(row, column)]=markierter_buchstabenstein
                    print(markierte_reihe)
                    paint_tile_with_letter(row, column, markierter_buchstabenstein, pink)
                    gestell[currentplayer].pop(markierte_spalte)
                    markierte_reihe=0
                    markierte_spalte=0
                    print_gestell(gestell[currentplayer])
                # Fall, wo cancel gedruckt wird
                if ((row, column)) == (15,12):
                    letters_on_board()
                    for (row, column) in currentmove:
                        kästchen_drucken(row, column)
                        gestell[currentplayer].append(currentmove[(row, column)])
                    currentmove={}
                    renew_letters = []
                    print_gestell(gestell[currentplayer])
                    print_message((""), dunkelgrün)
                    renew_is_active = False
                # Fall, wo renew gedruckt wird
                if ((row, column)) == (15, 11):
                    if currentmove != {}:
                        print_message("Please press Back before Renew", rot)
                        break
                    if renew_is_active:
                        print_message("Please press Done to finish Renew", rot)
                        break
                    renew_is_active = True

                # Fall, wo pass gedruckt wird
                if ((row, column)) == (15, 10):
                    letters_on_board()
                    for (row, column) in currentmove:
                        kästchen_drucken(row, column)
                        gestell[currentplayer].append(currentmove[(row, column)])
                    currentplayer = (currentplayer + 1) % num_players
                    for i in range(len(gestell[currentplayer])):
                        remove_from_gestell(15, i)
                    print_message(("You passed"), grün)
                    currentmove={}
                    print_players(num_players, currentplayer, computer_player)
                    passcount += 1
                # Fall, wo done gedruckt wird
                if ((row, column)) == (15, 13):
                    markierter_buchstabenstein = ' '
                    markierte_spalte = 0
                    markierte_reihe = 0
                    passcount = 0
                    if renew_is_active:
                        if renew_letters == []:
                            print_message("Please select letters to renew", rot)
                            break
                        else:
                            for letter in renew_letters:
                                bag.append(letter[0])
                                gestell[currentplayer].remove(letter)
                            random.shuffle(bag)
                            fülle_ablagebank(bag, len(renew_letters), gestell[currentplayer])
                            renew_is_active = False
                            currentplayer = (currentplayer + 1) % num_players
                            print_players(num_players, currentplayer, computer_player)
                            for i in range(len(gestell[currentplayer])):
                                remove_from_gestell(15, i)
                            renew_letters = []
                        break
                    else:
                        woerter = neu_woerter_entstanden(currentmove)
                        if woerter == []:
                            print_message("Invalid move", rot)
                        else:
                            falsche_woerter, richtig_woerter, score = alle_woerter_sind_gueltig(woerter, currentmove)
                            if score < 0:
                                print_message(
                                    str(len(falsche_woerter)) + "invalid word(s): " + ','.join(falsche_woerter), rot)
                                continue
                            print_message(
                                "Good move. You got " + str(score) + " points for " + ','.join(richtig_woerter), grün)
                            fülle_ablagebank(bag, 7 - len(gestell[currentplayer]), gestell[currentplayer])
                            scores[currentplayer] += score
                            currentplayer = (currentplayer + 1) % num_players
                            print_players(num_players, currentplayer, computer_player)
                            for i in range(len(gestell[currentplayer])):
                                remove_from_gestell(15, i)
                            for (row, column) in currentmove:
                                buchstabensteine_dictionary[(row, column)] = currentmove[(row, column)]
                            letters_on_board()
                            currentmove = {}
                if ((row, column)) == (-1, 13):
                    print("came here")
                    print_gestell(gestell[currentplayer])
                if ((row, column)) == (-1, 14):
                    for i in range(len(gestell[currentplayer])):
                        remove_from_gestell(15, i)
        else:
            pass

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()