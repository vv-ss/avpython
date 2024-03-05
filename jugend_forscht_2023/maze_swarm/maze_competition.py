import random
import time

candy_range = 25

name = input('Name: ')

maze_num = random.randint(1, 25)
print('Hallo ' + name + ', deine Irrgartennummer lautet: ' + str(maze_num) + '. \n'
                        'Versuche diesen Irrgarten so schnell wie möglich zu lösen. \n'
                        'Um zu beginnen, drücke die Entertaste. \n'
                        'Sobald du fertig bist, erfährst du deine gebrauchte Zeit.')
input()
print('Die Zeit läuft...')
start = time.time()
input()
maze_solving_time = time.time() - start
file = open('maze_solver_ranking.txt', 'a')
file.write(name + ' | ' + str(maze_num) + ' | ' + str(maze_solving_time) + '\n')

print('Du hast insgesamt ' + str(maze_solving_time) + ' Sekunden gebraucht.')
if maze_solving_time <= candy_range:
    print('Das war schnell! Du darfst dir eine Belohnung abhohlen.')
else:
    print('Danke, dass du da warst!')