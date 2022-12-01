# Mit 'import random' öffnen wir die Bücherrei 'random', da wir sie später brauchen werden.
import random
Wert_dict = {}
com_move_first = True

def next_players_state(n):
   moves=[]
   for i in range(0, len(n)):
       if n[i]=='0':
           x = list(n)
           x[i]='2'
           moves.append(''.join(x))
   return moves
#TODO: states change, end_state change,
def next_com_state(n):
   next_states=[]
   for i in range(0, len(n)):
       if n[i]=='0':
           x = list(n)
           x[i]='1'
           next_states.append(''.join(x))
   return next_states

def draw(n):
    if is_player_end_state(n) or is_com_end_state(n) or '0' in n:
        return False
    else:
        return True

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
        else:
            player_win = False
    return player_win

def is_com_end_state(n):
    if n[0]==n[3]==n[6]=='1':
        computer_win = True
    elif n[1]==n[4]==n[7]=='1':
        computer_win = True
    elif n[2]==n[5]==n[8]=='1':
        computer_win = True
    elif n[0]==n[1]==n[2]=='1':
        computer_win = True
    elif n[3]==n[4]==n[5]=='1':
        computer_win = True
    elif n[6]==n[7]==n[8]=='1':
        computer_win = True
    elif n[0]==n[4]==n[8]=='1':
        computer_win = True
    elif n[2]==n[4]==n[6]=='1':
        computer_win = True
    else:
        computer_win = False
    return computer_win

def com_turn(state):
    X=0
    O=0
    for i in state:
        if i=='1':
            O+=1
        if i=='2':
            X+=1
    if O==X:
        if com_move_first:
            return True
        else:
            return False
    else:
        if not com_move_first:
            return True
        else:
            return False

def get_wert(state):
    if state in Wert_dict:
        return Wert_dict[state]
    if is_com_end_state(state):
        return 100
    if is_player_end_state(state):
        return -100
    if draw(state):
        return 0
    alle_werte=[]
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

def com_move(state):
    next_states = next_com_state(state)
    next_best_state = next_states[0]
    next_best_wert = get_wert(next_best_state)
    for i in next_states:
        wert = get_wert(i)
        if wert > next_best_wert:
            next_best_wert = wert
            next_best_state = i
    for i in range(0,9):
        if state[i] != next_best_state[i]:
            return i

def com_random_move(state):
    while True:
        x = random.randint(0,8)
        if state[x] == '0':
            return x

def convert_state_to_board(state,i):
    if state[i] == '0':
        return ' '
    if state[i] == '1':
        return 'O'
    if state[i] == '2':
        return 'X'

def printBoard3(state):
    print('__ __ __ __ __')
    print('|',convert_state_to_board(state,0),'|',convert_state_to_board(state,1),'|',convert_state_to_board(state,2),'|')
    print('__ __ __ __ __')
    print('|',convert_state_to_board(state,3),'|',convert_state_to_board(state,4),'|',convert_state_to_board(state,5),'|')
    print('__ __ __ __ __')
    print('|',convert_state_to_board(state,6),'|',convert_state_to_board(state,7),'|',convert_state_to_board(state,8),'|')
    print('__ __ __ __ __')

def printBoard4(state):
    print('__ __ __ __ __ __')
    print('|', convert_state_to_board(state, 0), '|', convert_state_to_board(state, 1), '|',
          convert_state_to_board(state, 2), '|', convert_state_to_board(state, 3), '|')
    print('__ __ __ __ __ __')
    print('|', convert_state_to_board(state, 4), '|', convert_state_to_board(state, 5), '|',
          convert_state_to_board(state, 6), '|', convert_state_to_board(state, 7), '|')
    print('__ __ __ __ __ __')
    print('|', convert_state_to_board(state, 8), '|', convert_state_to_board(state, 9), '|',
          convert_state_to_board(state, 10), '|', convert_state_to_board(state, 11), '|')
    print('__ __ __ __ __ __')
    print('|', convert_state_to_board(state, 12), '|', convert_state_to_board(state, 13), '|',
          convert_state_to_board(state, 14), '|', convert_state_to_board(state, 15), '|')


def game():
    global com_move_first
    brett_size=input('What size do you want? Give in 3,4 or 5.')
    stufe=input('Do you want an easy or a hard level?')
    first_move=input('Would you want to start(yes/no)')
    if first_move=='yes':
        com_move_first=False
    # Board zeigen
    state = '000000000'
    while True:
        printBoard3(state)
        if draw(state):
            print("IT WAS A DRAW!!!!!!!!!!!!!!")
            break
        if is_com_end_state(state):
            print("COMPUTER WON!!!!")
            break
        if is_player_end_state(state):
            print("PLAYER WON!!!!")
            break
        if com_turn(state):
            if stufe == 'hard':
                move = com_move(state)
            else:
                move = com_random_move(state)
            if state[int(move)] != '0':
                print('That place is already filled.')
                continue
            state_list = list(state)
            state_list[move] = '1'
            state = ''.join(state_list)
        else:
            print("It's your turn, move to which place?")
            move = input()
            state_list = list(state)
            state_list[int(move)] = '2'
            state = ''.join(state_list)

game()