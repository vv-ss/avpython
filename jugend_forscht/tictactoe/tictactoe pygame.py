import pygame
from pygame.locals import *
import random

groessen_faktor = 1
Wert_dict = {}
com_ist_dran = True
kaestchen_groesse = 200*groessen_faktor

# Welche Züge kann der Spieler ziehen
def naechste_spieler_zuege(brettzustand):
    zuege = []
    for kaestchen in range(0, len(brettzustand)):
        if brettzustand[kaestchen] == '0':
            x = list(brettzustand)
            x[kaestchen] = '2'
            zuege.append(''.join(x))
    return zuege

# Welche Züge kann der Computer ziehen
def naechste_com_zuege(brettzustand):
    naechste_zuege = []
    for kaestchen in range(0, len(brettzustand)):
        if brettzustand[kaestchen] == '0':
            x = list(brettzustand)
            x[kaestchen] = '1'
            naechste_zuege.append(''.join(x))
    return naechste_zuege

# Unentschieden
def unentschieden(brettzustand):
    if spieler_hat_gewonnen(brettzustand) or com_hat_gewonnen(brettzustand) or '0' in brettzustand:
        return False
    else:
        return True

# Positionen, wie die Lage aussehen könnte, wenn der Spieler gewinnt
def spieler_hat_gewonnen(n):
    if len(n) == 9:
        if n[0] == n[3] == n[6] == '2':
            spieler_sieg = True
        elif n[1] == n[4] == n[7] == '2':
            spieler_sieg = True
        elif n[2] == n[5] == n[8] == '2':
            spieler_sieg = True
        elif n[0] == n[1] == n[2] == '2':
            spieler_sieg = True
        elif n[3] == n[4] == n[5] == '2':
            spieler_sieg = True
        elif n[6] == n[7] == n[8] == '2':
            spieler_sieg = True
        elif n[0] == n[4] == n[8] == '2':
            spieler_sieg = True
        elif n[2] == n[4] == n[6] == '2':
            spieler_sieg = True
        else:
            spieler_sieg = False
        return spieler_sieg
    if len(n) == 16:
        if n[0] == n[4] == n[8] == n[12] == '2':
            spieler_sieg = True
        elif n[1] == n[5] == n[9] == n[13] == '2':
            spieler_sieg = True
        elif n[2] == n[6] == n[10] == n[14] == '2':
            spieler_sieg = True
        elif n[3] == n[7] == n[11] == n[15] == '2':
            spieler_sieg = True
        elif n[0] == n[1] == n[2] == n[3] == '2':
            spieler_sieg = True
        elif n[4] == n[5] == n[6] == n[7] == '2':
            spieler_sieg = True
        elif n[8] == n[9] == n[10] == n[11] == '2':
            spieler_sieg = True
        elif n[12] == n[13] == n[14] == n[15] == '2':
            spieler_sieg = True
        elif n[0] == n[5] == n[10] == n[15] == '2':
            spieler_sieg = True
        elif n[3] == n[6] == n[9] == n[12] == '2':
            spieler_sieg = True
        else:
            spieler_sieg = False
        return spieler_sieg


# Positionen, wie die Lage aussehen könnte, wenn der Computer gewinnt
def com_hat_gewonnen(n):
   if len(n) == 9:
       if n[0] == n[3] == n[6] == '1':
           com_sieg = True
       elif n[1] == n[4] == n[7] == '1':
           com_sieg = True
       elif n[2] == n[5] == n[8] == '1':
           com_sieg = True
       elif n[0] == n[1] == n[2] == '1':
           com_sieg = True
       elif n[3] == n[4] == n[5] == '1':
           com_sieg = True
       elif n[6] == n[7] == n[8] == '1':
           com_sieg = True
       elif n[0] == n[4] == n[8] == '1':
           com_sieg = True
       elif n[2] == n[4] == n[6] == '1':
           com_sieg = True
       else:
           com_sieg = False
       return com_sieg
   if len(n) == 16:
       if n[0] == n[4] == n[8] == n[12] == '1':
           com_sieg = True
       elif n[1] == n[5] == n[9] == n[13] == '1':
           com_sieg = True
       elif n[2] == n[6] == n[10] == n[14] == '1':
           com_sieg = True
       elif n[3] == n[7] == n[11] == n[15] == '1':
           com_sieg = True
       elif n[0] == n[1] == n[2] == n[3] == '1':
           com_sieg = True
       elif n[4] == n[5] == n[6] == n[7] == '1':
           com_sieg = True
       elif n[8] == n[9] == n[10] == n[11] == '1':
           com_sieg = True
       elif n[12] == n[13] == n[14] == n[15] == '1':
           com_sieg = True
       elif n[0] == n[5] == n[10] == n[15] == '1':
           com_sieg = True
       elif n[3] == n[6] == n[9] == n[12] == '1':
           com_sieg = True
       else:
           com_sieg = False
       return com_sieg
# Ist der Computer dran?
def com_dran(state):
    X = 0
    O = 0
    for kaestchen in state:
        if kaestchen == '1':
            O += 1
        if kaestchen == '2':
            X += 1
    if O == X:
        if com_ist_dran:
            return True
        else:
            return False
    else:
        if not com_ist_dran:
            return True
        else:
            return False

# Wir geben jedem möglichen Zug einen Wert
def berechne_wert(state):
    #print("Came to get_wert for ", state)
    if state in Wert_dict:
        return Wert_dict[state]
    #print("Wert not found in dict for ", state)
    if com_hat_gewonnen(state):
        return 100
    if spieler_hat_gewonnen(state):
        return -100
    if unentschieden(state):
        return 0
    alle_werte = []
    state_wert = 0
    if com_dran(state):
        for zug in naechste_com_zuege(state):
            alle_werte.append(berechne_wert(zug))
        state_wert = max(alle_werte)
    else:
        for zug in naechste_spieler_zuege(state):
            alle_werte.append(berechne_wert(zug))
        state_wert = min(alle_werte)
    Wert_dict[state] = state_wert
    return state_wert

# In welches Kästchen soll der Computer ziehen?
def com_zug(state):
    next_states = naechste_com_zuege(state)
    next_best_state = next_states[0]
    next_best_wert = berechne_wert(next_best_state)
    for i in next_states:
        wert = berechne_wert(i)
        if wert > next_best_wert:
            next_best_wert = wert
            next_best_state = i
    for i in range(0, len(state)):
        if state[i] != next_best_state[i]:
            return i

# Der Computer zieht einen beliebigen Zug, sodass der Spieler auch gewinnen kann(einfache Spielvariante)
def beliebiger_com_zug(state):
    while True:
        x = random.randint(0, len(state)-1)
        if state[x] == '0':
            return x

# Farben, die später gebraucht werden
dunkelblau=(0, 0, 139)
gold=(253, 218, 13)
dunkelgruen2=(50, 110, 100)
rot= (255, 87, 51)
dunkelgruen=(0, 100, 0)
gruen = (0, 255, 0)
türkis=(64, 224, 208)
orange = (255,165,0)
hellblau=(150, 230, 250)
lila=(128, 0, 128)
pygame.init()
# Schriften, die später gebraucht werden
font_style = pygame.font.SysFont("bahnschrift", 50*groessen_faktor)
font_style2 = pygame.font.SysFont("comicschrift", 100*groessen_faktor)

# Der Computer berechnet mithilfe der Kordinaten in welches Kästchen der Spieler ziehen möchte
def spieler_klick():
    x, y = pygame.mouse.get_pos()
    column = x // kaestchen_groesse
    row = y // kaestchen_groesse
    return (row, column)

# Das Brett wird in der Größe 3/4 gemalt
def drucke_brett(groesse):
    abstand = 60*groessen_faktor
    surface = pygame.display.set_mode((groesse * kaestchen_groesse, groesse * kaestchen_groesse))
    surface.fill(rot)
    pygame.display.set_caption('Tik Tak Toe by Aarav and Viyona')
    for n in range(1, groesse):
        # Striche, die senkrecht sind
        pygame.draw.rect(window, hellblau, pygame.Rect(n * kaestchen_groesse, abstand, 5, groesse * kaestchen_groesse - 2 * abstand))
        # Striche, die waagerecht sind
        pygame.draw.rect(window, hellblau, pygame.Rect(abstand, n * kaestchen_groesse, groesse * kaestchen_groesse - 2 * abstand, 5))
    text = font.render('TicTacToe', True, lila)
    surface.blit(text, (groesse * kaestchen_groesse / 2 - 75, 2))
    return surface

# Der Hintergrund der Farben wird gemalt
breite=1300*groessen_faktor
hoehe=800*groessen_faktor
window = pygame.display.set_mode((breite, hoehe))
pygame.display.set_caption('Tik Tak Toe by Aarav and Viyona')
font = pygame.font.Font('freesansbold.ttf', 24)
green_cover=pygame.draw.rect(window, türkis, pygame.Rect(0, 0, breite, hoehe))

# Computer frägt erste Frage
erste_frage=font_style.render('Do you want to play against easy or hard(e/h)?', True, lila)
window.blit(erste_frage, (50*groessen_faktor, 200*groessen_faktor))
pygame.display.flip()

# Computer beobachtet bis der Spieler "e" oder "h" drückt
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
erste_antwort=font_style.render("You chose " + computer_stufe, True, dunkelgruen)
window.blit(erste_antwort, (50*groessen_faktor, 250*groessen_faktor))
pygame.display.flip()

# Computer frägt zweite Frage
zweite_frage=font_style.render('Do you want to play on 3x3 or 4x4 (3/4)?', True, lila)
window.blit(zweite_frage, (50*groessen_faktor, 370*groessen_faktor))
pygame.display.flip()

# Computer beobachtet bis der Spieler "3" oder "4" drückt
brett_groesse = None
while True:
    if (brett_groesse):
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                print("Key 3 has been pressed")
                brett_groesse = 3
                break
            if event.key == pygame.K_4:
                brett_groesse = 4
                print("Key 4 has been pressed")
                break

# Computer schreibt die Antwort der zweiten Frage darunter
zweite_antwort=font_style.render("You chose " + str(brett_groesse) + 'x' + str(brett_groesse), True, dunkelgruen)
window.blit(zweite_antwort, (50*groessen_faktor, 420*groessen_faktor))
pygame.display.flip()

# Computer frägt dritte Frage
dritte_frage=font_style.render('Do you want to move first(y/n)?', True, lila)
window.blit(dritte_frage, (50*groessen_faktor, 540*groessen_faktor))
pygame.display.flip()

# Computer beobachtet bis der Spieler "n" oder "y" drückt
# Computer beobachtet bis der Spieler "n" oder "y" drückt
spieler_faengt_an = None
while True:
    if spieler_faengt_an:
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                print("Key Y has been pressed")
                spieler_faengt_an = 'Y'
                break
            if event.key == pygame.K_n:
                spieler_faengt_an = 'N'
                print("Key N has been pressed")
                break

# So läuft das Spiel ab
def game():
    global com_ist_dran
    if spieler_faengt_an == 'Y':
        com_ist_dran = False
    surface = drucke_brett(brett_groesse)
    pygame.display.flip()
    spielstand = '0'*(brett_groesse * brett_groesse)
    while True:
        # Wenn es Unentschieden ist oder jemand gewonnen hat, soll der Computer hinschreiben wie das Spiel geendet ist
        if unentschieden(spielstand):
            computerwin = font_style.render('DRAW!!!', True, lila)
            surface.blit(computerwin, (brett_groesse * kaestchen_groesse / 2 - 200, brett_groesse * kaestchen_groesse - 50*groessen_faktor))
            pygame.display.flip()
            break
        if com_hat_gewonnen(spielstand):
            computerwin = font_style.render('COMPUTER WON!!!', True, lila)
            surface.blit(computerwin, (brett_groesse * kaestchen_groesse / 2 - 225, brett_groesse * kaestchen_groesse - 50*groessen_faktor))
            pygame.display.flip()
            break
        if spieler_hat_gewonnen(spielstand):
            computerwin = font_style.render('PLAYER WON!!!', True, lila)
            surface.blit(computerwin, (brett_groesse * kaestchen_groesse / 2 - 225, brett_groesse * kaestchen_groesse - 50*groessen_faktor))
            pygame.display.flip()
            break
        if com_dran(spielstand):
            if computer_stufe == 'Hard':
                zeros = 0
                for i in range(0, brett_groesse * brett_groesse):
                    if spielstand[i] == '0':
                        zeros = zeros + 1
                if zeros > 12:
                    move = beliebiger_com_zug(spielstand)
                else:
                    move = com_zug(spielstand)
            else:
                # Der Computer malt
                move = beliebiger_com_zug(spielstand)
            reihe = move // brett_groesse
            spalte = move % brett_groesse
            Oletter = font_style2.render('O', True, dunkelblau)
            surface.blit(Oletter, (kaestchen_groesse * spalte + kaestchen_groesse / 3 + 10, kaestchen_groesse * reihe + kaestchen_groesse / 3 + 10))
            pygame.display.update()
            state_list = list(spielstand)
            state_list[move] = '1'
            spielstand = ''.join(state_list)
        else:
            # Player turn
            moved = False
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        (reihe, spalte) = spieler_klick()
                        if spielstand[reihe * brett_groesse + spalte] != '0':
                            break
                        print(reihe, spalte)
                        Xletter=font_style2.render('X', True, gold)
                        surface.blit(Xletter, (kaestchen_groesse * spalte + kaestchen_groesse / 3 + 10, kaestchen_groesse * reihe + kaestchen_groesse / 3 + 10))
                        pygame.display.update()
                        moved = True
                        break
                    else:
                        pass
                if moved:
                    state_list = list(spielstand)
                    state_list[reihe * brett_groesse + spalte] = '2'
                    spielstand = ''.join(state_list)
                    break

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            else:
                pass
game()
#