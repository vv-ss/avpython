import time
import pygame
import random

# Farben
hellblau = (179, 250, 255)
schwarz = (0, 0, 0)
dunkelblau = (40, 60, 200)
gelb = (253, 208, 23)
gruen = (20, 200, 20)
RECHTS, UNTEN, LINKS, OBEN = range(4)

# Fenster gestalten
pygame.init()


brett_groesse = 30
kaestchen_groesse = 30
breite = brett_groesse * kaestchen_groesse
hoehe = brett_groesse * kaestchen_groesse
fenster = pygame.display.set_mode((breite, hoehe))
pygame.display.set_caption('random maze drawing by Aarav and Viyona')
fenster.fill(hellblau)
pygame.display.flip()

luecken_list = [[] for x in range(brett_groesse ** 2)]

def id(reihe, spalte):
    return reihe * brett_groesse + spalte

def umrechnen(id):
    return (id // brett_groesse, id % brett_groesse)

# Sucht nachbarkaestchen
def suche_nachbarkaestchen(kaestchen):
    (reihe, spalte) = umrechnen(kaestchen)
    nachbarkaestchen = [(reihe - 1, spalte), (reihe, spalte + 1), (reihe + 1, spalte), (reihe, spalte - 1)]
    set2= []
    for (r, s) in nachbarkaestchen:
        if r >= 0 and r < brett_groesse and s >= 0 and s < brett_groesse and id(r, s) not in besucht:
            set2.append(id(r, s))
    return set2

# Kaestchen wo man schon war
def besuchte_nachbarkaestchen(kaestchen):
    (reihe, spalte) = umrechnen(kaestchen)
    nachbarkaestchen = [(reihe - 1, spalte), (reihe, spalte + 1), (reihe + 1, spalte), (reihe, spalte - 1)]
    set2 = []
    for (r, s) in nachbarkaestchen:
        if r >= 0 and r < brett_groesse and s >= 0 and s < brett_groesse and id(r, s) in besucht:
            set2.append(id(r, s))
    return set2

beginn = random.randint(0, brett_groesse ** 2 - 1)
besucht = [beginn]
nachbarkaestchen = suche_nachbarkaestchen(beginn)

# Labyrinth wird hergestellt
def prim_algorithmus():
    while nachbarkaestchen != []:
        position = nachbarkaestchen.pop(random.randint(0, len(nachbarkaestchen)-1))
        if position in besucht:
            continue
        besuchte_nachbarn = besuchte_nachbarkaestchen(position)
        beliebiges_kaestchen = random.choice(besuchte_nachbarn)
        luecken_list[position].append(beliebiges_kaestchen)
        luecken_list[beliebiges_kaestchen].append(position)
        besucht.append(position)
        nachbarn = suche_nachbarkaestchen(position)
        if nachbarn != []:
            nachbarkaestchen.extend(nachbarn)

# Lücken hinzufügen
def drucke_wand(luecken_list):
    for erste in range(len(luecken_list)):
        for zweite in luecken_list[erste]:
            (r1, s1) = umrechnen(erste)
            (r2, s2) = umrechnen(zweite)
            if r1 == r2:
                pygame.draw.rect(fenster, hellblau, pygame.Rect(max(s1, s2) * kaestchen_groesse - 2, r1 * kaestchen_groesse + 2, 4, kaestchen_groesse - 4))
            if s1 == s2:
                pygame.draw.rect(fenster, hellblau, pygame.Rect(s1 * kaestchen_groesse + 2, max(r1, r2) * kaestchen_groesse - 2, kaestchen_groesse - 4, 4))
    pygame.display.flip()

# Karriert
for reihe in range(brett_groesse):
    for spalte in range(brett_groesse):
        pygame.draw.rect(fenster, dunkelblau, pygame.Rect(reihe * kaestchen_groesse, spalte * kaestchen_groesse, kaestchen_groesse, kaestchen_groesse), 2)
pygame.display.flip()

# Bewege punkt
def bewegung(kordi, richtung):
    if richtung == OBEN:
        if id(kordi[0] - 1, kordi[1]) in luecken_list[id(kordi[0], kordi[1])]:
            if kordi[0] != 0:
                return kordi[0] - 1, kordi[1]
            return kordi
        else:
            return kordi
    if richtung == UNTEN:
        if  id(kordi[0] + 1, kordi[1]) in luecken_list[id(kordi[0], kordi[1])]:
            if kordi[0] != brett_groesse - 1:
                return kordi[0] + 1, kordi[1]
            return kordi
        else:
            return kordi
    if richtung == RECHTS:
        if id(kordi[0], kordi[1] + 1) in luecken_list[id(kordi[0], kordi[1])]:
            if kordi[1] != brett_groesse - 1:
                return kordi[0], kordi[1] + 1
            return kordi
        else:
            return kordi
    if richtung == LINKS:
        if id(kordi[0], kordi[1] - 1) in luecken_list[id(kordi[0], kordi[1])]:
            if kordi[1] != 0:
                return kordi[0], kordi[1] - 1
            return kordi
        else:
            return kordi


prim_algorithmus()
print(luecken_list)
drucke_wand(luecken_list)
print(bewegung((0, 0), OBEN))
print(bewegung((0, 0), RECHTS))
print(bewegung((0, 0), UNTEN))
print(bewegung((0, 0), LINKS))

# SOLVE THE MAZE! PART 1.
# Try going from (0,0) to (MAX, MAX)
# follow your left hand.

def bewegen(weg):
    kordi = weg.pop(0)
    abstand = kaestchen_groesse/2
    besuchte_linien = []
    doppelt = []
    schnellste_weg = []
    for neue_kordi in weg:
        print(kordi, neue_kordi)
        if (kordi, neue_kordi) not in besuchte_linien:
            pygame.draw.line(fenster, gelb, (kordi[1] * kaestchen_groesse + abstand, kordi[0] * kaestchen_groesse + abstand), (neue_kordi[1] * kaestchen_groesse + abstand, neue_kordi[0] * kaestchen_groesse + abstand), 3)
            besuchte_linien.append((neue_kordi, kordi))
        else:
            pygame.draw.line(fenster, gruen, (kordi[1] * kaestchen_groesse + abstand, kordi[0] * kaestchen_groesse + abstand), (neue_kordi[1] * kaestchen_groesse + abstand, neue_kordi[0] * kaestchen_groesse + abstand), 3)
            doppelt.append((kordi, neue_kordi))
        # time.sleep(0.1)
        kordi = neue_kordi
        pygame.display.flip()
    for i in besuchte_linien:
        if i not in doppelt:
            schnellste_weg.append((i[1], i[0]))
    return schnellste_weg

def left_handed_solver():
    weg = [(0, 0)]
    kordi = (0, 0)
    sicht_richtung = OBEN
    while kordi != (brett_groesse - 1, brett_groesse - 1):
        print("sicht richtung: ", sicht_richtung, kordi)
        neue_kordi = bewegung(kordi, sicht_richtung)
        if neue_kordi != kordi:
                weg.append(neue_kordi)
                kordi = neue_kordi
                sicht_richtung = (sicht_richtung - 1)%4
        else:
            sicht_richtung = (sicht_richtung + 1)%4
    return weg

def right_handed_solver():
    weg = [(0, 0)]
    kordi = (0, 0)
    sicht_richtung = OBEN
    while kordi != (brett_groesse - 1, brett_groesse - 1):
        print("sicht richtung: ", sicht_richtung, kordi)
        neue_kordi = bewegung(kordi, sicht_richtung)
        if neue_kordi != kordi:
                weg.append(neue_kordi)
                kordi = neue_kordi
                sicht_richtung = (sicht_richtung + 1)%4
        else:
            sicht_richtung = (sicht_richtung - 1)%4
    return weg


print(bewegen(right_handed_solver()))

input()
# [[1], [0, ]]
# SOLVE THE MAZE! PART 2.
# Show the shortest route from (0, 0) to (MAX, MAX).
