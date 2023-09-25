import pygame
import random

# Farben
hellblau = (179, 250, 255)
schwarz = (0, 0, 0)
dunkelblau = (40, 60, 200)
gelb = (253, 208, 23)
gruen = (20, 200, 20)
pink = (212, 17, 156)
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
    return id // brett_groesse, id % brett_groesse


# Sucht nachbarkaestchen
def suche_nachbarkaestchen(kaestchen):
    (reihe, spalte) = umrechnen(kaestchen)
    nachbarkaestchen = [(reihe - 1, spalte), (reihe, spalte + 1), (reihe + 1, spalte), (reihe, spalte - 1)]
    set2 = []
    for (r, s) in nachbarkaestchen:
        if 0 <= r < brett_groesse and 0 <= s < brett_groesse and id(r, s) not in besucht:
            set2.append(id(r, s))
    return set2


# Kaestchen wo man schon war
def besuchte_nachbarkaestchen(kaestchen):
    (reihe, spalte) = umrechnen(kaestchen)
    nachbarkaestchen = [(reihe - 1, spalte), (reihe, spalte + 1), (reihe + 1, spalte), (reihe, spalte - 1)]
    set2 = []
    for (r, s) in nachbarkaestchen:
        if 0 <= r < brett_groesse and 0 <= s < brett_groesse and id(r, s) in besucht:
            set2.append(id(r, s))
    return set2


beginn = random.randint(0, brett_groesse ** 2 - 1)
besucht = [beginn]
nachbarkaestchen = suche_nachbarkaestchen(beginn)


# Labyrinth wird hergestellt
def prim_algorithmus():
    while nachbarkaestchen:
        position = nachbarkaestchen.pop(random.randint(0, len(nachbarkaestchen) - 1))
        if position in besucht:
            continue
        besuchte_nachbarn = besuchte_nachbarkaestchen(position)
        beliebiges_kaestchen = random.choice(besuchte_nachbarn)
        luecken_list[position].append(beliebiges_kaestchen)
        luecken_list[beliebiges_kaestchen].append(position)
        besucht.append(position)
        nachbarn = suche_nachbarkaestchen(position)
        if nachbarn:
            nachbarkaestchen.extend(nachbarn)


# Lücken hinzufügen
def drucke_wand(ll):
    luecken_laenge = kaestchen_groesse - 4
    for erste in range(len(ll)):
        for zweite in ll[erste]:
            (r1, s1) = umrechnen(erste)
            (r2, s2) = umrechnen(zweite)
            if r1 == r2:
                pygame.draw.rect(fenster, hellblau,
                                 pygame.Rect(max(s1, s2) * kaestchen_groesse - 2, (r1 + 0.5) * kaestchen_groesse
                                             - luecken_laenge / 2, 4, luecken_laenge))
            if s1 == s2:
                pygame.draw.rect(fenster, hellblau,
                                 pygame.Rect((s1 + 0.5) * kaestchen_groesse - luecken_laenge / 2, max(r1, r2)
                                             * kaestchen_groesse - 2, luecken_laenge, 4))
    pygame.display.flip()


# Karriert
for reihe in range(brett_groesse):
    for spalte in range(brett_groesse):
        pygame.draw.rect(fenster, dunkelblau,
                         pygame.Rect(reihe * kaestchen_groesse, spalte * kaestchen_groesse, kaestchen_groesse,
                                     kaestchen_groesse), 2)
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
        if id(kordi[0] + 1, kordi[1]) in luecken_list[id(kordi[0], kordi[1])]:
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


def zeichne_weg(weg, farbe, doppelt_farbe=None):
    kordi = weg[0]
    abstand = kaestchen_groesse / 2
    besuchte_linien = []
    for neue_kordi in weg[1:]:
        if (kordi, neue_kordi) not in besuchte_linien:
            pygame.draw.line(fenster, farbe,
                             (kordi[1] * kaestchen_groesse + abstand, kordi[0] * kaestchen_groesse + abstand),
                             (neue_kordi[1] * kaestchen_groesse + abstand, neue_kordi[0] * kaestchen_groesse + abstand),
                             3)
            besuchte_linien.append((neue_kordi, kordi))
        else:
            pygame.draw.line(fenster, doppelt_farbe,
                             (kordi[1] * kaestchen_groesse + abstand, kordi[0] * kaestchen_groesse + abstand),
                             (neue_kordi[1] * kaestchen_groesse + abstand, neue_kordi[0] * kaestchen_groesse + abstand),
                             3)
        # time.sleep(0.1)
        kordi = neue_kordi
        pygame.display.flip()


def schnellste_weg_hand_solved(weg):
    kordi = weg[0]
    besuchte_linien = []
    doppelt = []
    schnellste_weg = [kordi]
    for neue_kordi in weg[1:]:
        if (kordi, neue_kordi) not in besuchte_linien:
            besuchte_linien.append((neue_kordi, kordi))
        else:
            doppelt.append((kordi, neue_kordi))
        kordi = neue_kordi
    for linie in besuchte_linien:
        if linie not in doppelt:
            schnellste_weg.append((linie[0]))
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
            sicht_richtung = (sicht_richtung - 1) % 4
        else:
            sicht_richtung = (sicht_richtung + 1) % 4
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
            sicht_richtung = (sicht_richtung + 1) % 4
        else:
            sicht_richtung = (sicht_richtung - 1) % 4
    return weg


def dijkstra(ll):
    shortest_path = []
    pred_dict = {}
    frontier = [0]
    running = True
    while running:
        current = frontier.pop(0)
        for neighbor in ll[current]:
            if neighbor not in pred_dict:
                pred_dict[neighbor] = current
                frontier.append(neighbor)
                if neighbor == id(brett_groesse - 1, brett_groesse - 1):
                    cell = id(brett_groesse - 1, brett_groesse - 1)
                    shortest_path.append(umrechnen(cell))
                    while cell != 0:
                        cell = pred_dict[cell]
                        shortest_path.append(umrechnen(cell))
                    running = False
    shortest_path.reverse()
    return shortest_path


right_hand_solved = right_handed_solver()
zeichne_weg(right_hand_solved, gelb, gruen)
dijkstra_solved = dijkstra(luecken_list)
zeichne_weg(dijkstra_solved, pink)
right_hand_solved = schnellste_weg_hand_solved(right_hand_solved)
print(right_hand_solved)
print(dijkstra_solved)
print(right_hand_solved == dijkstra_solved)

input()
