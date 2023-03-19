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
hautfarbe=(255, 210, 120)
neongrün=(223,255,0)
pygame.init()
pygame.display.init()
pygame.font.init()

# Variabeln, die später gebraucht werden
bildschirm_größe = 2
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
            if brett[reihe][s] == '00' or brett[reihe][s] == '--':
                punkte = punkte + buchstaben_punkte[buchstabe_auf_brett]
            if brett[reihe][s] == 'DL':
                if (reihe, s) in buchstabensteine_dictionary:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett])
                else:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett] * 2)
            if brett[reihe][s] == 'TL':
                if (reihe, s) in buchstabensteine_dictionary:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett])
                else:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett] * 3)
            if brett[reihe][s] == 'DW':
                punkte = punkte + buchstaben_punkte[buchstabe_auf_brett]
                if not (reihe, s) in buchstabensteine_dictionary:
                    insgesamt = 2
            if brett[reihe][s] == 'TW':
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
            print("came with", buchstabe_auf_brett, buchstaben_punkte[buchstabe_auf_brett], r, spalte, brett[r][spalte])
            if brett[r][spalte] == '00' or brett[r][spalte] == '--':
                punkte = punkte + buchstaben_punkte[buchstabe_auf_brett]
            if brett[r][spalte] == 'DL':
                if (r, spalte) in buchstabensteine_dictionary:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett])
                else:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett] * 2)
            if brett[r][spalte] == 'TL':
                if (r, spalte) in buchstabensteine_dictionary:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett])
                else:
                    punkte = punkte + (buchstaben_punkte[buchstabe_auf_brett] * 3)
            if brett[r][spalte] == 'DW':
                punkte = punkte + buchstaben_punkte[buchstabe_auf_brett]
                if not (r, spalte) in buchstabensteine_dictionary:
                    insgesamt = 2
            if brett[r][spalte] == 'TW':
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
def drucke_brett():
    fenster.fill(dunkelgrün)
    for m in range(0,15):
        for n in range(0,15):
            kästchen_drucken(m, n)
    pygame.display.flip()

# Ablagebank wird gedruckt
def drucke_ablagebank(ablagebank):
    m=15
    n=0
    pygame.draw.rect(fenster, dunkelgrün2, pygame.Rect(abstand + n * kästchen_größe, abstand + m * kästchen_größe, kästchen_größe * 7, kästchen_größe))
    for i in ablagebank:
        pygame.draw.rect(fenster, weiß, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2))
        pygame.draw.rect(fenster, schwarz, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2), 3)
        buchstabe = font3.render(i.upper(), True, schwarz)
        points = font3.render(str(buchstaben_punkte[i[0]]), True, schwarz)
        fenster.blit(buchstabe, (abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
        fenster.blit(points, (abstand + n * kästchen_größe + abstand2 + kästchen_größe / 2, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 2))
        n += 1
    pygame.display.flip()

# Einen Buchstaben von der Ablagebank entfernen
def entferne_von_der_ablagebank(m, n):
    pygame.draw.rect(fenster, dunkelgrün2,
                     pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2,
                                 kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2))
    pygame.display.flip()

# Hilfe, um den angeklickten Buchstaben auf der Ablagebank zu markieren
def helfer_fuer_markierte_buchstaben(color1, color2, m, n, i):
    pygame.draw.rect(fenster, color1,
                     pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2,
                                 kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2))
    pygame.draw.rect(fenster, color2,
                     pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2,
                                 kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2), 3)
    buchstabe = font3.render(i.upper(), True, schwarz)
    points = font3.render(str(buchstaben_punkte[i[0]]), True, schwarz)
    fenster.blit(buchstabe, (
        abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
    fenster.blit(points, (
        abstand + n * kästchen_größe + abstand2 + kästchen_größe / 2, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 2))
    pygame.display.flip()

# Den angeklickten Buchstaben auf der Ablagebank markieren
def markiere_buchstaben(row, column, tile):
    global markierte_reihe, markierte_spalte, markierter_buchstabenstein
    if markierte_reihe != 0:
        helfer_fuer_markierte_buchstaben(weiß, schwarz, markierte_reihe, markierte_spalte, markierter_buchstabenstein)
    helfer_fuer_markierte_buchstaben(gelb, gelb, row, column, tile)
    markierte_reihe = row
    markierte_spalte = column
    markierter_buchstabenstein = tile

# Einen Buchstaben auf dem Brett malen
def drucke_kaestchen_mit_buchstabe(row, column, tile, color):
    margin2 = 10 // bildschirm_größe
    pygame.draw.rect(fenster, color,
                     pygame.Rect(abstand + column * kästchen_größe + margin2, abstand + row * kästchen_größe + margin2, kästchen_größe - margin2 * 2, kästchen_größe - margin2 * 2))
    pygame.draw.rect(fenster, schwarz, pygame.Rect(abstand + column * kästchen_größe + margin2, abstand + row * kästchen_größe + margin2, kästchen_größe - margin2 * 2, kästchen_größe - margin2 * 2), 3)
    buchstabe = font3.render(tile.upper(), True, schwarz)
    punkte = font3.render((str(buchstaben_punkte[tile[0]])), True, schwarz)
    fenster.blit(buchstabe, (
        abstand + column * kästchen_größe + margin2 + kästchen_größe / 4, abstand + row * kästchen_größe + margin2 + kästchen_größe / 4))
    fenster.blit(punkte, (
        abstand + column * kästchen_größe + margin2 + kästchen_größe / 2, abstand + row * kästchen_größe + margin2 + kästchen_größe / 2))
    pygame.display.flip()

# Aktuelles Brett drucken
def aktualisiere_brett():
    for kordinat in buchstabensteine_dictionary:
        (m,n)=kordinat
        pygame.draw.rect(fenster, weiß, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2))
        pygame.draw.rect(fenster, schwarz, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe - abstand2 * 2, kästchen_größe - abstand2 * 2), 3)
        buchstabe = font3.render((str(buchstabensteine_dictionary[kordinat])).upper(), True, schwarz)
        punkte = font3.render((str(buchstaben_punkte[(buchstabensteine_dictionary[kordinat][0]).lower()])), True, schwarz)
        fenster.blit(buchstabe, (abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
        fenster.blit(punkte, (abstand + n * kästchen_größe + abstand2 + kästchen_größe / 2, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 2))
    pygame.display.flip()

# Spielknöpfe drucken
def drucke_knopf(m, n, text, farbe):
    pygame.draw.rect(fenster, farbe, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe, kästchen_größe))
    pygame.draw.rect(fenster, schwarz, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe, kästchen_größe), 3)
    text = font3.render(text, True, schwarz)
    fenster.blit(text, (
        abstand + n * kästchen_größe + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
    pygame.display.flip()

# aktuellen Spieler anzeigen
def drucke_spieler(m, n, punktestand, farbe, computer_spieler_dabei):
    pygame.draw.rect(fenster, farbe, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe, kästchen_größe))
    pygame.draw.rect(fenster, schwarz, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2, kästchen_größe, kästchen_größe), 3)
    if computer_spieler_dabei:
        text = font2.render("COM", True, schwarz)
    else:
        text = font2.render("P" + str(n + 1), True, schwarz)
    fenster.blit(text, (
        abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
    punkte = font2.render(str(punktestand[n]), True, schwarz)
    fenster.blit(punkte, (
        abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + 3 * kästchen_größe / 5))
    pygame.display.flip()


# senkrechten Zug suchen
def bestimme_wort_senkrecht(min_reihe, max_reihe, reihe, spalte, buchstabe, ablagebank):
    meisten_punkte = 0
    bester_zug = {}
    buchstaben_des_besten_zuges = []
    beste_wort = ''
    maximale_buchstaben_der_ablagebank = min(7, max_reihe - min_reihe)
    for anzahl_der_buchstaben_der_ablagebank in range(1, maximale_buchstaben_der_ablagebank + 1):
        alle_kombinationen = list(itertools.permutations(ablagebank, anzahl_der_buchstaben_der_ablagebank))
        for kombi in alle_kombinationen:
            # word can start from size of word above to one below the row
            for start_pos in range(reihe - anzahl_der_buchstaben_der_ablagebank, reihe + 1):
                buchstaben_liste = list(kombi)
                # wenn das Wort nicht auf dem Brett ist
                if start_pos < min_reihe or start_pos + anzahl_der_buchstaben_der_ablagebank > max_reihe:
                    continue
                buchstaben_liste.insert(reihe - start_pos, buchstabe)
                wort = ''.join(buchstaben_liste)
                if wort in alle_woerter:
                    print(wort)
                    # Aktuelle Bewegung aus der Ablagebank definieren
                    zug = {}
                    worttuple = (wort, start_pos, spalte)
                    for i in buchstaben_liste:
                        zug[(start_pos, spalte)] = i
                        start_pos += 1
                    erhaltene_punkte = punkte_berechnen(worttuple, "down", zug)
                    if len(zug) == 8:
                        erhaltene_punkte += 50
                    print(erhaltene_punkte)
                    if erhaltene_punkte > meisten_punkte:
                        meisten_punkte = erhaltene_punkte
                        bester_zug = zug
                        buchstaben_des_besten_zuges = list(kombi)
                        beste_wort = wort
    return bester_zug, meisten_punkte, buchstaben_des_besten_zuges, beste_wort

# waagerechten Zug suchen
def bestimme_wort_waagerecht(reihe, spalte, min_spalte, max_spalte, buchstabe, ablagebank):
    meisten_punkte = 0
    bester_zug = {}
    buchstaben_des_besten_zuges = []
    bestes_wort = ''
    maximale_buchstaben_der_ablagebank = min(7, max_spalte - min_spalte)
    for anzahl_der_buchstaben_der_ablagebank in range(1, maximale_buchstaben_der_ablagebank + 1):
        alle_kombinationen = list(itertools.permutations(ablagebank, anzahl_der_buchstaben_der_ablagebank))
        for kombi in alle_kombinationen:
            # word can start from size of word above to one below the row
            # Wort kann von der Größe des Wortes über bis zu einer unter der Zeile beginnen
            for start_pos in range(spalte - anzahl_der_buchstaben_der_ablagebank, spalte + 1):
                buchstaben_liste = list(kombi)
                if start_pos < min_spalte or start_pos + anzahl_der_buchstaben_der_ablagebank > max_spalte:
                    continue
                buchstaben_liste.insert(spalte - start_pos, buchstabe)
                wort = ''.join(buchstaben_liste)
                if wort.lower().replace("*", "e") in alle_woerter:
                    print(wort)
                    # Aktuelle Bewegung aus der Ablagebank definieren
                    zug = {}
                    worttuple = (wort, reihe, start_pos)
                    for i in buchstaben_liste:
                        zug[(reihe, start_pos)] = i
                        start_pos += 1
                    erhaltene_punkte = punkte_berechnen(worttuple, "right", zug)
                    if len(zug) == 8:
                        erhaltene_punkte +=50
                    print(erhaltene_punkte)
                    if erhaltene_punkte > meisten_punkte:
                        meisten_punkte = erhaltene_punkte
                        bester_zug = zug
                        buchstaben_des_besten_zuges = list(kombi)
                        bestes_wort = wort
    return bester_zug, meisten_punkte, buchstaben_des_besten_zuges, bestes_wort


# entgueltige Punkte berechnen
def endpunktestand_berechnen(ablagebaenke, punkte, spieler_mit_leerer_ablagebank):
    bonus = 0
    for i in range(len(ablagebaenke)):
        if ablagebaenke[i]:
            ablagebank_punkte = 0
            for buchstabe in ablagebaenke[i]:
                ablagebank_punkte += buchstaben_punkte[buchstabe]
            bonus += ablagebank_punkte
            punkte[i] -= ablagebank_punkte
    if spieler_mit_leerer_ablagebank is not None:
        punkte[spieler_mit_leerer_ablagebank] += bonus
    return punkte

# Gewinner bestimmen
def gewinner_bestimmen(punkte, computerspieler):
    max_punkte = 0
    gewinner = []
    for i in range(len(punkte)):
        if punkte[i] > max_punkte:
            max_punkte = punkte[i]
            gewinner = []
            if computerspieler and i == len(punkte) - 1:
                gewinner.append("Computer")
            else:
                gewinner.append("Player " + str(i+1))
        elif punkte[i] == max_punkte:
            if computerspieler and i == len(punkte) - 1:
                gewinner.append("Computer")
            else:
                gewinner.append("Player " + str(i+1))
    return ','.join(gewinner)

def erste_computerzug(ablagebank):
    bester_zug = {}
    meisten_punkte = 0
    buchstaben_des_besten_zuges = []
    bestes_wort = ''
    for anzahl_der_buchstaben_der_ablagebank in range(1, 8):
        alle_kombinationen = list(itertools.permutations(ablagebank, anzahl_der_buchstaben_der_ablagebank))
        for kombi in alle_kombinationen:
            wort = ''.join(kombi)
            if wort in alle_woerter:
                reihe = 7
                spalte = 7
                print(wort)
                zug = {}
                worttuple = (wort, reihe, spalte)
                for buchstaben in kombi:
                    zug[(reihe, spalte)] = buchstaben
                    reihe = reihe + 1
                punkte = punkte_berechnen(worttuple, "down", zug)
                if len(zug) == 7:
                    punkte += 50
                print(punkte)
                if punkte > meisten_punkte:
                    meisten_punkte = punkte
                    bester_zug = zug
                    buchstaben_des_besten_zuges = list(kombi)
    return bester_zug, meisten_punkte, buchstaben_des_besten_zuges, bestes_wort


# Computerzug
def computerzug(buchstabensteine_dictionary, ablagebank):
    bester_zug = {}
    meisten_punkte = 0
    buchstaben_des_besten_zuges = []
    bestes_wort = ''
    if buchstabensteine_dictionary == {}:
        return erste_computerzug(ablagebank)
    for (r,s) in buchstabensteine_dictionary:
        wort_richtung = None
        # Spezialfall nur ein Buchstabe auf dem Brett
        if (r, s+1) not in buchstabensteine_dictionary and (r, s - 1) not in buchstabensteine_dictionary and (r - 1, s) not in buchstabensteine_dictionary and (r + 1, s) not in buchstabensteine_dictionary:
            wort_richtung = 'down'
        if (r,s + 1) in buchstabensteine_dictionary or (r, s - 1) in buchstabensteine_dictionary:
            if (r + 1, s) not in buchstabensteine_dictionary and (r - 1, s) not in buchstabensteine_dictionary:
                wort_richtung = 'down'
        if (r + 1, s) in buchstabensteine_dictionary or (r - 1, s) in buchstabensteine_dictionary:
            if (r, s + 1) not in buchstabensteine_dictionary and (r, s - 1) not in buchstabensteine_dictionary:
                wort_richtung = 'right'
        if wort_richtung is None:
            continue
        if wort_richtung == 'down':
            min_reihe = r
            max_reihe = r
            for i in range(1,8):
                if r - i < 0:
                    break
                if (r - i, s - 1) not in buchstabensteine_dictionary and (r - i, s + 1) not in buchstabensteine_dictionary and (r - i, s) not in buchstabensteine_dictionary and (r - i - 1, s) not in buchstabensteine_dictionary:
                    min_reihe -= 1
                else:
                    break
            for i in range(1, 8):
                if r + i > 14:
                    break
                if (r + i, s - 1) not in buchstabensteine_dictionary and (r + i, s + 1) not in buchstabensteine_dictionary and (r + i, s) not in buchstabensteine_dictionary and (r + i + 1, s) not in buchstabensteine_dictionary:
                    max_reihe += 1
                else:
                    break
            if min_reihe != max_reihe:
                (zug, punkte, bbz, wort) = bestimme_wort_senkrecht(min_reihe, max_reihe, r, s, buchstabensteine_dictionary[r, s], ablagebank)
                if punkte > meisten_punkte:
                    meisten_punkte = punkte
                    bester_zug = zug
                    buchstaben_des_besten_zuges = bbz
                    bestes_wort = wort
        if wort_richtung == 'right':
            min_spalte = s
            max_spalte = s
            for i in range(1, 8):
                if s - i < 0:
                    break
                if (r - 1, s - i) not in buchstabensteine_dictionary and (r + 1, s - i) not in buchstabensteine_dictionary and (r, s - i) not in buchstabensteine_dictionary and (r, s - i - 1) not in buchstabensteine_dictionary:
                    min_spalte -= 1
                else:
                    break
            for i in range(1, 8):
                if s + i > 14:
                    break
                if (r - 1, s + i) not in buchstabensteine_dictionary and (r + 1, s + i) not in buchstabensteine_dictionary and (r, s + i) not in buchstabensteine_dictionary  and (r, s + i + 1) not in buchstabensteine_dictionary:
                    max_spalte += 1
                else:
                    break
            if min_spalte != max_spalte:
                (zug, punkte, bbz, wort) = bestimme_wort_waagerecht(r, s, min_spalte, max_spalte, buchstabensteine_dictionary[r, s], ablagebank)
                if punkte > meisten_punkte:
                    meisten_punkte = punkte
                    bester_zug = zug
                    buchstaben_des_besten_zuges = bbz
                    bestes_wort = wort
    return bester_zug, meisten_punkte, buchstaben_des_besten_zuges, bestes_wort

# Nachricht anzeigen
def nachricht_drucken(str, color):
    m = -1.25
    n = 5
    pygame.draw.rect(fenster, color, pygame.Rect(abstand + n * kästchen_größe + abstand2, abstand + m * kästchen_größe + abstand2,
                                                 kästchen_größe * 7, kästchen_größe))
    invalid = font2.render(str, True, schwarz)
    fenster.blit(invalid, (abstand + n * kästchen_größe + abstand2 + kästchen_größe / 4, abstand + m * kästchen_größe + abstand2 + kästchen_größe / 4))
    pygame.display.flip()

# Der Computer zeigt die Punkte an und markiert, wer dran ist
def spieler_drucken(anzahl_spieler, aktueller_spieler, computer_spieler):
    for i in range(anzahl_spieler):
        is_computer_player = False
        if computer_spieler:
            if i == anzahl_spieler - 1:
                is_computer_player = True
        if i == aktueller_spieler:
            drucke_spieler(-1.25, i, punktestand, grün, is_computer_player)
        else:
            drucke_spieler(-1.25, i, punktestand, hellblau, is_computer_player)

# Der Computer sucht alle neuentstandenen Wörter,
# im Fall, dass das gebildete Wort waagerecht ist
def neue_woerter_waagerecht(minreihe, minspalte, maxspalte, aktueller_zug):
    woerter = []
    for c in range(minspalte, maxspalte + 1):
        if (minreihe, c) in buchstabensteine_dictionary:
            continue
        minr=minreihe
        maxr = minreihe
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
                character = aktueller_zug[(r, c)]
            str = str + character
        woerter.append((str, minr, c, "down"))
    while minspalte > 0 and (minreihe, minspalte - 1) in buchstabensteine_dictionary:
        minspalte -= 1
    while maxspalte < 14 and (minreihe, maxspalte + 1) in buchstabensteine_dictionary:
        maxspalte += 1
    str = ''
    for c in range(minspalte, maxspalte + 1):
        if (minreihe, c) in buchstabensteine_dictionary:
            character = buchstabensteine_dictionary[(minreihe, c)]
        else:
            character = aktueller_zug[(minreihe, c)]
        str = str + character
    if len(str) > 1:
        woerter.append((str, minreihe, minspalte, "right"))
    return woerter

# Der Computer sucht alle neuentstandenen Wörter,
# im Fall, dass das gebildete Wort senkrecht ist
def neue_woerter_senkrecht(minspalte, minreihe, maxreihe, aktueller_zug):
    woerter = []
    for r in range(minreihe, maxreihe + 1):
        if (r, minspalte) in buchstabensteine_dictionary:
            continue
        mins=minspalte
        maxs = minspalte
        while mins > 0 and (r, mins - 1) in buchstabensteine_dictionary:
            mins = mins - 1
        while maxs <14 and (r, maxs+1) in buchstabensteine_dictionary:
            maxs = maxs + 1
        if mins == maxs:
            continue
        str = ''
        for s in range(mins, maxs+1):
            if (r, s) in buchstabensteine_dictionary:
                buchstabe = buchstabensteine_dictionary[(r, s)]
            else:
                buchstabe = aktueller_zug[(r, s)]
            str = str + buchstabe
        woerter.append((str, r, mins, "right"))
    while minreihe > 0 and (minreihe - 1, minspalte) in buchstabensteine_dictionary:
        minreihe -= 1
    while maxreihe < 14 and (maxreihe + 1, minspalte) in buchstabensteine_dictionary:
        maxreihe += 1
    str = ''
    for r in range(minreihe, maxreihe + 1):
        if (r, minspalte) in buchstabensteine_dictionary:
            buchstabe = buchstabensteine_dictionary[(r, minspalte)]
        else:
            buchstabe = aktueller_zug[(r, minspalte)]
        str = str + buchstabe
    if len(str) > 1:
        woerter.append((str, minreihe, minspalte, "down"))
    return woerter

# Prüft, ob die neuentstandenen Wörter gültig sind
def alle_woerter_sind_gueltig(woerter, currentmove):
    punkte = 0
    falsche_woerter = []
    richtige_woerter = []
    for (w, r, c, direction) in woerter:
        w = w.lower().replace("*", "")
        if w not in alle_woerter:
            falsche_woerter.append(w)
        else:
            richtige_woerter.append(w)
            punkte += punkte_berechnen((w, r, c), direction, currentmove)
    print("score = ", punkte)
    if falsche_woerter != []:
        punkte = -1
    return falsche_woerter, richtige_woerter, punkte

# Welche Wörter sind entstanden
def neu_woerter_entstanden(aktueller_zug):
    min_spalte = None
    max_spalte = None
    min_reihe = None
    max_reihe = None
    if aktueller_zug == {}:
        return []
    for (r, s) in aktueller_zug:
        if min_reihe is None:
            min_reihe = max_reihe = r
            min_spalte = max_spalte = s
        if r < min_reihe:
            min_reihe = r
        if r > max_reihe:
            max_reihe = r
        if s < min_spalte:
            min_spalte = s
        if s > max_spalte:
            max_spalte = s
    if min_reihe != max_reihe and min_spalte != max_spalte:
        return []

    # Fall in dem der Spieler den ersten Zug zieht
    if buchstabensteine_dictionary == {}:
        if (7,7) not in aktueller_zug:
            return []
        str = ''
        if min_reihe == max_reihe:
            for s in range(min_spalte, max_spalte + 1):
                str = str + aktueller_zug[(min_reihe, s)]
            return [(str, min_reihe, min_spalte, "right")]
        else:
            for r in range(min_reihe, max_reihe + 1):
                str = str + aktueller_zug[(r, min_spalte)]
            return [(str, min_reihe, min_spalte, "down")]
    # Fall schon etwas auf dem Brett liegt, in dem der Spieler ein queres Wort bildet
    if min_reihe == max_reihe:
        print("came to waagerecht")
        for s in range(min_spalte, max_spalte + 1):
            if (min_reihe, s) not in buchstabensteine_dictionary and (min_reihe, s) not in aktueller_zug:
                return []
        woerter = neue_woerter_waagerecht(min_reihe, min_spalte, max_spalte, aktueller_zug)

    # Fall in dem der Spieler ein senkrechtes Wort bildet
    elif min_spalte == max_spalte:
        print("came to senkrecht")
        for r in range(min_reihe, max_reihe + 1):
            if (r, min_spalte) not in buchstabensteine_dictionary and (r, min_spalte) not in aktueller_zug:
                return []
        woerter = neue_woerter_senkrecht(min_spalte, min_reihe, max_reihe, aktueller_zug)
    print("Neue woerter => ", woerter)
    # Sonderfall für Nicht-Erster Zug:
    if len(woerter) == 1:
        (wort, reihe, spalte, d) = woerter[0]
        if len(wort) == len(aktueller_zug):
            print("far away word")
            return []
    if len(woerter) > 1:
        for (wort, reihe, spalte, d) in woerter:
            if len(wort) == 1:
                pass
                # remove word
    return woerter

# Computer frägt die dritte Frage
def computer_spieler_hinzufuegen():
    frage = font4.render('Add computer player (y/n)?', True, neongrün)
    fenster.blit(frage, (50, 550))
    pygame.display.flip()

    # Computer beobachtet, ob der Spieler "y" oder "n" drückt
    computer_spieler = None
    while True:
        if computer_spieler is not None:
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
frage=font4.render('Number of human Players (1-4)?', True, neongrün)
fenster.blit(frage, (50, 200))
pygame.display.flip()

# Computer beobachtet ob der Spieler "2","3" oder "4" drückt
anzahl_spieler = 0
super_modus = False
while True:
    if anzahl_spieler:
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("Key 1 has been pressed")
                anzahl_spieler = 1
                break
            if event.key == pygame.K_2:
                print("Key 2 has been pressed")
                anzahl_spieler = 2
                break
            if event.key == pygame.K_3:
                anzahl_spieler = 3
                print("Key 3 has been pressed")
                break
            if event.key == pygame.K_4:
                anzahl_spieler = 4
                print("Key 4 has been pressed")
                break
            if event.key == pygame.K_0:
                anzahl_spieler = 4
                super_modus = True
                print("Super Mode on :-) 4 Com")
                break
            nachricht_drucken('ungueltig', hautfarbe)

nachricht_drucken('', schwarz)

# Computer schreibt die Antwort der zweiten Frage darunter
if not super_modus:
    antwort= font4.render("You chose " + str(anzahl_spieler), True, neonblau)
else:
    antwort = font4.render("Super Mode On, 4 Computers playing!", True, neonblau)
fenster.blit(antwort, (50, 250))
pygame.display.flip()

# Computer frägt die zweite Frage
frage=font4.render('Language? (d für Deutsch, e for english, f pour francais)', True, neongrün)
fenster.blit(frage, (50, 350))
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
antwort= font4.render("You chose " + sprache, True, neonblau)
fenster.blit(antwort, (50, 450))
pygame.display.flip()

# Wenn es 2/3 Spieler gibt frägt der Computer, ob man
# einen Computerspieler addieren möchte
computer_spieler = False
if 1 < anzahl_spieler < 4 and not super_modus:
    computer_spieler = computer_spieler_hinzufuegen()
    if computer_spieler:
        anzahl_spieler += 1

# Wenn es nur einen Spieler gibt, muss es einen Computer-Spieler geben
if anzahl_spieler == 1:
    computer_spieler = True
    anzahl_spieler = 2

drucke_brett()
aktueller_spieler = 0
brett = erstelle_brettliste()

alle_woerter = wörterbuch_lesen(sprache)
beutel = erstelle_beutel(sprache)
ablagebank = []
punktestand = []
for player in range(anzahl_spieler):
    ablagebank.append([])
    fülle_ablagebank(beutel, 7, ablagebank[player])
    punktestand.append(0)

# Zusätzlichen Tasten werden gedruckt
drucke_knopf(15, 10, "PASS", hellblau)
drucke_knopf(15, 11, "RENEW", hellblau)
drucke_knopf(15, 12, "BACK", hellblau)
drucke_knopf(15, 13, "DONE", hellblau)
drucke_knopf(-1.25, 13, "SHOW", hellblau)
drucke_knopf(-1.25, 14, "HIDE", hellblau)
spieler_drucken(anzahl_spieler, aktueller_spieler, computer_spieler)
buchstabensteine_dictionary = {}
aktualisiere_brett()
pygame.display.update()

# Spielablauf
aktueller_zug={}
print(ablagebank)
renew_modus = False
renew_buchstaben = []
anzahl_pass = 0

while True:
    if anzahl_pass >= 3 * anzahl_spieler:
        endpunktestand_berechnen(ablagebank, punktestand, None)
        x = gewinner_bestimmen(punktestand, computer_spieler)
        spieler_drucken(anzahl_spieler, aktueller_spieler, computer_spieler)
        nachricht_drucken("Game over! Winner(s): " + x, gold)
        break
    for i in range(len(ablagebank)):
        if ablagebank[i] == [] and beutel == []:
            endpunktestand_berechnen(ablagebank, punktestand, i)
            x = gewinner_bestimmen(punktestand, computer_spieler)
            spieler_drucken(anzahl_spieler, aktueller_spieler, computer_spieler)
            nachricht_drucken("Game over! Winner(s): " + x, gold)
            break
    if super_modus or (computer_spieler and aktueller_spieler == anzahl_spieler - 1):
        (aktueller_zug, score, ablagebank_buchstaben, word) = computerzug(buchstabensteine_dictionary, ablagebank[aktueller_spieler])
        print("Computer's move = ", aktueller_zug, score, ablagebank[aktueller_spieler])
        # Fall, wo der Computer nichts machen kann...
        if aktueller_zug == {}:
            for ablagebank_buchstabe in ablagebank[aktueller_spieler]:
                beutel.append(ablagebank_buchstabe[0])
            random.shuffle(beutel)
            ablagebank[aktueller_spieler] = []
            fülle_ablagebank(beutel, 7, ablagebank[aktueller_spieler])
            nachricht_drucken("Computer pass.", grün)
            anzahl_pass += 1
        else:
            anzahl_pass = 0
            for (reihe, spalte) in aktueller_zug:
                if aktueller_zug[(reihe, spalte)] == '*':
                    buchstabensteine_dictionary[(reihe, spalte)] = '*e'
                else:
                    buchstabensteine_dictionary[(reihe, spalte)] = aktueller_zug[(reihe, spalte)]
            punktestand[aktueller_spieler] += score
            for i in ablagebank_buchstaben:
                ablagebank[aktueller_spieler].remove(i)
            fülle_ablagebank(beutel, 7 - len(ablagebank[aktueller_spieler]), ablagebank[aktueller_spieler])
            nachricht_drucken("Computer moved " + word + " and got " + str(score) + " points.", grün)
        aktualisiere_brett()
        aktueller_zug = {}
        aktueller_spieler = (aktueller_spieler + 1) % anzahl_spieler
        spieler_drucken(anzahl_spieler, aktueller_spieler, computer_spieler)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            print(markierter_buchstabenstein, ablagebank[aktueller_spieler][markierte_spalte])
            if markierter_buchstabenstein[0] == '*':
                if pygame.K_a <= event.key <= pygame.K_z:
                    ablagebank[aktueller_spieler][markierte_spalte] = '*' + chr(ord('a') + event.key - pygame.K_a)
                    print("changing * to ", ablagebank[aktueller_spieler][markierte_spalte])
                    markiere_buchstaben(reihe, spalte, ablagebank[aktueller_spieler][spalte])
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x -= abstand
            y -= abstand
            spalte = int(x // kästchen_größe)
            reihe = int(y // kästchen_größe)
            # Fall, wo Ablagebank angeklickt wird
            if reihe == 15 and 0 <= spalte < len(ablagebank[aktueller_spieler]):
                if not renew_modus:
                    print(ablagebank[aktueller_spieler][spalte])
                    markiere_buchstaben(reihe, spalte, ablagebank[aktueller_spieler][spalte])
                    nachricht_drucken((""), dunkelgrün)
                if renew_modus:
                    helfer_fuer_markierte_buchstaben(lila, lila, reihe, spalte, ablagebank[aktueller_spieler][spalte])
                    renew_buchstaben.append(ablagebank[aktueller_spieler][spalte])
            else:
                # Fall, wo man einen Buchstaben auf das Brett überträgt
                if markierte_reihe>0 and 0 <= reihe < 15 and 0 <= spalte < 15 and (reihe, spalte) not in buchstabensteine_dictionary and (reihe, spalte) not in aktueller_zug:
                    if markierter_buchstabenstein == '*':
                        nachricht_drucken("Please assign Blanko before moving.", rot)
                        reihe = markierte_reihe
                        spalte = markierte_spalte
                        break
                    aktueller_zug[(reihe, spalte)]=markierter_buchstabenstein
                    print(markierte_reihe)
                    drucke_kaestchen_mit_buchstabe(reihe, spalte, markierter_buchstabenstein, hautfarbe)
                    ablagebank[aktueller_spieler].pop(markierte_spalte)
                    markierte_reihe=0
                    markierte_spalte=0
                    drucke_ablagebank(ablagebank[aktueller_spieler])
                # Fall, wo cancel gedruckt wird
                if ((reihe, spalte)) == (15, 12):
                    aktualisiere_brett()
                    for (reihe, spalte) in aktueller_zug:
                        kästchen_drucken(reihe, spalte)
                        ablagebank[aktueller_spieler].append(aktueller_zug[(reihe, spalte)])
                    aktueller_zug={}
                    renew_buchstaben = []
                    drucke_ablagebank(ablagebank[aktueller_spieler])
                    nachricht_drucken((""), dunkelgrün)
                    renew_modus = False
                # Fall, wo renew gedruckt wird
                if ((reihe, spalte)) == (15, 11):
                    if aktueller_zug != {}:
                        nachricht_drucken("Please press Back before Renew", rot)
                        break
                    if renew_modus:
                        nachricht_drucken("Please press Done to finish Renew", rot)
                        break
                    renew_modus = True

                # Fall, wo pass gedruckt wird
                if ((reihe, spalte)) == (15, 10):
                    aktualisiere_brett()
                    for (reihe, spalte) in aktueller_zug:
                        kästchen_drucken(reihe, spalte)
                        ablagebank[aktueller_spieler].append(aktueller_zug[(reihe, spalte)])
                    aktueller_spieler = (aktueller_spieler + 1) % anzahl_spieler
                    for i in range(len(ablagebank[aktueller_spieler])):
                        entferne_von_der_ablagebank(15, i)
                    nachricht_drucken(("You passed"), grün)
                    aktueller_zug={}
                    spieler_drucken(anzahl_spieler, aktueller_spieler, computer_spieler)
                    anzahl_pass += 1
                # Fall, wo done gedruckt wird
                if ((reihe, spalte)) == (15, 13):
                    markierter_buchstabenstein = ' '
                    markierte_spalte = 0
                    markierte_reihe = 0
                    anzahl_pass = 0
                    if renew_modus:
                        if renew_buchstaben == []:
                            nachricht_drucken("Please select letters to renew", rot)
                            break
                        else:
                            for letter in renew_buchstaben:
                                beutel.append(letter[0])
                                ablagebank[aktueller_spieler].remove(letter)
                            random.shuffle(beutel)
                            fülle_ablagebank(beutel, len(renew_buchstaben), ablagebank[aktueller_spieler])
                            renew_modus = False
                            aktueller_spieler = (aktueller_spieler + 1) % anzahl_spieler
                            spieler_drucken(anzahl_spieler, aktueller_spieler, computer_spieler)
                            for i in range(len(ablagebank[aktueller_spieler])):
                                entferne_von_der_ablagebank(15, i)
                            renew_buchstaben = []
                        break
                    else:
                        woerter = neu_woerter_entstanden(aktueller_zug)
                        if woerter == []:
                            nachricht_drucken("Invalid move", rot)
                        else:
                            falsche_woerter, richtig_woerter, score = alle_woerter_sind_gueltig(woerter, aktueller_zug)
                            if score < 0:
                                nachricht_drucken(
                                    str(len(falsche_woerter)) + "invalid word(s): " + ','.join(falsche_woerter), rot)
                                continue
                            nachricht_drucken(
                                "Good move. You got " + str(score) + " points for " + ','.join(richtig_woerter), grün)
                            fülle_ablagebank(beutel, 7 - len(ablagebank[aktueller_spieler]), ablagebank[aktueller_spieler])
                            punktestand[aktueller_spieler] += score
                            aktueller_spieler = (aktueller_spieler + 1) % anzahl_spieler
                            spieler_drucken(anzahl_spieler, aktueller_spieler, computer_spieler)
                            for i in range(len(ablagebank[aktueller_spieler])):
                                entferne_von_der_ablagebank(15, i)
                            for (reihe, spalte) in aktueller_zug:
                                buchstabensteine_dictionary[(reihe, spalte)] = aktueller_zug[(reihe, spalte)]
                            aktualisiere_brett()
                            aktueller_zug = {}
                if ((reihe, spalte)) == (-1, 13):
                    print("came here")
                    drucke_ablagebank(ablagebank[aktueller_spieler])
                if ((reihe, spalte)) == (-1, 14):
                    for i in range(len(ablagebank[aktueller_spieler])):
                        entferne_von_der_ablagebank(15, i)
        else:
            pass

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()