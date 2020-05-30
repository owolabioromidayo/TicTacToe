import sys, copy
from math import inf as infinity
import random



# def flatten(arr):
#     flat =  [j  for i in arr for j in i]
#     return flat




def choice_to_index(state, choice):
    size = len(state)
    y = choice // size
    x = choice - y*size

    return y,x



def get_empty_cells(state):
    empty_cells = []
    size = len(state)
    for y in range(size):
        for x in range(size):
            if state[y][x] is ' ':
                empty_cells.append(y*size +x)

    return empty_cells


def check_win(state):
 
    d1, d2 = [],[]
    for idx,row in enumerate(state):
         #check rows
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0] 
    
        col = [row[idx] for row in state]
        if col.count(col[0]) == len(col) and col[0] != ' ':
            return col[0]


        d1.append(state[idx][idx])
        d2.append(state[idx][len(state)-1-idx])

    if d1.count(d1[0]) == len(d1) and d1[0] != ' ':
        return d1[0]

    if d2.count(d2[0]) == len(d2) and d2[0] != ' ':
        return d2[0]



    #check draw
    if get_empty_cells(state) == []: return 'draw'

    
    return None


    
def play_move(state, idx, player):
    y,x = choice_to_index(state, idx)
    state[y][x] = player 




def main_check_win(state):
    res = check_win(state)
    if res =='X' or res=='O' or res == "Draw": 
        print(f"Game over, {res} won") 
        sys.exit()


def print_state(state):
    print('----------------')
    for row in state:
        print(f"| {row[0]} || {row[1]} || {row[2]} |")
        print('----------------')

        

def main_play_move(state, choices, choice, player):
    y,x = choice_to_index(state, choice)
    state[y][x] = player
    choices.remove(choice)
    main_check_win(state)
    print_state(state)
    










def get_best_move(state, player):
    #word for word
    winner = check_win(state)
    # print(winner)
    if winner == 'O': return 1
    if winner == 'X': return -1
    if winner is 'draw': return 0

    moves, empty_cells = [], get_empty_cells(state)
    # print(empty_cells)

    for empty_cell in empty_cells:
        move = {}
        move['index'] = empty_cell
        new_state = copy.deepcopy(state)
        play_move(new_state, empty_cell, player)

        # move['score'] = get_best_move(new_state, 'X') if player == 'O' else get_best_move(new_state, 'O')
        if player == "O":
            move['score'] = get_best_move(new_state, 'X')
        else:
            move['score'] = get_best_move(new_state, 'O')


        moves.append(move)
    
    # print(moves) 


    best_move = None
    best = -infinity if player == 'O' else infinity
    
    if player == 'O':   
        for move in moves:
            if move['score'] > best:
                best = move['score']
                best_move = move['index']
    else:
        for move in moves:
            if move['score'] < best:
                best = move['score']
                best_move = move['index']

    # print(best_move)
    return best_move




def computer_choice(state, choices):
    choice = get_best_move(state, 'O')
    # choice  = random.choice(choices)
    main_play_move(state, choices, choice, 'O')
    

def player_choice(state, choices):
    while True:
        pchoice = int(input("Make a choice bucko : "))
        if pchoice in choices:
            main_play_move(state, choices, pchoice, 'X')
            break
    



def game():
    state = [[' ' for i in range(3)] for i in range(3)]
    choices = list(range(9))
    print_state(state)
    while True:
        player_choice(state, choices)
        computer_choice(state, choices)


if __name__ == "__main__":
    # print(flatten([[4 for i in range(3)] for i in range(3)]))
    game()